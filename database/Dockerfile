FROM mysql

COPY ./schema_social_media.sql /tmp

CMD [ "mysqld", "--init-file=/tmp/schema_social_media.sql" ]