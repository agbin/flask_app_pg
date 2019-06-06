#!/bin/sh

dropdb phone_numbers
createdb phone_numbers
psql -1 phone_numbers < sql/schema.sql
psql -1 phone_numbers < sql/data.sql

