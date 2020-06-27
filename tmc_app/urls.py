# Django
from django.urls import path

# View
from tmc_app import views

urlpatterns = [
    path(
        route='',
        view=views.init_page,
        name='init'
    ),
]
