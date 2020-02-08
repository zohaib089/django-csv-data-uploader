from django.contrib import admin
from django.urls import path
from csvuploader.views import user_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('csv_upload/', user_upload, name="user_upload"),
]
