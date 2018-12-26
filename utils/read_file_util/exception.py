from rest_framework.exceptions import APIException


class UploadFileException(APIException):
    status_code = 1040
    default_detail = '文件中必填字段未填写'

