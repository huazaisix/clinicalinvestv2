from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import GeneralInfoList, GeneralInfoCreate, GeneralInfoDetails
from .views import MenstruationViewSet, SymptomViewSet, OtherViewSet, ClinicalConclusionViewSet
from .views import MyUserGenInfoDetail, InvestFileUploadViewSet, GeneralListView
from .views import GetPatientInfoView, FileDownloadView

menstruation_list = MenstruationViewSet.as_view({
    # 'get': 'list',
    'post': 'create'
})
menstruation_detail = MenstruationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# symptom_list = SymptomViewSet.as_view({
#     # 'get': 'list',
#     'post': 'create'
# })
# symptom_detail = SymptomViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

other_list = OtherViewSet.as_view({
    # 'get': 'list',
    'post': 'create'
})
other_detail = OtherViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

clinicalconclusion_list = ClinicalConclusionViewSet.as_view({
    # 'get': 'list',
    'post': 'create'
})
clinicalconclusion_detail = ClinicalConclusionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

investfileupload_list = InvestFileUploadViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
patient_view = GetPatientInfoView.as_view()


urlpatterns = [
    path('geninfo/', GeneralInfoList.as_view(), name='generalinfo'),
    path('geninfo/list/', GeneralListView.as_view(), name='generalinfo-list'),
    path('geninfo/create/', GeneralInfoCreate.as_view(), name='generalinfo-create'),
    path('geninfo/<pk>/', GeneralInfoDetails.as_view(), name='generalinfo-detail'),  # 注意这里必须是破折号，因为列表那边会自动构建
    # 月经情况
    path('menstruation/', menstruation_list, name='menstruation-list'),
    path('menstruation/<pk>/', menstruation_detail, name='menstruation-detail'),
    # 全身症状
    path('symptom/', SymptomViewSet.as_view(), name='symptom-create'),
    path('symptom/<pk>/', SymptomViewSet.as_view(), name='symptom-detail'),
    # 其它情况
    path('other/', other_list, name='other-list'),
    path('other/<pk>/', other_detail, name='other-detail'),
    # 临床诊断
    path('cc/', clinicalconclusion_list, name='clinicalconclusion-list'),
    path('cc/<pk>/', clinicalconclusion_detail, name='clinicalconclusion-detail'),
    # 用户创建的病例列表
    path('users/<pk>/', MyUserGenInfoDetail.as_view(), name='prj001-myuser-detail'),
    # 用户上传excel文件
    path('upload/', investfileupload_list, name='investfileupload-list'),

    path("patientInfo/<pk>/", patient_view, name="patient-info"),

    path('download/', FileDownloadView.as_view(), name='download-csv'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
