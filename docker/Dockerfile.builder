FROM python:3.12-slim-bookworm

# System deps for ROM tool chain
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    zip unzip p7zip-full \
    zstd brotli lz4 \
    file ca-certificates curl wget \
    erofs-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /factory

# Python deps
COPY third_party/mezo_core/requirements.txt /tmp/mezo_requirements.txt
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt || true && \
    pip install --no-cache-dir flask && \
    pip install --no-cache-dir \
        cryptography httpx protobuf pycryptodome requests toml zstandard brotli \
        pyyaml || true

# Repo source
COPY . /factory

# Make binary tools executable
RUN find third_party/mezo_core/bin -type f -exec chmod +x {} \; 2>/dev/null || true

# Fly volume mount point for cache + workdir
RUN mkdir -p /data/cache /data/work /data/logs

EXPOSE 8080

CMD ["python", "server/builder_api.py"]
