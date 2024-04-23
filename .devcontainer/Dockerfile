FROM python:3.12.2-slim-bookworm

# Install packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y install --no-install-recommends \
    sudo \
    libjpeg-dev \
    zlib1g-dev \
    git \
    gcc \
    g++ \
    build-essential \
    libffi-dev \
    libpango-1.0-0 \
    libpangoft2-1.0-0

# Install Python packages
RUN python3 -m pip install --upgrade \
    mkdocs \
    mkdocs-material \
    mkdocs-git-authors-plugin \
    mkdocs-git-revision-date-localized-plugin \
    pymdown-extensions \
    livereload \
    qrcode \
    mkdocs-mermaid2-plugin \
    mkdocs-static-i18n[material] \
    mkdocs-literate-nav \
    mike

# Install domWalters/mkdocs-to-pdf
# Patched to add some bugfixes
RUN git clone https://github.com/domWalters/mkdocs-to-pdf.git
WORKDIR /mkdocs-to-pdf
RUN pip install -e .
