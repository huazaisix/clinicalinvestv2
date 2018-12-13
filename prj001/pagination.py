from rest_framework.pagination import PageNumberPagination
from django.conf import settings


class GenPage(PageNumberPagination):
    """一般信息分页类"""
    page_size = settings.GEN_PAGE_SIZE
