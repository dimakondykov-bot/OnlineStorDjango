from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items(): # self.fields — это словарь всех полей формы
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        forbidden_words =  ['казино', 'криптовалюта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Запрещенное слово: {word}')
        return cleaned_data

    def clean_description(self):
        cleaned_desc = self.cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in forbidden_words:
            if word in cleaned_desc.lower():
                raise forms.ValidationError(f'Запрещенное слово: {word}')
        return cleaned_desc

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной')
        return price