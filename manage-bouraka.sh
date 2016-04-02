#!/bin/bash

function putCredsInInitDjangoScript {
  echo "#!/bin/bash
  host=$db_host
  port=$db_port
  username=$username
  password=$password
  email=$email" | cat - init-django-after-DB-ready.sh > temp && mv temp init-django-after-DB-ready.sh
}

function putCredsInDBCredsFile {
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
}

function exportCredsForDockerCompose {
  export POSTGRES_PASSWORD=$db_pass
  export POSTGRES_DB=$db_name
  export POSTGRES_USER=$db_user
  export WEB_PORT=$web_port
}

function runDockerCompose {
  docker-compose up
}

function start-fresh {
  putCredsInInitDjangoScript
  putCredsInDBCredsFile
  exportCredsForDockerCompose
  runDockerCompose
}

function start-again {
  exportCredsForDockerCompose
  runDockerCompose
}

function stop {
  #TODO
}

function restart {
  #TODO - probably gonna call stop then start-again
}

function update {

}

if [[ $# -ne 1 ]]
then
  echo "usage: ./$1 {start-fresh|start-again|stop|update}"
  exit
fi

source ./all-vars.txt

case $1 in
  start-fresh)
    echo $1 start-fresh
    ;;
  start-again)
    echo $1 start-again
    ;;
  stop)
    echo $1 stop
    ;;
  update)
    echo $1 update
    ;;
  *)
  echo "usage: ./$1 {start-fresh|start-again|stop|update}"
  exit
  ;;
esac
