FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        brotli \
        ca-certificates \
        curl \
        erofs-utils \
        file \
        gh \
        git \
        lz4 \
        openjdk-17-jre \
        p7zip-full \
        python3 \
        python3-pip \
        python3-venv \
        unzip \
        wget \
        zip \
        zstd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN python3 -m pip install --break-system-packages -r requirements.txt

COPY . .

RUN if [ -f third_party/mezo_core/requirements.txt ]; then \
        python3 -m pip install --break-system-packages -r third_party/mezo_core/requirements.txt; \
    fi \
    && find tools -type f -exec chmod +x {} \; 2>/dev/null || true \
    && find third_party/mezo_core/bin -type f -exec chmod +x {} \; 2>/dev/null || true \
    && chmod +x /app/scripts/fly_entrypoint.sh

ENTRYPOINT ["/app/scripts/fly_entrypoint.sh"]
