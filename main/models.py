from django.db import models


# Create your models here.
# model to store language and technology
class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    added_date = models.DateTimeField(auto_now=True)
    logo = models.ImageField(upload_to="tech/")
    slug = models.CharField(max_length=100)
    live = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_subtopics(self):
        return self.subtopics_set.all()

        # model to store sub topics or table of content


class SubTopics(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_topics(self):
        return self.topic_set.all()


class Topic(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    author = models.CharField(max_length=500)
    slug = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now=True)
    sub_topic = models.ForeignKey(SubTopics, on_delete=models.CASCADE)
    keyword = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title
