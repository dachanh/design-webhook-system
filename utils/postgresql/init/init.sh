#!/bin/bash
set -e

psql -v ON_ERROR_STOP=0 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE "${ENV}-webhook" ENCODING 'UTF8' TEMPLATE template0;
EOSQL