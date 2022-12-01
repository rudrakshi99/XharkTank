from rest_framework import serializers, status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from entrepreneur.serializers import EntrepreneurSerializer
from entrepreneur.models import Entrepreneur
from investor.models import Investor


class EntrepreneurListCreateAPIView(ListCreateAPIView):
    serializer_class = EntrepreneurSerializer

    def post(self, request, *args, **kwargs):
        if request.data is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # check if all required fields are present
        if not all(
            field in request.data
            for field in [
                "entrepreneur",
                "pitchTitle",
                "pitchIdea",
                "askAmount",
                "equity",
            ]
        ) or any(value == None for value in request.data.values()):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if not 0 <= request.data["equity"] <= 100:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {"id": serializer.data["id"]}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Entrepreneur.objects.all()


class EntrepreneurRetrieveAPIView(RetrieveAPIView):
    serializer_class = EntrepreneurSerializer
    lookup_field = "id"

    def retrieve(self, request, *args, **kwargs):
        try:
            entrepreneur = Entrepreneur.objects.get(id=kwargs["id"])
        except Entrepreneur.DoesNotExist:
            return Response(
                {"error": "Entrepreneur does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(entrepreneur)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            # check if all required fields are present
            if not all(
                fields in request.data
                for fields in [
                    "investor",
                    "comment",
                    "amount",
                    "equity",
                ]
            ) or any(value == None for value in request.data.values()):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if not 0 <= request.data["equity"] <= 100:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            entrepreneur = Entrepreneur.objects.get(id=kwargs["id"])
        except Entrepreneur.DoesNotExist:
            return Response(
                {"error": "Entrepreneur does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        try:
            investor = Investor.objects.create(**request.data)
            serializer = self.serializer_class.update(
                self=EntrepreneurSerializer,
                instance=entrepreneur,
                validated_data=investor,
            )
            return Response({"id": str(investor.id)}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"error": "Error in updating investor"},
                status=status.HTTP_404_NOT_FOUND,
            )
