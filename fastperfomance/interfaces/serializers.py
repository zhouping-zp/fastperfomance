from rest_framework import serializers

from configures.models import Configures
from testcases.models import Testcases

from system.models import System
from utils import common, validates
from .models import Interfaces


# 使用模型序列化器类：简化序列化器类中字段的创建
class InterfacesModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    system_id = serializers.PrimaryKeyRelatedField(queryset=System.objects.all(), label='系统id',
                                                   help_text='系统id')

    # a.会将父表的主键id值作为返回值
    # projects = serializers.PrimaryKeyRelatedField(help_text='所属项目', label='所属项目', queryset=Projects.objects.all())
    # b.会将父表对应对象的__str__方法的结果返回
    # projects = serializers.StringRelatedField()
    # c.会将父表对应对象的某个字段的值返回
    # projects = serializers.SlugRelatedField(slug_field='leader', read_only=True)
    # d.可以将某个序列化器对象定义为字段，支持Field中的所有参数
    # projects1 = ProjectsModelSerializer(label='所属项目信息', help_text='所属项目信息', read_only=True)

    class Meta:
        model = Interfaces
        fields = (
            'id', 'name', 'request', 'create_time', 'path', 'method', 'system_id', 'rig_id', 'rig_env', 'threads',
            'rate', 'execution_time', 'latency_time', 'assertstr')

        extra_kwargs = {
            'create_time': {
                'read_only': True,
                'format': common.datetime_fmt()
            }
        }

    def create(self, validated_data):
        project = validated_data.pop('project_id')
        validated_data['project'] = project
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            project = validated_data.pop('project_id')
            validated_data['project'] = project

        return super().update(instance, validated_data)


class TestcasesNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testcases
        fields = ('id', 'name')


class TestcasesByInterfaceIdModelSerializer(serializers.ModelSerializer):
    testcases = TestcasesNamesModelSerializer(many=True, read_only=True)

    class Meta:
        model = Interfaces
        fields = ('testcases',)


class ConfiguresNamesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configures
        fields = ('id', 'name')


class ConfiguresByInterfaceIdModelSerializer(serializers.ModelSerializer):
    configures = ConfiguresNamesModelSerializer(many=True, read_only=True)

    class Meta:
        model = Interfaces
        fields = ('configures',)


class InterfaceRunSerializer(serializers.ModelSerializer):
    """
    通过接口来运行测试用例序列化器
    """
    env_id = serializers.IntegerField(write_only=True,
                                      help_text='环境变量ID',
                                      validators=[validates.is_exised_env_id])

    class Meta:
        model = Interfaces
        fields = ('id', 'env_id')
