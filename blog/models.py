from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def pub_date_pretty(self):
        return self.publication_date.strftime('%b %d %Y')

    def summary(self):
        return self.body[:50]

    def __str__(self):
        return self.title
