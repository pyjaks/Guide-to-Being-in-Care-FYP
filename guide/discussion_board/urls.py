from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(template_name='forums.html'), name='discussion-board'),
#    path('detail', views.HomePageView.as_view(template_name='detail.html'), name='discussion-board-details'),
    path('detail/<slug>', views.DiscussionBoardDetailView.as_view(template_name='detail.html'), name='detail'),
    path('posts', views.HomePageView.as_view(template_name='posts.html'), name='posts'),

]
