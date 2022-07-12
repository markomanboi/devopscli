FROM alpine:latest

#Initialize alpine
RUN apk update
RUN apk upgrade

# Install cURL
RUN apk add curl

# Install Maven
RUN apk add maven

# Install Jacoco and SonarQube
RUN mvn dependency:get org.jacoco:jacoco-maven-plugin:${JACOCO_VERSION}
RUN mvn dependency:get org.sonarsource.scanner.maven:sonar-maven-plugin:${SONAR_VERSION}

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    unzip awscliv2.zip \
    ./aws/install

# Setup DevOpsCLI
ADD ${BUILD_DESTINATION}/dist/devopscli .
RUN chmod +x ./devopscli
RUN mv ./devopscli /usr/local/bin/
ADD devopscli_app.json /usr/local/bin/