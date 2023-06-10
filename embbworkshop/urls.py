from django.contrib import admin
from django.urls import path

from core.views import index, schedule, lecture

urlpatterns = [
    path('', index, name='index'),
    path('schedule/', schedule, name='schedule'),
    path('lecture/', lecture, name='lecture'),
    path("admin/", admin.site.urls),
]
