#!/bin/bash

docker rm -f bourakadev_bourakadevweb_1 bourakadev_bourakadevdb_1

rm -rf bouraka-static/*
rm -rf bouraka-media/*
rm -rf bouraka-db/*
rm -rf bouraka-django/*/migrations

docker-compose up
