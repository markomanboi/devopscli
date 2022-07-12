FROM alpine:latest

# Install cURL
RUN apk add curl

# Install Maven
RUN apk add maven

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    unzip awscliv2.zip \
    ./aws/install

# Setup DevOpsCLI
ADD ${BUILD_DESTINATION}/dist/devopscli .
RUN chmod +x ./devopscli
RUN mv ./devopscli /usr/local/bin/
ADD devopscli_app.json /usr/local/bin/