from django.urls import path, include
from .views import EntrepreneurListCreateAPIView, EntrepreneurRetrieveAPIView

app_name = "entrepreneur"

urlpatterns = [
    path("pitches", EntrepreneurListCreateAPIView.as_view(), name="pitches"),
    path(
        "pitches/<int:id>",
        EntrepreneurRetrieveAPIView.as_view(),
        name="pitches",
    ),
    path(
        "pitches/<int:id>/makeOffer",
        EntrepreneurRetrieveAPIView.as_view(),
    ),
]
