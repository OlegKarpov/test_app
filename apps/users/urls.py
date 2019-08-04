from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<slug>[a-zA-Z0-9]+)$', views.ProfileDetailView.as_view(), name='user_page'),
]
