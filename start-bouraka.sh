#!/bin/bash

#Django admin
username="admin"
password="admin"
email="admin@insa-lyon.fr"

#DB creds
db_engine=django.db.backends.postgresql_psycopg2
db_name=postgres
db_user=postgres
db_pass=postgres
db_host=db
db_port=5432

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
### DO NOT MODIFY ANYTHING BELLOW THIS POINT ###
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#

#To put in init-django-after-DB-ready.sh
echo "host=$db_host
port=$db_port
username=$username
password=$password
email=$email" | cat - init-django-after-DB-ready.sh > temp && mv temp init-django-after-DB-ready.sh

#To put in db-creds.txt
if [[ -f ./bouraka-django/db-creds.txt ]]
then
    rm ./bouraka-django/db-creds.txt
fi
touch ./bouraka-django/db-creds.txt
echo "{
    'default': {
      'ENGINE': '$db_engine',
      'NAME': '$db_name',
      'USER': '$db_user',
      'PASSWORD': '$db_pass',
      'HOST': '$db_host',
      'PORT': $db_port,
    }
}" | cat - ./bouraka-django/db-creds.txt > temp && mv temp ./bouraka-django/db-creds.txt

#To export for compose
export POSTGRES_PASSWORD=$db_pass
export POSTGRES_DB=$db_name
export POSTGRES_USER=$db_user

#Run docker-compose
docker-compose up
