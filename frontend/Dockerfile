FROM nginx:1.27-alpine

RUN apk add --no-cache wget unzip

WORKDIR /tmp

RUN wget -O templatemo_615_amber_folio.zip https://templatemo.com/download/templatemo_615_amber_folio \
    && unzip templatemo_615_amber_folio.zip \
    && cp -r templatemo_615_amber_folio/* /usr/share/nginx/html/ \
    && rm -rf /tmp/*

RUN chown -R nginx:nginx /usr/share/nginx/html

USER nginx
EXPOSE 80