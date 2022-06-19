from django.conf import settings
from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as accounts_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # django form을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    # django modelform을 이용해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    path('detail/<int:blog_id>', views.detail, name='detail'),

    # media 파일에 접근할 수 있는 url도 추가 해줘야한다.
    path('create_comment/<int:blog_id>',
         views.create_comment, name='create_comment'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),


]
# 아래는 관례처럼 굳어진 거라서 이해보다는 외우는게 편하다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
