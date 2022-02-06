#!/bin/bash
set -eoxu pipefail

rm -f db.sqlite3
rm -rf seapanapp/migrations
python manage.py makemigrations seapanapp
python manage.py migrate