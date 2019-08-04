from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.detail import DetailView

from apps.users.forms import CustomSignInForm
from apps.users.models import User


class ProfileDetailView(LoginRequiredMixin, DetailView):
    form_class = CustomSignInForm
    template_name = 'user_detail.html'
    slug_field = "first_name"
    model = User

    def get_success_url(self):
        return reverse('user_page', args=[self.request.user.username])
