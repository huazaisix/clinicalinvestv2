from rest_framework import filters
from urllib.parse import unquote


class OwnSearchFilter(filters.SearchFilter):
    def get_search_terms(self, request):
        value = request.query_params.get(self.search_param, '')

        try:
            params = unquote(value, 'utf-8')
        except Exception as e:
            return ValueError('查询字段字符集无法转换%s' % e)

        return params.replace(',', ' ').split()
