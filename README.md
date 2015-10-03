# bouraka
bouraka is back.

## Prerequisites
- Docker engine https://docs.docker.com/installation/
- Docker-compose http://docs.docker.com/compose/install/

## Fresh install
Download latest release from GitHub

Edit the docker-compose.yml
- Change the postgres username, password and db name
- Change the port you would like to expose bouraka on

Edit bouraka-django/bouraka/settings.py
- Change the db credentials according to what you put in docker-compose.yml

Edit the init-django
- Change the admin credentials

Start everything with
```
$  sudo docker-compose up -d
```

##How to back up
On the machine you want to keep the backups on, run the script backup-bouraka.sh available in this repo

## Recover from backup
Retrieve the backup and run
```
$ sudo docker-compose up -d
```
