FROM nginx:1.27-alpine

RUN apk update && apk upgrade --no-cache && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /var/cache/nginx /var/run /tmp && \
    chown -R nginx:nginx /var/cache/nginx /var/run /tmp /usr/share/nginx/html

COPY index.html /usr/share/nginx/html/index.html

USER nginx
EXPOSE 80