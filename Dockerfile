FROM n8nio/n8n:1.50.1

USER root

# Install Python and automation libraries + Dashboard dependencies
RUN apk add --update python3 py3-pip && \
    ln -sf python3 /usr/bin/python && \
    pip install pandas openpyxl fastapi uvicorn jinja2 --break-system-packages

USER node
