FROM nginx:latest

RUN apt-get update && \
    apt-get install -y procps && \
    apt-get install -y apache2-utils && \
    apt-get install -y openssl

RUN mkdir -p /etc/pwd

RUN htpasswd -bc /etc/pwd/passwords root root

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/nginx.key \
    -out /etc/nginx/nginx.cert \
    -subj "/C=US/ST=State/L=City/O=Organization/OU=Unit/CN=techbeast.local"

COPY conf.d/ /etc/nginx/conf.d/
COPY html/ /var/www/techbeast.local/

EXPOSE 443
