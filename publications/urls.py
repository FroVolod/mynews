from django.urls import path, re_path

from publications.views import PublicationListView,\
                               PublicationDetailView,\
                               PublicationAdd


urlpatterns = [
    path('', PublicationListView.as_view(),
        name='publication_list'),
    path('add/', PublicationAdd.as_view(),
        name='publication_add'),
    re_path(r'^(?P<page_alias>[-a-z\d]+)/$', PublicationDetailView.as_view(),
        name='publication_details'),
]
