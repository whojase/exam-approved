from django.db import models

class MainLearn(models.Model):
    title = models.CharField(max_length = 32)
    description = models.TextField()

    def __str__(self):
        return self.title

class QuestionsFromExams(models.Model):
    title = models.CharField(max_length = 32)
    answer = models.TextField()

    def __str__(self):
        return self.title

class VideoGuides(models.Model):
    title = models.CharField(max_length = 32)
    url_on_video = models.URLField(max_length = 300)

    def __str__(self):
        return self.title