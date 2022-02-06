from datetime import datetime, time, date
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from os import environ, listdir
import django
from sentence_transformers import SentenceTransformer

environ.setdefault("DJANGO_SETTINGS_MODULE", "seapan.settings")
django.setup()
from seapanapp.models import Category, Lecturer, QuestionAnswer, Recording

MIN_QUESTION_LENGTH = 3
nltk.download("punkt")

model = SentenceTransformer("distilbert-base-nli-mean-tokens")


def parse_timestamp(timestamp_str):
    time_parts = timestamp_str.split(":")
    if len(time_parts) == 2:
        return time(0, int(time_parts[0]), int(time_parts[1]))
    elif len(time_parts) == 3:
        return time(int(time_parts[0]), int(time_parts[1]), int(time_parts[2]))
    else:
        raise RuntimeError("Timestamp must have 2 or 3 parts")


def load_phrases(filename):
    phrases = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        metadata = lines[:5]
        lecture_id = metadata[0].split(": ")[1]
        lecture_title = metadata[1].split(": ", 1)[1]
        lecture_category = metadata[2].split(": ", 1)[1]
        lecture_lecturer = metadata[3].split(": ", 1)[1]
        d, m, y = metadata[4].split(": ", 1)[1].split("/")
        lecture_date = date.fromisoformat(f"{y}-{m}-{d}")

        cat, _ = Category.objects.get_or_create(name=lecture_category)
        lec, _ = Lecturer.objects.get_or_create(name=lecture_lecturer)

        recording = Recording(
            panopto_id=lecture_id,
            name=lecture_title,
            category=cat,
            lecturer=lec,
            date=lecture_date,
        )
        recording.save()

        lecture_category = metadata[2].split(": ", 1)[1]
        lecturer = metadata[3].split(": ")[1]
        lecture_date = datetime.strptime(metadata[4].split(": ")[1], "%d/%m/%Y")

        timestamped_phrases = []
        for i in range(5, len(lines), 2):
            timestamp = parse_timestamp(lines[i + 1])
            phrase_texts = sent_tokenize(lines[i])
            timestamped_phrases += [(timestamp, text) for text in phrase_texts]

        for i in range(len(timestamped_phrases)):
            timestamp = timestamped_phrases[i][0]
            preamble = ""
            question = ""
            answer = ""
            if i - 1 >= 0:
                preamble = timestamped_phrases[i - 1][1]
            question = timestamped_phrases[i][1]
            if i + 1 < len(timestamped_phrases):
                answer = timestamped_phrases[i + 1][1]
            phrases.append(
                Phrase(
                    timestamp,
                    preamble,
                    question,
                    answer,
                    recording,
                    lecture_category,
                    lecturer,
                    lecture_date,
                )
            )

    return phrases


class Phrase:
    def __init__(
        self,
        timestamp,
        preamble,
        question,
        answer,
        recording,
        lecture_category,
        lecturer,
        lecture_date,
    ):
        self.timestamp = timestamp
        self.preamble = preamble
        self.question = question
        self.answer = answer
        self.recording = recording
        self.lecture_category = lecture_category
        self.lecturer = lecturer
        self.lecture_date = lecture_date

    def __str__(self):
        return f"{self.recording.panopto_id}@{self.timestamp}: {self.question}"

    def is_question(self):
        words = word_tokenize(self.question)
        return self.question.endswith("?") and len(words) >= MIN_QUESTION_LENGTH

    def save(self):
        question_answer = QuestionAnswer(
            preamble=self.preamble,
            question=self.question,
            answer=self.answer,
            timestamp=self.timestamp,
            encoding=model.encode(self.question).tobytes(),
            recording=self.recording,
        )
        question_answer.save()


files_dir = "panopto-api-stuff"
filenames = [f for f in listdir(files_dir) if f.endswith(".txt")]

for filename in filenames:
    print(filename)
    phrases = load_phrases(f"{files_dir}/{filename}")
    questions = [phrase for phrase in phrases if phrase.is_question()]

    for question in questions:
        question.save()
