# Install Maven 3.6, Java 11, Java 8 and Python3
FROM rust:1-slim-buster

RUN apt-get --quiet --quiet update \
    && apt-get --quiet --quiet install -y bash python3 \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHON=python3

# Install our own CAs on the image.
# Assumes Linux Debian based image.
COPY CAs/* /usr/local/share/ca-certificates/
RUN update-ca-certificates
