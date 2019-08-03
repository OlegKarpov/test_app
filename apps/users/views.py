from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.utils.decorators import method_decorator

from apps.users.forms import CustomSignInForm
from apps.users.models import User


class ProfileObjectMixin(SingleObjectMixin):
    """
    Provides views with the current user's profile.
    """
    model = User

    def get_object(self):
        """Return's the current users profile."""
        try:
            return self.request.user
        except User.DoesNotExist:
            raise NotImplemented(
                "What if the user doesn't have an associated profile?")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """Ensures that only authenticated users can access the view."""
        klass = ProfileObjectMixin
        return super().dispatch(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, DetailView):
    form_class = CustomSignInForm
    template_name = 'user_detail.html'
    slug_field = "first_name"
    model = User
    """
    A view that displays a form for editing a user's profile.

    Uses a form dynamically created for the `Profile` model and
    the default model's update template.
    """
    pass  # That's All Folks!