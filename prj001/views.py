#from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasScope
#from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, IsAuthenticatedOrTokenHasScope

from .models import GeneralInfo, Menstruation, Symptom, Other, ClinicalConclusion
from .models import InvestFileUpload
from .serializers import GeneralInfoListSerializer, GeneralInfoCreateSerializer, GeneralInfoDetailSerializer
from .serializers import MenstruationSerializer, SymptomSerializer, OtherSerializer, ClinicalConclusionSerializer
from .serializers import MyUserGenInfoDetailSerializer, InvestFileUploadSerializer, InfoSerializer
from .serializers import GeneralListSerializer
from .permissions import IsOwnerOrReadOnly, CheckOperationPerm
from myusers.models import MyUser

import xlrd
import magic
import urllib.parse
from django.conf import settings

import json

from .utils import perform_create_content
# 引入读取离线文件的工具包
from utils.read_file_util.questionairetojson import readQuestionaireExcel

# Create your views here.
#######################################################################
# class MyUserList(generics.ListAPIView):
#     permission_classes = [TokenHasScope, IsOwnerOrReadOnly]
#     required_scopes = ['prj001']
#     queryset = MyUser.objects.all()
#     serializer_class = MyUserListSerializer


class MyUserGenInfoDetail(generics.RetrieveAPIView):
    """
        get:
        获取该用户所创建的所有 一般情况 列表
    """
    permission_classes = [TokenHasScope, IsOwnerOrReadOnly]
    required_scopes = ['prj001']
    queryset = MyUser.objects.all()
    serializer_class = MyUserGenInfoDetailSerializer


class GeneralInfoList(generics.ListAPIView):
    """
        get:
        获取所有 一般情况 列表
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$name', '$nation')


class GeneralListView(generics.ListAPIView):
    """
    get - 获得个人发布的数据的详情列表
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']

    def get_queryset(self):
        # self.request.user 获取对象
        return GeneralInfo.objects.filter(owner_id=self.request.user.id)

    serializer_class = GeneralListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$name', '$nation')


class GeneralInfoCreate(generics.CreateAPIView):
    """
        post:
        创建一个 一般情况
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralInfoCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GeneralInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    """
        get:
        获取该 一般情况 的详情

        put:
        整体更新该 一般情况.

        patch:
        部分更新该 一般情况.

        delete:
        删除该 一般情况
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralInfoDetailSerializer


#######################################################################
class MenstruationViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 月经情况 的列表

        retrieve:
        获取该 月经情况 的详情

        create:
        创建一个 月经情况

        update:
        整体更新该 月经情况.

        partial_update:
        部分更新该 月经情况.

        delete:
        删除该 月经情况
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]  # CheckOperationPerm
    required_scopes = ['prj001']
    queryset = Menstruation.objects.all()
    serializer_class = MenstruationSerializer

    def perform_create(self, serializer):

        perform_create_content(self, GeneralInfo, serializer)


#######################################################################
class SymptomViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 全身症状 的列表

        retrieve:
        获取该 全身症状 的详情

        create:
        创建一个 全身症状

        update:
        整体更新该 全身症状.

        partial_update:
        部分更新该 全身症状.

        delete:
        删除该 全身症状
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

    def perform_create(self, serializer):

        perform_create_content(self, Symptom, serializer)


#######################################################################
class OtherViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 其它情况 的列表

        retrieve:
        获取该 其它情况 的详情

        create:
        创建一个 其它情况

        update:
        整体更新该 其它情况.

        partial_update:
        部分更新该 其它情况.

        delete:
        删除该 其它情况
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = Other.objects.all()
    serializer_class = OtherSerializer

    def perform_create(self, serializer):
        perform_create_content(self, Other, serializer)


#######################################################################
class ClinicalConclusionViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 临床诊断 的列表

        retrieve:
        获取该 临床诊断 的详情

        create:
        创建一个 临床诊断

        update:
        整体更新该 临床诊断.

        partial_update:
        部分更新该 临床诊断.

        delete:
        删除该 临床诊断
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = ClinicalConclusion.objects.all()
    serializer_class = ClinicalConclusionSerializer

    def perform_create(self, serializer):
        perform_create_content(self, ClinicalConclusion, serializer)


class InvestFileUploadViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 上传文件 的列表

        retrieve:
        获取该 上传文件 的详情

        create:
        创建一个 上传文件，用于批量生成病例信息

        update:
        整体更新该 上传文件.

        partial_update:
        部分更新该 上传文件.

        delete:
        删除该 上传文件
    """

    permission_classes = [TokenHasScope, CheckOperationPerm, ]
    required_scopes = ['prj001']

    def get_serializer_class(self):
        """
        提供序列化器
        """
        if self.action == 'list':
            return InvestFileUploadSerializer
        else:
            return InfoSerializer

    def create(self, request, *args, **kwargs):

        file = request.data.dict()

        resp_data = {
            "code": 0,
            "msg": "",
        }

        # print(file.get('ivfile'), "======")
        # print(file)

        if not file.get('ivfile'):
            resp_data["code"] = status.HTTP_204_NO_CONTENT
            resp_data["msg"] = "请选择上传的表格文件！"
            return Response(resp_data)

        serial = InvestFileUploadSerializer(data=file)

        serial.is_valid(raise_exception=True)
        # print(serial.errors)

        # 此时文件还是 InMemoryUploadedFile
        # 如果此时处理文件，则应形如：
        # wb = xlrd.open_workbook(file_contents=file['ivfile'].read())

        # 保存文件至本地 bv
        # file_contents = file['ivfile'].read()

        serial.save()

        # 检查文件类型
        file_path = serial.data["ivfile"]
        tmp_str = file_path.split('/', 2)
        file_path = settings.MEDIA_ROOT + "/" + tmp_str[2]
        de_path = urllib.parse.unquote(file_path)
        # print(de_path, "+++++++++++")

        # checkresult = magic.from_file(de_path)
        #
        # if "Microsoft Excel" in checkresult:
        #
        #     # 参数是文件路径
        try:
            file_data = readQuestionaireExcel(de_path)
        except Exception as e:
            resp_data["code"] = 1441
            resp_data["msg"] = "文件数据无法分析"
            return Response()
        #
        #     # #########old v
        #     # # 读取文件内容，进行处理
        #     # wb = xlrd.open_workbook(de_path)
        #     # table = wb.sheets()[0]
        #     # row = table.nrows
        #     # for i in range(1, row):
        #     #     col = table.row_values(i)
        #     #     print(col)
        # else:
        #     resp_data["code"] = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        #     resp_data["msg"] = "文件格式不是Excel"
        #     return Response(resp_data)

        # if "ASCII text" in checkresult:
        #     file_object = open('test.txt')
        #     try:
        #         file_context = file_object.read()
        #         print(file_context)
        #         # file_context是一个list，每行文本内容是list中的一个元素
        #         # file_context = open(file).read().splitlines()
        #     finally:
        #         file_object.close()
        # else:
        #     return Response(data="上传文件不是文本文件！", status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        data_str = json.dumps(serial.data)

        try:
            data_dict = json.loads(data_str)

            data_dict_file = json.loads(file_data)
            # print(data_dict_file)
        except Exception as e:
            resp_data["code"] = status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
            resp_data["msg"] = "数据转化发生错误"
            return Response(resp_data)

        # 返回的整体的json数据
        data_dict.update(data_dict_file)

        # 保存数据库
        from .utils import save_table_data
        try:
            save_table_data(data_dict)
        except Exception as e:
            print(e)
            resp_data["code"] = 1400
            resp_data["msg"] = "数据保存失败，请查看文件是否符合模板要求！！"
            return Response(resp_data)

        resp_data["code"] = status.HTTP_200_OK
        resp_data["msg"] = data_dict

        return Response(resp_data)

    def list(self, request, *args, **kwargs):

        self.queryset = InvestFileUpload.objects.all()

        return super(InvestFileUploadViewSet, self).list(request)


class GetPatientInfoView(generics.GenericAPIView):
    """
    get:
        获取患者的各项详细信息
    """
    permission_classes = [TokenHasScope, ]  # IsOwnerOrReadOnly
    required_scopes = ['prj001']

    def get(self, request, pk):

        if not pk:
            return Response({"msg": "请重新选择患者"})

        gen_obj = GeneralInfo.objects.filter(id=pk)

        if not gen_obj:
            return Response({"msg": "该病患还没有录入信息"})

        serializer = InfoSerializer(instance=gen_obj, many=True)

        return Response(serializer.data)
