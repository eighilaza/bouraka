#!/bin/bash
host=db
port=5432
username=admin
password=admin
email=admin@insa-lyon.fr
service="database"

max=100000
counter=1

MANAGE_PATH=/bouraka/bouraka-django/manage.py

while [ $counter -lt $max ]
do
  python -c "import socket;s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.connect(('$host', $port))" \
    >/dev/null 2>/dev/null && break || \
    echo "Waiting that $service on ${host}:${port} is started (sleeping for 5)"
  sleep 5
  if [[ ${counter} == ${max} ]];then
    echo "Could not connect to ${service} after some time"
    echo "Investigate locally the logs with docker-compose logs"
    exit 1
  fi
  ((++counter))
done

python $MANAGE_PATH makemigrations
python $MANAGE_PATH migrate
python $MANAGE_PATH collectstatic --noinput
#Create superuser
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$username','$email','$password')" | python $MANAGE_PATH shell

#Change owner of media and static folders
chown -R www-data:www-data /bouraka/bouraka-media
chown -R www-data:www-data /bouraka/bouraka-static
