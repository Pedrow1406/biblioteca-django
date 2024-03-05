from django import forms
from .models import Livro, Categoria, Emprestimo
class CadastroLivro(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'
        exclude = ['emprestado']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dono_livro_cadastrado'].widget = forms.HiddenInput()
        self.fields['usuario'].widget = forms.HiddenInput()
        
        for fields_name in self.fields:
            if fields_name != 'emprestado':
                self.fields[fields_name].widget.attrs['class'] = 'form-control'


class CadastroCategoria(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()

        for fields_name in self.fields:
            self.fields[fields_name].widget.attrs['class'] = 'form-control'
    class Meta:
        model = Categoria
        fields = "__all__"

class CadastroEmprestimo(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dono_livro_atual'].widget = forms.HiddenInput()
        self.fields['avaliacao'].widget = forms.HiddenInput()
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            if isinstance(self.fields[field_name].widget, forms.DateInput):
                self.fields[field_name].widget.input_type = 'date'

    class Meta:
        model = Emprestimo
        fields = '__all__'
        exclude = ['data_emprestimo','data_devolucao']
