import math

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets, views
from rest_framework.response import Response
from urllib.parse import unquote, quote, urlencode

from myusers.models import MyUser
from .models import GeneralInfo, Menstruation, Symptom, Other, ClinicalConclusion
from .models import InvestFileUpload
from .permissions import IsOwnerOrReadOnly, CheckOperationPerm
from .serializers import GeneralInfoCreateSerializer, GeneralInfoDetailSerializer
from .serializers import GeneralListSerializer, GeneralInfoPageSeriaializer
from .serializers import MenstruationSerializer, SymptomSerializer, OtherSerializer, ClinicalConclusionSerializer
from .serializers import MyUserGenInfoDetailSerializer, InvestFileUploadSerializer, InfoSerializer
from .utils.utils import get_and_post
from .utils.utils import group_permission_show
from .utils.utils import perform_create_content, create_file_view
from .utils.utils_excel import save_excel
from .utils.search_util import OwnSearchFilter


class MyUserGenInfoDetail(generics.RetrieveAPIView):
    """
        get:
        获取该用户所创建的所有 一般情况 列表
    """
    permission_classes = [TokenHasScope, IsOwnerOrReadOnly]
    required_scopes = ['prj001']
    queryset = MyUser.objects.all()
    serializer_class = MyUserGenInfoDetailSerializer


class GeneralInfoList(generics.ListCreateAPIView):
    """
        get:
        获取所有 一般情况 列表
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    serializer_class = GeneralListSerializer

    filter_backends = (DjangoFilterBackend, OwnSearchFilter,)
    # TODO 多个删选条件
    # filter_class = GenInfoFilter
    search_fields = ('=age', 'nation', 'name', 'career', 'blood_type', 'marriage')

    # 分组 -- 组内成员具有查看权限,其他组员无查看权限
    def get_queryset(self):
        return group_permission_show(self)

    def get(self, request, *args, **kwargs):

        search_index = request.query_params.get('search')

        total_num = self.get_queryset().count()
        total_pages = math.ceil(total_num / settings.GEN_PAGE_SIZE)
        queryset = self.filter_queryset(self.get_queryset())

        resp_dict = dict()

        if search_index:
            search_pages = math.ceil(len(queryset) / settings.GEN_PAGE_SIZE)
            resp_dict['total_pages'] = search_pages
        else:
            resp_dict["total_pages"] = total_pages

        page = get_and_post(request, queryset=queryset)

        # 清除之前的数据,再设置
        try:
            del request.session[str(request.user.id)]
        except KeyError:
            pass

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            resp_dict['totalCount'] = total_num
            resp_dict['count'] = len(queryset)
            resp_dict["results"] = serializer.data

            request.session[str(request.user.id)] = serializer.data

            print(request.user.id)

            return Response(resp_dict)

        context = {
            'request': request
        }
        serializer = self.get_serializer(instance=queryset,
                                         context=context,
                                         many=True)

        # 总记录数
        resp_dict['totalCount'] = total_num
        # 符合search 的数
        resp_dict['count'] = len(queryset)
        resp_dict["results"] = serializer.data

        request.session[str(request.user.id)] = serializer.data

        return Response(resp_dict)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = GeneralInfoPageSeriaializer(data=data)
        serializer.is_valid(raise_exception=True)

        page = serializer.validated_data["page"]

        end_num = (page-1) * settings.GEN_PAGE_SIZE + settings.GEN_PAGE_SIZE

        gen_list = self.get_queryset()[(page-1)*settings.GEN_PAGE_SIZE: end_num]

        gen_obj_list = get_and_post(request=request, queryset=gen_list)

        serializer_context = {
            'request': request,
        }

        serializer_gen = self.get_serializer(gen_obj_list,
                                             many=True,
                                             context=serializer_context)
        resp_data = dict()
        resp_data["results"] = serializer_gen.data
        
        return Response(resp_data)


class GeneralListView(generics.ListAPIView):
    """
    get - 获得个人发布的数据的详情列表
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']

    def get_queryset(self):
        # self.request.user 获取对象
        return GeneralInfo.objects.filter(owner_id=self.request.user.id)

    serializer_class = InfoSerializer
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('$name', '$nation')


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
    # queryset = Menstruation.objects.all()
    serializer_class = MenstruationSerializer

    def get_queryset(self):
        # print(self.request.user.get_all_permissions(), "用户的所有权限")
        # print(self.request.user.get_group_permissions(), "用户的组权限")

        return Menstruation.objects.all()

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

        perform_create_content(self, GeneralInfo, serializer)


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
        perform_create_content(self, GeneralInfo, serializer)


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
        perform_create_content(self, GeneralInfo, serializer)


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


class FileDownloadView(generics.GenericAPIView):
    """
    GET - 下载文件
    """
    permission_classes = [TokenHasScope, ]
    required_scopes = ['prj001']

    def get(self, request, *args, **kwargs):
        #
        try:
            excel_data = request.session[str(request.user.id)]
        except KeyError:
            return ValueError('并没有需要保存的值')
        id_list = []
        # 抽离id
        for item in excel_data:
            id_list.append(item.get('id'))

        gen_os = GeneralInfo.objects.filter(id__in=id_list)

        serializer = InfoSerializer(instance=gen_os,
                                    context={'request': request},
                                    many=True)

        save_excel(serializer)

        return Response(serializer.data)
