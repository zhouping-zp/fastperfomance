from django.core.exceptions import ObjectDoesNotExist
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from fastperfomance import models, serializers
from rest_framework.response import Response

from django.db import DataError
from django.db.models import Q
import json

from fastperfomance.utils.locustutils import LocustFile, makefile, run


class LocustRUNAPIView(GenericViewSet):
    serializer_class = serializers.LocustRUNAPISerializer
    queryset = models.LocustAPI.objects

    def run_single(self, request, pk):

        try:
            locustapi = models.LocustAPI.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



        serializer = self.serializer_class(locustapi)

        qdict = eval(str(serializer.data).replace(r'"',""))


        api = LocustFile()
        datatext = LocustFile.prepare_locust_tests(api,qdict)
        locustfile1 = makefile(datatext)
        run(locustfile1, datatext)
        return Response(status=status.HTTP_200_OK)
