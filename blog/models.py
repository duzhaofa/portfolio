from django.db import models


class Blog(models.Model):
    title = models.CharField(default='文章标题', max_length=50)
    date = models.DateField()
    image = models.ImageField(default='defualt.png', upload_to='images/')
    text = models.TextField(default='正文')

    def __str__(self):
        return self.title
