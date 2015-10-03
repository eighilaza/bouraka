#!/bin/bash

#Put this file on the machine where you would like to keep the backup
#And run it periodically using crontab

username="username"
host="hostname"
path_to_bouraka="/path/to/bouraka"
path_to_local_backup="/path/to/local/backup"

rsync -azv --progress $username@$host:$path_to_bouraka/bouraka-db $path_to_local_backup
rsync -azv --progress $username@$host:$path_to_bouraka/bouraka-static $path_to_local_backup
rsync -azv --progress $username@$host:$path_to_bouraka/bouraka-media $path_to_local_backup
rsync -azv --progress $username@$host:$path_to_bouraka/bouraka-django $path_to_local_backup
