from rest_framework import exceptions


def deny_permission(msg, request, own_obj):
    """
    无法通过权限的返回信息
    :param msg:  请求传递的参数-- msg = super().get_parser_context(request)
    :param request:
    :param own_obj: 对应的模型类
    """
    if request.authenticators and not request.successful_authenticator:
        raise exceptions.NotAuthenticated()

    try:
        pk = msg['kwargs'].get('pk')
    except Exception as e:
        data = {
            'detail': '路径中未包含该条信息的id %s' % e
        }
        raise exceptions.PermissionDenied(detail=data)

    try:
        obj = own_obj.objects.get(id=pk)
        owner = obj.owner
    except own_obj.DoesNotExist:
        data = {
            'detail': '该信息不存在'
        }
        raise exceptions.PermissionDenied(detail=data)

    data = {
        'detail': '您目前对该信息无修改权限, 如需修改请联系%s' % owner.user_name,
        'name': owner.email,
    }
    raise exceptions.PermissionDenied(detail=data)


