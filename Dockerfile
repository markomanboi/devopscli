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
    -n devopscli \
    --onefile
RUN chmod +x ./dist/devopscli
RUN mv ./dist/devopscli /usr/local/bin/
ADD devopscli_app.json /usr/local/bin/