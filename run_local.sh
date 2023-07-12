#!/bin/bash

## Run your postgres container locally if you want to test without touching the distant database
# docker run --name my-postgres-container -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=saif -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres:15
## Execute the db_init.sql queries to create the tables

flask run --host=0.0.0.0 --port=5001

