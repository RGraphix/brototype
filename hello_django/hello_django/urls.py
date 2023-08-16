
from django.contrib import admin
from django.urls import path
from helo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.print_hello)

]
