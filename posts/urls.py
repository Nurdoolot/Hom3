from django.urls import path
from .views import post_view, like_post, post_detail_view, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', post_view, name='post'),
    path('detail/<int:pk>', post_detail_view, name='detail'),
    path('like/', like_post, name='like'),
    path('create/',PostCreate.as_view(), name='create'),
    path('update/<int:pk>', PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>', PostDelete.as_view(), name='delete'),
]