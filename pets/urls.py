from django.urls import path
from .views import PetsView, PetsDetailsView
urlpatterns =[
    path("pets/", PetsView.as_view()),
    path("pets/<pet_id>/", PetsDetailsView.as_view() )
]