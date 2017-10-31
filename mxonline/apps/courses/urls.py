# _*_ coding: utf-8 _*_
__author__ = 'Coder-Chandler'
__date__ = '2017.08.09 - 16:22'

from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView, CourseInfoView, CommentView, AddCommentView, \
                   VideoPlayView
urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentView.as_view(), name='course_comment'),

    # 添加课程评论
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name='video_play')
]
