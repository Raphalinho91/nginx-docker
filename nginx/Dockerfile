FROM nginx:latest

RUN apt-get update && \
    apt-get install -y procps && \
    apt-get install --no-install-recommends -y apache2-utils

RUN mkdir -p /home/app/staticfiles && \
    mkdir -p /etc/pwd

RUN htpasswd -bc /etc/pwd/.htpasswd yourusername yourpassword

COPY conf.d/ /etc/nginx/conf.d/