#!/usr/bin/env python

"""
MkDocs build and live preview
"""

import argparse
import os
import subprocess
import shutil
import yaml
from livereload import Server

def generate_index_html(languages, default_language):
    """
    Generate an index.html file for the root of the MkDocs site
    """
    index_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Redirecting...</title>
    <script>
            // List of available languages
            var availableLanguages = {available_languages}; // Dynamically populated
            var defaultLanguage = '{default_language}'; // Dynamically set

            // Function to find the best match for the user's preferred languages
            var getBestLanguageMatch = function(preferredLanguages, availableLanguages, defaultLanguage) {{
                for (var i = 0; i < preferredLanguages.length; i++) {{
                    var preferredLang = preferredLanguages[i].toLowerCase().split('-')[0]; // Consider only the primary language subtag
                    if (availableLanguages.includes(preferredLang)) {{
                        return preferredLang;
                    }}
                }}
                return defaultLanguage;
            }};

            // Get the best matching language
            var bestMatch = getBestLanguageMatch(navigator.languages, availableLanguages, defaultLanguage);

            // Construct the redirection URL
            var currentUrl = window.location.href;
            var newPath = currentUrl.endsWith('/') ? currentUrl + bestMatch : currentUrl + '/' + bestMatch;

            // Redirect to the matched language version of the site
            window.location.href = newPath;
    </script>
</head>
<body>
    <p>If you are not redirected, <a href="{default_language}/">click here to continue</a>.</p>
