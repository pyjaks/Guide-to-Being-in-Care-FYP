from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from profanity.validators import validate_is_profane
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.username


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
        return Post.objects.filter(category=self).filter(approved=True).count()

    @property
    def last_post(self):
        return Post.objects.filter(category=self).filter(approved=True).latest("datePosted")


class Post(models.Model):
    title = models.CharField(max_length=400, validators=[validate_is_profane])
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(validators=[validate_is_profane])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
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
    content = models.TextField(validators=[validate_is_profane])
    datePosted = models.DateTimeField(auto_now_add=True)
    original_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def get_replies(self):
        return Reply.objects.filter(reply_to=self)

    def __str__(self):
        return self.content[:100]


class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(validators=[validate_is_profane])
    datePosted = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:100]

    class Meta:
        verbose_name_plural = "replies"


@receiver(post_save, sender=get_user_model())
def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)


