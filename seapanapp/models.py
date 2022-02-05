from django.db import models

# Create your models here.


class Recording(models.Model):
    panopto_id = models.TextField()

    def __str__(self):
        return self.panopto_id[:8]


class QuestionAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.TimeField()
    recording = models.ForeignKey(Recording, on_delete=models.RESTRICT)

    def __str__(self):
        return self.question

    def answer_start(self):
        return self.answer[:100]
