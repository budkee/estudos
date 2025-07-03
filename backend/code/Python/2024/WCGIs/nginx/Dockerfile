FROM nginx

COPY ./nginx.conf /etc/nginx/nginx.conf

COPY ./static /usr/share/nginx/html

EXPOSE 7979

CMD [ "-g", "daemon", "off" ]

