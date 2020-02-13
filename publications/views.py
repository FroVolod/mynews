from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from publications.models import Publication, Comment
from publications.forms import CommentForm, PublicationCreateForm
from publications.tasks import send_email_to_author


class PublicationListView(ListView):
    model = Publication
    template_name = 'publications/publications_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(
            moderation_status=Publication.MODERATION_STATUS_APPROVED
            )
        return queryset
    

class PublicationDetailView(DetailView, CreateView):
    model = Publication
    template_name = 'publications/publications_detail.html'
    form_class = CommentForm

    def dispatch(self, *args, **kwargs):
        object = self.get_object()
        return super(PublicationDetailView, self) \
            .dispatch(*args, **kwargs)

    def get_object(self):
        return get_object_or_404(Publication,
                                 slug=self.kwargs.get('page_alias'))

    def get_context_data(self, *args, **kwargs):
        context = super(PublicationDetailView, self).get_context_data(*args, **kwargs)
        publication = Publication.objects.get(slug=self.kwargs.get('page_alias'))
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(publication=publication)
        context['user'] = self.request.user
        return context

    def form_valid(self, form):
        object = self.get_object()
        form.instance.user = self.request.user
        form.instance.publication = object
        form.save()
        send_email_to_author.delay(object.author.email, object.title)
        return redirect('publication_details', object.slug)

class PublicationAdd(CreateView):
    model = Publication
    form_class = PublicationCreateForm
    template_name = 'publications/publication_add.html'

    def form_valid(self, form):
        if self.request.user.has_perm('publications.change_publication'):
            form.instance.moderation_status = Publication.MODERATION_STATUS_APPROVED
        form.instance.author = self.request.user
        form.save()
        return redirect('publication_list')
    