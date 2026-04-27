from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog_preview/', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')  # Галочка (Да/Нет)
    views_count = models.PositiveIntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'preview', 'is_published', 'views_count', 'create_at']
    success_url = reverse_lazy('blog:list')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse('blog:view', kwargs={'pk': self.object.pk})
        # Это ID той самой статьи, которую мы только что сохранили.
        # Пользователя вернёт на эту же статью, а не в общий список


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')
