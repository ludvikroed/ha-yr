# Base image med Python 3.11
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base-python:latest
FROM $BUILD_FROM

# Sett språk
ENV LANG C.UTF-8

# Kopier filer til container
COPY run.sh /
COPY server.py /data/

# Gi run.sh kjørbar
RUN chmod a+x /run.sh

# Start run.sh
CMD [ "/run.sh" ]
