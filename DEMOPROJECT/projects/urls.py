from django.urls import path

from .import views

urlpatterns = [
    # /projects/
    path('', views.index, name='home-page'),
    # /projects/721/
    path('<int:student_id>', views.details, name='details'),

]
