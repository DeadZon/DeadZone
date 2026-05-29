FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

WORKDIR /app
ENV PATH="/app/tools/helper/linux:/app/tools/helper:${PATH}"

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl wget unzip zip tar xz-utils zstd brotli file git android-sdk-libsparse-utils \
    || apt-get install -y --no-install-recommends \
    curl wget unzip zip tar xz-utils zstd brotli file git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt || true

COPY . /app

RUN python3 -c 'import json, platform, urllib.request; arch = platform.machine().lower(); aliases = {"x86_64": ("amd64", "x86_64"), "amd64": ("amd64", "x86_64"), "aarch64": ("arm64", "aarch64"), "arm64": ("arm64", "aarch64")}.get(arch, (arch,)); data = json.load(urllib.request.urlopen("https://api.github.com/repos/ssut/payload-dumper-go/releases/latest")); assets = data.get("assets", []); matches = [a for a in assets if "linux" in a.get("name", "").lower() and any(x in a.get("name", "").lower() for x in aliases) and a.get("name", "").lower().endswith((".tar.gz", ".tgz"))]; url = matches[0]["browser_download_url"] if matches else ""; assert url, "payload-dumper-go linux release asset not found"; urllib.request.urlretrieve(url, "/tmp/payload-dumper-go.tar.gz")' \
    && mkdir -p /tmp/payload-dumper-go /app/tools/helper \
    && tar -xzf /tmp/payload-dumper-go.tar.gz -C /tmp/payload-dumper-go \
    && install -m 0755 "$(find /tmp/payload-dumper-go -type f -name payload-dumper-go | head -n 1)" /app/tools/helper/payload-dumper-go \
    && chmod +x /app/tools/helper/linux/* 2>/dev/null || true \
    && rm -rf /tmp/payload-dumper-go /tmp/payload-dumper-go.tar.gz

ENTRYPOINT ["python3", "-m", "factory.deadzone"]
