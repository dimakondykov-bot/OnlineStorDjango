from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'page_range'
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
    pk_url_kwarg = 'product_id'


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
