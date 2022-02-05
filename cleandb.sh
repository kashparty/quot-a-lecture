#!/bin/bash
set -eoxu pipefail

rm -f db.sqlite
rm -rf seapanapp/migrations
python manage.py makemigrations seapanapp
python manage.py migrate