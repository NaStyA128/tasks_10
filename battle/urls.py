from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from .views import (
    index,
    form_django
)

urlpatterns = [
    url(r'^$', index),
    url(r'^form_django/$', form_django),
]
