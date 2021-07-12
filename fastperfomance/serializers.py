from rest_framework import serializers
from  fastperfomance import models


class LocustAPISerializer(serializers.ModelSerializer):
    """
    压测接口序列化
    """
    class Meta:
        model = models.LocustAPI
        fields = '__all__'

class LocustRUNAPISerializer(serializers.ModelSerializer):
    """
    压测接口序列化
    """
    class Meta:
        model = models.LocustAPI
        fields = ['id','name','body','url','method','users','rate','missiontime','assertstr','delete']