FROM nginx:1.27-alpine
RUN apk update && apk upgrade --no-cache && \
    rm -rf /var/cache/apk/*
COPY index.html /usr/share/nginx/html/index.html
RUN chown -R nginx:nginx /usr/share/nginx/html
USER nginx
EXPOSE 8080