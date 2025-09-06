from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=50, default="iniciante")

    def __str__(self):
        return self.title

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="questions", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correta' if self.is_correct else 'Errada'})"