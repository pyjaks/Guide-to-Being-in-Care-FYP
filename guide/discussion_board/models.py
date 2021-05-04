from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = models.TextField()
    # profile_picture?

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.fullname
        #or username


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="description")

    class Meta:
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
    # TODO: Error handling for when slug isn't unique

    def get_absolute_url(self):
        return reverse("posts", kwargs={
            "slug": self.slug
        })

    def __str__(self):
        return self.title

    @property
    def post_count(self):
        return Post.objects.filter(categories=self).count()

    @property
    def last_post(self):
        return Post.objects.filter(categories=self).latest("datePosted")


class Post(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    datePosted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={
                                "slug": self.slug
                                })

    def get_comments(self):
        return Comment.objects.filter(original_post=self)

    @property
    def comments_count(self):
        return Comment.objects.filter(original_post=self).count()

    @property
    def last_comment(self):
        return Comment.objects.filter(original_post=self).latest("datePosted")

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)
    original_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def get_replies(self):
        return Reply.objects.filter(reply_to=self)

    def __str__(self):
        return self.content[:100]


class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:100]

    class Meta:
        verbose_name_plural = "replies"

