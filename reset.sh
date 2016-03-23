#!/bin/bash

docker rm -f bourakadev_bourakaweb_1 bourakadev_bourakadb_1

rm -rf bouraka-static/*
rm -rf bouraka-media/*
rm -rf bouraka-db/*
rm -rf bouraka-django/*/migrations
