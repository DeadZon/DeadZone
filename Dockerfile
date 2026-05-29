FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV FLY_NO_PROMPT=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl wget unzip zip xz-utils zstd brotli file \
    python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt || true

COPY . /app

ENTRYPOINT ["python", "-m", "factory.pipeline.orchestrator"]
