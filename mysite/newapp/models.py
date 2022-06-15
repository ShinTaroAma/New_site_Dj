from django.db import models
from django.utils import timezone

CHOICES = (
    (0, ("Not Avaliable")),
    (1, ("Avaliable"))
)


# 1 task


class Author(models.Model):
    name = models.CharField(max_length=120)
    second_name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='aut')

    def __str__(self):
        return self.title


# 2 task


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class NewStoreBooks(models.Model):
    title = models.CharField(max_length=120)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='per')
    Author = models.ManyToManyField(Author)
    date_take = models.DateField()
    avaliable = models.IntegerField(choices=CHOICES, default=1)

    def __str__(self):
        return self.title


# 3 task


class PersonComentator(models.Model):
    name = models.CharField(max_length=128)


class ArticleAuthor(models.Model):
    nikname = models.CharField(max_length=120, blank=True, null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):
    article_Author = models.ForeignKey(ArticleAuthor, on_delete=models.CASCADE, null=True, related_name='articles')
    text = models.TextField(max_length=10000, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('newapp.Comment', null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name='comments')
    personComentator = models.ForeignKey(PersonComentator, on_delete=models.DO_NOTHING)


class Like(models.Model):
    personComentator = models.ForeignKey(PersonComentator, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)

