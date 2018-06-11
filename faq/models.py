from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question'
