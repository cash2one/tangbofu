from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^news_list/(?P<page>[0-9]*)', views.news_list, name='news_list'),
    url(r'^news_detail/(?P<news_id>[0-9]*)', views.news_detail, name="news_detail"),
    url(r'^join_us/', views.join_us, name="join_us"),
    url(r'^contact_us/', views.contact_us, name="contact_us"),
    url(r'^about/', views.about, name="about"),
    url(r'^send_email/$', views.send_email, name="send_email"),
]