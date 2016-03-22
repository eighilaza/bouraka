# bouraka
bouraka is back.

## Prerequisites
- Docker engine https://docs.docker.com/installation/
- Docker-compose http://docs.docker.com/compose/install/

## Fresh install
Download and unzip the latest release https://github.com/eighilaza/bouraka/releases

Edit bouraka/start-bouraka.sh:
- Change the postgres username, password and db name
- Change the port you would like to expose bouraka on
- Change the django admin credentials

Start everything with
```
$ ./start-bouraka.sh 
```

##How to back up
On the machine you want to keep the backups on, run the script backup-bouraka.sh available in this repo

## Recover from backup
Retrieve the backup and run
```
$ ./start-bouraka.sh
```

##How to update
- Download latest release
- Unzip it
- In the resulting folder copy the directories bouraka-{db,media,static} and the file named start-bouraka.sh, from the previous deployment.
- Run ./start-bouraka.sh
