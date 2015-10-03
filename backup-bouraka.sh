#!/bin/bash

username="username"
host="hostname"
path_to_bouraka="/path/to/bouraka"
path_to_local_backup="/path/to/local/backup"

rsync -azv --progress $username@$host:$path_to_bouraka/bouraka-db $path_to_local_backup
rsync -azv --progress $username@$host:$path_to_bouraka/bouraka-static $path_to_local_backup
rsync -azv --progress $username@$host:$path_to_bouraka/bouraka-media $path_to_local_backup
