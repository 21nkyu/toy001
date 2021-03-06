from django.db import models

# Create your models here.
# Docs(Fields types) -> https://docs.djangoproject.com/en/3.0/ref/models/fields/#field-types


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
    # id값 대신 제목을 표시할 수 있다.


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()



