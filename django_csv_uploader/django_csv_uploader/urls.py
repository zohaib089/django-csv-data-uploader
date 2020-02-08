from django.contrib import admin
from django.urls import path
from csvuploader.views import user_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', user_upload, "user_upload"),
]