</body>
</html>
"""
    # Validate default_language
    if default_language not in languages:
        if languages:
            default_language = sorted(languages)[0]  # First language alphabetically
        else:
            default_language = "en"
            print("Error: Default language not available. Falling back to first available language.")
    # Format the template with actual values
    formatted_index = index_template.format(available_languages=languages, default_language=default_language)
    return formatted_index

def create_index_file_for_mkdocs(config_files, default_language):
    """
    Create an index.html file for language redirection in the root of the MkDocs site
    """
    site_dir = get_output_dir(config_files[0])
    site_dir_root = os.path.dirname(site_dir)

    languages = []
    for d in os.listdir(site_dir_root):
        if os.path.isdir(os.path.join(site_dir_root, d)):
            languages.append(d)

    index_html_content = generate_index_html(languages, default_language)

    # Write the generated index.html to the site directory
    with open(os.path.join(site_dir_root, "index.html"), "w", encoding="utf-8") as index_file:
        index_file.write(index_html_content)
    print(f"Created index.html for {site_dir_root} with languages {languages}")

def get_config_files(config_dir):
    """
    Get all mkdocs.yml files in the config directory
    """
    config_files = []
    for root, _, files in os.walk(config_dir):
        if "mkdocs.yml" in files:
            config_files.append(os.path.join(root, "mkdocs.yml"))
    return config_files

def get_output_dir(config_file):
    """
    Get the output directory for the MkDocs site
    """
    with open(config_file, "r", encoding="utf-8") as f:
        mkdocs_config = yaml.safe_load(f)
        output_dir = mkdocs_config.get("site_dir", "site")
        output_dir_absolute = os.path.join(os.path.dirname(config_file), output_dir)
        return output_dir_absolute

def get_source_dir(config_file):
    """
    Get the source directory for the MkDocs site
    """
    with open(config_file, "r", encoding="utf-8") as f:
        mkdocs_config = yaml.safe_load(f)
        source_dir = mkdocs_config.get("docs_dir", "docs")
        source_dir_absolute = os.path.join(os.path.dirname(config_file), source_dir)
        return source_dir_absolute

def build_mkdocs(build_options):
    """
    Build MkDocs site for each subfolder with mkdocs.yml
    """
    if build_options["clean"]:
        print("Cleaning output directory...")
        for config_file in build_options["config_files"]:
            output_dir = get_output_dir(config_file)
            subprocess.run(["rm", "-rf", output_dir], check=True)
    for config_file in build_options["config_files"]:
        print(f"Building MkDocs site using {os.path.dirname(config_file)}...")

        # Set ENABLE_PDF_EXPORT environment variable if build_options["PDFs"] is True
        if build_options["PDFs"]:
            # Copy the current environment variables
            env = os.environ.copy()
            # Add or update the ENABLE_PDF_EXPORT variable
            env["ENABLE_PDF_EXPORT"] = "1"
            subprocess.run(["mkdocs", "build", "-f", config_file], check=True, env=env)
        else:
            subprocess.run(["mkdocs", "build", "-f", config_file], check=True)

        # Copy extra folders to the site directory
        if build_options["extra"]:
            extra_folders = build_options["extra"].split(",")
            for folder in extra_folders:
                source_dir = os.path.dirname(get_source_dir(config_file))
                folder_path = os.path.join(source_dir, folder)
                destination_dir = os.path.join(get_output_dir(config_file), folder)
                shutil.copytree(folder_path, destination_dir, dirs_exist_ok=True)
                print(f"Copied {folder_path} to {destination_dir}")

    site_dir = get_output_dir(build_options["config_files"][0])
    site_dir_root = os.path.dirname(site_dir)

    if build_options["index_file"] is None:
        create_index_file_for_mkdocs(build_options["config_files"],
                                     build_options["default_lang"])
    else:
        shutil.copy(build_options["index_file"], site_dir_root)

    print("MkDocs sites built.")


def serve(build_options, port):
    """
    Serve MkDocs site and rebuild on file changes
    """
    server = Server()
    for config_file in build_options["config_files"]:
        server.watch(config_file, lambda: build_mkdocs(build_options))
        print(f"Watching {config_file} for changes...")
        docs_dir = get_source_dir(config_file)
        print(f"Watching {docs_dir} for changes...")
        server.watch(docs_dir + '/**/*.*', lambda: build_mkdocs(build_options))

    # Serve the MkDocs site
    site_dir = get_output_dir(build_options["config_files"][0])
    site_dir_root = os.path.dirname(site_dir)
    server.serve(root=site_dir_root, port=port)

def add_common_options(parser):
    """
    Add common options to the parser
    """
    parser.add_argument("-d", "--config",
                        type=str,
                        help="MkDocs configuration directory. Default is ./config",
                        default="./config")
    parser.add_argument("-i", "--index",
                        type=str,
                        help="Index file to place in the root of the output directory. "
                            "If not specified, one will be generated dynamically.",
                        default=None)
    parser.add_argument("-l", "--language",
                        type=str,
                        help="Default language for the index file. Default is 'en'",
                        default="en")
    parser.add_argument("-c", "--clean",
                        action="store_true",
                        help="Clean the output directory before building.")
    parser.add_argument("-f", "--full",
                        action="store_true",
                        help="Build with PDFs. Default is False.")
    parser.add_argument("-e", "--extra",
                        type=str,
                        help="Extra folders to copy to each site directory. Relative to parent of docs_dir.")

def main():
    """
    Main function setup with commands instead of flags
    """
    parser = argparse.ArgumentParser(description="MkDocs live preview")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Build command
    build_parser = subparsers.add_parser("build", help="Build MkDocs site")

    # Serve command
    serve_parser = subparsers.add_parser("serve", help="Start live preview")

    # Common arguments
    add_common_options(build_parser)
    add_common_options(serve_parser)

    # Serve-specific arguments
    serve_parser.add_argument("-p", "--port",
                              type=str,
                              help="Port mapping. Default is 8000",
                              default="8000")

    args = parser.parse_args()



    if args.command in ('build', 'serve'):
        build_options = {
            "config_files": get_config_files(args.config),
            "default_lang": args.language,
            "index_file": args.index,
            "clean": args.clean,
            "PDFs": args.full,
            "extra": args.extra
        }
        build_mkdocs(build_options)
        if args.command == "serve":
            serve(build_options, args.port)
    else:
        parser.print_help()

if __name__ == "__main__":
    # Define a custom YAML loader that ignores `!!python/name` tags
    def custom_yaml_loader(loader, tag_suffix, node):
        return str(node.value)

    # Register the custom tag handler with PyYAML
    yaml.SafeLoader.add_multi_constructor("tag:yaml.org,2002:python/name:", custom_yaml_loader)
    main()
