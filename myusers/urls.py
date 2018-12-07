from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import MyUserList, MyUserDetail, UpdatePassword
from .views import UserView, UserLogoutView

urlpatterns = [

    path("register/", UserView.as_view(), name="myuser-register"),
    # path("login/", UserLoginView.as_view(), name="myuser-login"),
    path("logout/", UserLogoutView.as_view(), name="myuser-logout"),


    path('', MyUserList.as_view(), name='myuser-list'),
    path('<pk>/', MyUserDetail.as_view(), name='myuser-detail'),
    path('<pk>/changepassword/', UpdatePassword.as_view(), name='myuser-changepassword'),


]

# urlpatterns = format_suffix_patterns(urlpatterns)
