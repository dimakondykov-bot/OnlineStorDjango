from django.urls import path
from .models import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]