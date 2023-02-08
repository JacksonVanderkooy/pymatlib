FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractable

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install -y \
    python-is-python3 \
    pip

RUN pip install \
    control \
    numpy \
    scipy \
    matplotlib

RUN apt-get install -y \
    python3-tk
