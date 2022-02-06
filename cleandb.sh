#!/bin/bash
set -eoxu pipefail

rm db.sqlite3 
rm -rf seapanapp/migrations/
./manage.py makemigrations seapanapp
./manage.py migrate
python extract_questions.py 