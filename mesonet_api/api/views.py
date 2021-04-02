from classifiers.models import MLModel
from classifiers.serializers import MLModelSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework import generics, permissions, views
from rest_framework.response import Response


class ListModelsView(generics.ListAPIView):
    queryset = MLModel.objects.all()
    serializer_class = MLModelSerializer
    permission_classes = [permissions.AllowAny]


class PredictionResultsView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        selected_model = get_object_or_404(MLModel, pk=kwargs['model_pk'])

        num_imgs = kwargs['num_imgs']
        conv_idx = kwargs['conv_idx']

        response = selected_model.create_prediction_response(
            num_imgs, conv_idx
        )

        return Response()
