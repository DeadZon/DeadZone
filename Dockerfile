FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /workspace

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        brotli \
        curl \
        erofs-utils \
        file \
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
RUN python3 -m pip install --break-system-packages --upgrade pip wheel \
    && python3 -m pip install --break-system-packages -r requirements.txt

COPY . .

RUN python3 -m pip install --break-system-packages -r third_party/mezo_core/requirements.txt \
    && find third_party/mezo_core/bin -type f -exec chmod +x {} \; \
    && chmod +x scripts/fly_entrypoint.sh

ENTRYPOINT ["scripts/fly_entrypoint.sh"]
