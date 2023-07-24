from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()

    # automatically set the time the moemnt the object is created
    created_on = models.DateTimeField(auto_now_add=True)

    # many-to-one relationship: a post can have many comments, but a comment can
    # only belong to one post
    # create a relationship with Post model
    # if a post is deleted, delete all the comments associated with the post
    posts = models.ForeignKey('Post', on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    # automatically set the time the moemnt the object is created
    created_on = models.DateTimeField(auto_now_add=True)

    # latest modification time for the object
    last_modified = models.DateTimeField(auto_now=True)

    # many-to-many relationship: a category can have many posts and a post can
    # have many categories
    # 'related_name' allows us to get a list of posts with a particular category
    categories = models.ManyToManyField('Category', related_name='posts')

