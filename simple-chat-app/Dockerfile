FROM jenkins/jenkins:lts
RUN useradd -m -s /bin/bash jenkins
USER jenkins

FROM node:14-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN apk add --no-cache curl  # Install curl
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000 || exit 1
