#!/bin/bash

# This tells bash that it should exit the script if any statement returns a non-true return value.
# http://web.archive.org/web/20110314180918/http://www.davidpashley.com/articles/writing-robust-shell-scripts.html
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE "tenant" ENCODING 'UTF8' TEMPLATE template0;
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "tenant" <<-EOSQL
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        email VARCHAR(100),
        salt VARCHAR(255),
        bio VARCHAR(255),
        hashed_password VARCHAR(255),
        image VARCHAR(500),
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
        INSERT INTO users (
        username, 
        email, 
        salt, 
        bio,
        hashed_password, 
        image, 
        created_at, 
        updated_at
    ) VALUES (
        'test',                 -- username
        'test@example.com',     -- email
        'random_salt_value',        -- salt
        'bio',                      -- bio
        'hashed_password_value',    -- hashed_password (make sure it's hashed)
        'http://example.com/image', -- image URL or path
        CURRENT_TIMESTAMP,          -- created_at (current timestamp)
        CURRENT_TIMESTAMP           -- updated_at (current timestamp)
    );
EOSQL