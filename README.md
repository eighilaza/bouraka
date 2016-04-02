# bouraka
bouraka is back.

## Prerequisites
- Docker engine https://docs.docker.com/installation/
- Docker-compose http://docs.docker.com/compose/install/

## Fresh install
Download and unzip the latest release from: https://github.com/eighilaza/bouraka/releases

Edit bouraka/all-vars.txt:
- Change the postgres username, password and db name
- Change the port you would like to expose Bouraka on
- Change the django admin credentials

You can then start everything with:
```
$ ./manage-bouraka.sh fresh-start
```

##How to back up
On the machine where you want to keep the backups, run the script backup-bouraka.sh that is available in this repository

## Recover from backup
Retrieve the backup and run
```
$ ./manage-bouraka.sh start-again
```

##How to update
To update Bouraka run
```
$ ./manage-bouraka.sh update
```
