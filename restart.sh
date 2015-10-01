#!/bin/bash

docker rm -f bouraka_bourakaweb_1 bouraka_bourakadb_1

rm -rf bouraka-static/*
rm -rf bouraka-media/*
rm -rf bouraka-db/*

docker-compose up
