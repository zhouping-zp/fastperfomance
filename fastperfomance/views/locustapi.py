import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from fastperfomance import models, serializers
from rest_framework.response import Response

from django.db import DataError
from django.db.models import Q
import json
from fastperfomance.utils.locustutils import LocustFile, makefile, run

from rest_framework.schemas import AutoSchema, SchemaGenerator


class LocustAPIView(GenericViewSet):
    serializer_class = serializers.LocustAPISerializer
    queryset = models.LocustAPI.objects

    def list(self, request):
        """
        获取所有接口数据
        :param request:
        :return:
        """
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def single(self, request, **kwargs):
        """
        获取单个接口数据
        :param request:
        :param kwargs:
        :return:
        """
        try:
            locustapi = models.LocustAPI.objects.get(id=kwargs['pk'])
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(locustapi)
        return Response(serializer.data)

    def update(self, request, **kwargs):
        """
        修改一个接口
        :param request:
        :param kwargs:
        :return:
        """
        pk = kwargs['pk']
        try:
            locustapi = self.queryset.filter(id=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance=locustapi, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

    def add(self, request):
        """
        新增一个接口数据
        :param request:
        :return:
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, **kwargs):
        """
        软删除一个接口
        :param request:
        :param kwargs:
        :return:
        """
        try:
            self.queryset.filter(id=kwargs['pk']).update(delete=1, update_time=datetime.datetime.now())
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

