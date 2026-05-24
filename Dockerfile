FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv

# Adding a virtual environment to the path
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Installing the system's core packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        brotli ca-certificates curl erofs-utils file gh git lz4 \
        openjdk-17-jre p7zip-full python3 python3-pip python3-venv \
        unzip wget zip zstd \
    && rm -rf /var/lib/apt/lists/*

# Creating and activating the virtual environment
RUN python3 -m venv $VIRTUAL_ENV

# Setting requirements within the virtual environment
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir \
        cryptography>=42.0.0 \
        httpx>=0.27.0 \
        protobuf>=4.25.0 \
        pycryptodome>=3.19.0 \
        requests>=2.31.0 \
        toml>=0.10.2 \
        zstandard>=0.22.0

COPY . .

# Virtual environment installation requirements 
RUN if [ -f third_party/mezo_core/requirements.txt ]; then \
        pip install -r third_party/mezo_core/requirements.txt; \
    fi \
    && find tools -type f -exec chmod +x {} \; 2>/dev/null || true \
    && find third_party/mezo_core/bin -type f -exec chmod +x {} \; 2>/dev/null || true \
    && chmod +x /app/scripts/fly_entrypoint.sh

ENTRYPOINT ["/app/scripts/fly_entrypoint.sh"]
