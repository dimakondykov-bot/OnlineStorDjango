from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView,CreateView,UpdateView,DeleteView
from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    paginate_by = 6
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_obj = context['page_obj']

        context['page_range'] = paginator.get_elided_page_range(
            page_obj.number,
            on_each_side=1,
            on_ends=1
        )
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.show.html'
    context_object_name = 'product'

class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')