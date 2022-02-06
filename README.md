## Setup

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt 
For the "Lecture Transcript Extractor" see the separate readme
```

## Formatting

We use black

```
black seapan seapanapp
```

## Updateing DB

```
rm db.sqlite3 
rm -r seapanapp/migrations/
./manage.py makemigrations seapanapp
./manage.py migrate
python extract_questions.py
```

Generating files


```
python save_counts.py
python extract_questions.py
```
