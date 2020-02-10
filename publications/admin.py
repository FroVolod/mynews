from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from publications.models import Publication, Comment


class PublicationAdmin(SummernoteModelAdmin):
    model = Publication
    list_display = ['title', 'moderation_status', 'date_pub', 'author']
    list_filter = ['author', 'date_pub']
    search_fields = ['title', 'text']


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['date', 'user', 'publication', 'text']


admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comment, CommentAdmin)
