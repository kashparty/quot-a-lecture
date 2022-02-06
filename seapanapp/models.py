import re
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.TextField(unique=True)

    def __str__(self) -> str:
        return self.name


class Lecturer(models.Model):
    name = models.TextField(unique=True)

    def __str__(self) -> str:
        return self.name


class Recording(models.Model):
    panopto_id = models.TextField(unique=True)
    name = models.TextField()

    # TODO: Their should be forein keys
    category = models.ForeignKey(
        Category, on_delete=models.RESTRICT, related_name="recordings"
    )
    lecturer = models.ForeignKey(
        Lecturer, on_delete=models.RESTRICT, related_name="recordings"
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.panopto_id[:8]}"

    def to_url(self):
        return f"https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id={self.panopto_id}"


class QuestionAnswer(models.Model):
    preamble = models.TextField()
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.TimeField()
    encoding = models.BinaryField()
    recording = models.ForeignKey(
        Recording, on_delete=models.RESTRICT, related_name="questions"
    )
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question

    def to_url(self):
        t = (
            self.timestamp.hour * 60 * 60
            + self.timestamp.minute * 60
            + self.timestamp.second
        )
        pid = self.recording.panopto_id
        return f"https://imperial.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id={pid}&start={t}"
