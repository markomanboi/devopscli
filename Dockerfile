FROM alpine:latest

#Initialize alpine
RUN apk update
RUN apk upgrade

# Install cURL
RUN apk add curl

# Install Python 
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

# Install pyinstaller and binutils
RUN apk add binutils
RUN pip3 install --no-cache pyinstaller

# Install AWS CLI
RUN pip3 install --no-cache-dir awscli

# Setup DevOpsCLI
ADD main.py .
RUN  pyinstaller main.py \
    --distpath /usr/local/bin \
    -n devopscli \
    --onefile

# Change permission of /usr/local/bin
RUN chmod -R u=rwX,go=rX /usr/local/bin