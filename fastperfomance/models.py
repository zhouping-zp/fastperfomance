from django.db import models

# Create your models here.
# from model_utils import  Choices
# from fastuser.models import BaseTable
# from fastrunner.models import Project



# class LocustCase(BaseTable):
#     """
#     压测集信息表
#     """
#     class Meta:
#         verbose_name ='压测集信息'
#         da_table = 'locustcase'
#     name = models.CharField('压测集名称',null=False,max_length=100,help_text='压测集名称')
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, db_constraint=False,help_text='所属项目')
#     inclue = models.TextField('包含的压测接口',help_text='包含的压测接口')
#
#     def __str__(self):
#         return self.name


class LocustAPI(models.Model):
    """
    压测API信息表
    """
    class Meta:
        verbose_name = '压测接口信息'
        db_table = 'locustapi'

    ENV_TYPE = (
        (0, "测试环境"),
        (1, "生产环境"),
        (2, "预发布 ")
    )
    # TAG = Choices(
    #     (0, "未知"),
    #     (1, "成功"),
    #     (2, "失败"),
    #     (3, "自动成功")
    # )
    name = models.CharField('接口名称',null=False,max_length=100,db_index=True,help_text='接口名称')
    body = models.TextField('主体信息',null=False,help_text='主体信息')
    url = models.CharField('请求地址',null=False,max_length=255,db_index=True,help_text='请求地址')
    method = models.CharField('请求方式',null=False,max_length=10,help_text='请求方式')
    # project = models.ForeignKey(Project, on_delete=models.CASCADE, db_constraint=False,help_text='')
    delete = models.IntegerField('是否删除',null=True,default=0,help_text='是否删除')
    rig_id = models.IntegerField("网关API_id", null=True, db_index=True,help_text='网关API_id')
    rig_env = models.IntegerField("网关环境", choices=ENV_TYPE, default=0,help_text='网关环境')
    # tag = models.IntegerField("API标签", choices=TAG, default=0,help_text='API标签')
    users = models.IntegerField('并发用户数',null=False,default=1,help_text='并发用户数')
    rate = models.IntegerField('加压速率',null=False,default=1,help_text='加压速率')
    missiontime = models.CharField('压测时间',max_length=255,null=False,help_text='压测时间')
    assertstr = models.CharField('断言字符串',max_length=255,null=False,help_text='断言字符串')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    creator = models.CharField(verbose_name="创建人", max_length=20, null=True)
    updater = models.CharField(verbose_name="更新人", max_length=20, null=True)
    def __str__(self):
        return self.name

