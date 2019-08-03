from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('user_page', args=[request.user.first_name]))
