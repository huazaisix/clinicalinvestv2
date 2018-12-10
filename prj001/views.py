#from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasScope
# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, IsAuthenticatedOrTokenHasScope

from .models import GeneralInfo, Menstruation, Symptom, Other, ClinicalConclusion
from .models import InvestFileUpload
from .serializers import GeneralInfoListSerializer, GeneralInfoCreateSerializer, GeneralInfoDetailSerializer
from .serializers import MenstruationSerializer, SymptomSerializer, OtherSerializer, ClinicalConclusionSerializer
from .serializers import MyUserGenInfoDetailSerializer, InvestFileUploadSerializer, InfoSerializer
from .serializers import GeneralListSerializer
from .permissions import IsOwnerOrReadOnly, CheckOperationPerm
from myusers.models import MyUser


from .utils import perform_create_content, create_file_view
from .utils import group_permission_show


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
    # queryset = GeneralInfo.objects.all()
    serializer_class = GeneralListSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$name', '$nation')

    def get_queryset(self):
        return group_permission_show(self)


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

    # def get(self, request, *args, **kwargs):
    #
    #     data = request.query_params
    #
    #     if data.get("to_type") == 1:
    #         self.permission_classes = [CheckOperationPerm]
    #
    #     return super().get(request)


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
    # queryset = Menstruation.objects.all()
    serializer_class = MenstruationSerializer

    def get_queryset(self):
        print(self.request.user.get_all_permissions(), "用户的所有权限")
        print(self.request.user.get_group_permissions(), "用户的组权限")

        return Menstruation.objects.all()

    def perform_create(self, serializer):
        # print(self.request.path, "--------------ceshi----------")

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
    serializer_class = InvestFileUploadSerializer

    def create(self, request, *args, **kwargs):

        file = request.data.dict()

        resp_data = {
            "code": 0,
            "msg": "",
        }

        serial = InvestFileUploadSerializer(data=file)

        serial.is_valid(raise_exception=True)
        # print(serial.errors)

        # 如果此时处理文件，则应形如：
        # wb = xlrd.open_workbook(file_contents=file['ivfile'].read())

        serial.save(owner=request.user)

        try:
            resp_data = create_file_view(serial, resp_data)
        except Exception as e:
            resp_data["msg"] = e
            return Response(resp_data)

        return Response(resp_data)

    def list(self, request, *args, **kwargs):

        # TODO: 返回自己上传的列表,还是所有数据
        self.queryset = InvestFileUpload.objects.all()

        # self.queryset = InvestFileUpload.objects.filter(owner=request.user)

        return super(InvestFileUploadViewSet, self).list(request)


class GetPatientInfoView(generics.GenericAPIView):
    """
    get:
        获取患者的各项详细信息
    """
    # permission_classes = [TokenHasScope, ]  # IsOwnerOrReadOnly

    def get_permissions(self):
        print(self.request.method)

        if self.request.method == "GET":
            self.permission_classes = [TokenHasScope, ]
        else:
            self.permission_classes = [TokenHasScope, CheckOperationPerm]

        return super().get_permissions()

    required_scopes = ['prj001']

    def get(self, request, pk):

        if not pk:
            return Response({"msg": "请重新选择患者"})

        gen_obj = GeneralInfo.objects.filter(id=pk)

        if not gen_obj:
            return Response({"msg": "该病患还没有录入信息"})

        serializer = InfoSerializer(instance=gen_obj, many=True)

        return Response(serializer.data)
