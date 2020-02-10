from django.db import models
from django.contrib.auth.models import User

from slugify import slugify_ru


class Publication(models.Model):
    MODERATION_STATUS_APPROVED = 0
    MODERATION_STATUS_DRAFT = 1
    MODERATION_STATUS_PRE_MODERATION = 2
    MODERATION_STATUS_DECLINED = 3
    MODERATION_STATUS_CHOICE = (
        (MODERATION_STATUS_APPROVED, 'approved'),
        (MODERATION_STATUS_DRAFT, 'draft'),
        (MODERATION_STATUS_PRE_MODERATION, 'pre-moderation'),
        (MODERATION_STATUS_DECLINED, 'declined'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    moderation_status = models.IntegerField(choices=MODERATION_STATUS_CHOICE, default=1)
    date_create = models.DateTimeField(auto_now_add=True)
    date_pub = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, editable=True, blank=True)

    class Meta:
        ordering = ['-date_pub']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug and not self.moderation_status:
            self.slug = slugify_ru(self.title, to_lower=True, max_length=100)
        super(Publication, self).save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
