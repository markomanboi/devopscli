FROM python:3.10-alpine

# Install Maven
RUN apk add maven

# Install AWSCLI 
RUN pip3 install --no-cache -dir awscli

# Setup DevOpsCLI
ADD ${BUILD_DESTINATION}/dist/devopscli .
RUN chmod +x ./devopscli
RUN mv ./devopscli /usr/local/bin/
ADD devopscli_app.json /usr/local/bin/