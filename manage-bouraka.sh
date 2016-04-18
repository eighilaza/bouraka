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

function DockerComposeUp {
  docker-compose up -d
}

function DockerComposeBuild {
  docker-compose build
}

function start-fresh {
  putCredsInInitDjangoScript
  putCredsInDBCredsFile
  exportCredsForDockerCompose
  DockerComposeUp
}

function start-again {
  exportCredsForDockerCompose
  DockerComposeUp
}

function stop {
  docker stop bouraka_db bouraka_web
  docker rm bouraka_db bouraka_web
}

function restart {
  stop
  start-again
}

function update {
  #TODO - figure out a clean way to take either a local or remote path (url) to the new release
  #TODO - figure out when it is best to stop the containers (before unzip, before build or before start-again)
  #TODO - test what happens if manage-bouraka.sh is modified in the new release
  read -p "Please input the url or path to the release you want to deploy (.zip): " new_release
  echo "new_release available at: "$new_release
  wget $update_url -O newVersion.zip
  #cp $new_release ./newVersion.zip
  mv all-vars.txt all-vars.txt.save
  stop
  unzip newVersion.zip
  rm all-vars.txt && mv all-vars.txt.save all-vars.txt
  #DockerComposeBuild - BAD IDEA, SHOULD PULL LATEST IMAGE
  rm newVersion.zip
  start-again
}

if [[ $# -ne 1 ]]
then
  echo "usage: ./$1 {start-fresh|stop|start-again|restart|update}"
  exit
fi

source ./all-vars.txt

case $1 in
  start-fresh)
    echo $1
    start-fresh
    ;;
  start-again)
    echo $1
    start-again
    ;;
  stop)
    echo $1
    stop
    ;;
  restart)
    echo $1
    restart
    ;;
  update)
    echo $1
    update
    ;;
  *)
  echo "usage: ./$1 {start-fresh|start-again|stop|update}"
  exit
  ;;
esac
