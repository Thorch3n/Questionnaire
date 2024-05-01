from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    TEXT = 'text'
    SINGLE_CHOICE = 'single_choice'
    MULTIPLE_CHOICE = 'multiple_choice'

    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (SINGLE_CHOICE, 'Single Choice'),
        (MULTIPLE_CHOICE, 'Multiple Choice'),
    ]

    text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user_id = models.IntegerField()

    def __str__(self):
        return self.text