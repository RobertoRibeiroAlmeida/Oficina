from .models import Marca, Modelo, Cliente, Veiculo
from bootstrap_modal_forms.forms import BSModalModelForm

class MarcaModelForm(BSModalModelForm):
    class Meta:
        model = Marca
        exclude = ['id']

class ModeloModelForm(BSModalModelForm):
    class Meta:
        model = Modelo
        exclude = ['id']


class ClienteModelForm(BSModalModelForm):
    class Meta:
        model = Cliente
        exclude = ['id']


class VeiculoModelForm(BSModalModelForm):
    class Meta:
        model = Veiculo
        exclude = ['id']
