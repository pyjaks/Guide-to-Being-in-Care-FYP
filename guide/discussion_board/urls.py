from django.urls import path
from . import views

urlpatterns = [
    path('', views.DiscussionBoardHomeView.as_view(template_name='discussion-boards.html'), name='discussion-board'),
    path('detail/<slug:slug>/', views.DiscussionBoardDetailView.as_view(), name='detail'),
    path('posts/<slug:slug>/', views.DiscussionBoardPostsView.as_view(template_name='posts.html'), name='posts'),
    path('new-post', views.NewPostView.as_view(template_name='new-post.html'), name='new-post'),
    path('new-post-success', views.NewPostSuccessView.as_view(template_name='new-post-success.html'), name='new-post-success'),

]
