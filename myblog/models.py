from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32, default='')
    pub_date = models.DateTimeField('发布时间')
    content = models.TextField(null=True)
    favorite = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=32)
    create_time = models.DateTimeField('评论时间',auto_now_add=True)
    comment_text = models.CharField(max_length=200)
    favorite = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text[:10]


# Create your models here.
