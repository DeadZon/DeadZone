FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl wget sudo zip unzip p7zip-full \
    zstd brotli lz4 file ca-certificates erofs-utils \
    openjdk-17-jre python3.12 python3.12-venv python3-pip \
    && ln -s /usr/bin/python3.12 /usr/bin/python

RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
    && apt-get update && apt-get install gh -y

COPY build_script_snap.sh /build_script_snap.sh
RUN chmod +x /build_script_snap.sh

COPY build_script_mtk.sh /build_script_mtk.sh
RUN chmod +x /build_script_mtk.sh

ENTRYPOINT ["/build_script_snap.sh"]
