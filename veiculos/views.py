from django.urls import reverse_lazy
from django.views import generic
from .forms import MarcaModelForm, ModeloModelForm, ClienteModelForm, VeiculoModelForm
from .models import Marca, Modelo, Cliente, Veiculo
from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

# MARCAS
class MarcaList(generic.ListView):
  model = Marca
  context_object_name = 'marcas'
  template_name = 'marca_list.html'
  queryset = Marca.objects.all()


class MarcaCreateView(BSModalCreateView):
  template_name = 'core/create_marca.html'
  form_class = MarcaModelForm
  success_message = 'Marca criada com sucesso.'
  success_url = reverse_lazy('core:marcas')


class MarcaUpdateView(BSModalUpdateView):
  model = Marca
  template_name = 'core/update_marca.html'
  form_class = MarcaModelForm
  success_message = 'Marca atualizada com sucesso.'
  success_url = reverse_lazy('core:marcas')


class MarcaReadView(BSModalReadView):
  model = Marca
  template_name = 'core/read_marca.html'


class MarcaDeleteView(BSModalDeleteView):
  model = Marca
  template_name = 'core/delete_marca.html'
  success_message = 'Marca excluida com sucesso.'
  success_url = reverse_lazy('core:marcas')

# MODELOS
class ModeloList(generic.ListView):
  model = Modelo
  context_object_name = 'modelos'
  template_name = 'modelo_list.html'
  queryset = Modelo.objects.all()

class ModeloCreateView(BSModalCreateView):
  template_name = 'core/create_modelo.html'
  form_class = ModeloModelForm
  success_message = 'Modelo criado com sucesso.'
  success_url = reverse_lazy('core:modelos')

class ModeloUpdateView(BSModalUpdateView):
  model = Modelo
  template_name = 'core/update_modelo.html'
  form_class = ModeloModelForm
  success_message = 'Modelo atualizado com sucesso.'
  success_url = reverse_lazy('core:modelos')

class ModeloReadView(BSModalReadView):
  model = Modelo
  template_name = 'core/read_modelo.html'

class ModeloDeleteView(BSModalDeleteView):
  model = Modelo
  template_name = 'core/delete_modelo.html'
  success_message = 'Modelo excluido com sucesso.'
  success_url = reverse_lazy('core:modelos')


# CLIENTES
class ClienteList(generic.ListView):
  model = Cliente
  context_object_name = 'clientes'
  template_name = 'cliente_list.html'
  queryset = Cliente.objects.all()

class ClienteCreateView(BSModalCreateView):
  template_name = 'core/create_cliente.html'
  form_class = ClienteModelForm
  success_message = 'Cliente criado com sucesso.'
  success_url = reverse_lazy('core:clientes')

class ClienteUpdateView(BSModalUpdateView):
  model = Cliente
  template_name = 'core/update_cliente.html'
  form_class = ClienteModelForm
  success_message = 'Cliente atualizado com sucesso.'
  success_url = reverse_lazy('core:clientes')

class ClienteReadView(BSModalReadView):
  model = Cliente
  template_name = 'core/read_cliente.html'

class ClienteDeleteView(BSModalDeleteView):
  model = Cliente
  template_name = 'core/delete_cliente.html'
  success_message = 'Cliente excluido com sucesso.'
  success_url = reverse_lazy('core:clientes')

# VEICULOS
class VeiculoList(generic.ListView):
  model = Veiculo
  context_object_name = 'veiculos'
  template_name = 'veiculo_list.html'
  queryset = Veiculo.objects.all()

class VeiculoCreateView(BSModalCreateView):
  template_name = 'core/create_veiculo.html'
  form_class = VeiculoModelForm
  success_message = 'Veiculo criado com sucesso.'
  success_url = reverse_lazy('core:veiculos')

class VeiculoUpdateView(BSModalUpdateView):
  model = Veiculo
  template_name = 'core/update_veiculo.html'
  form_class = VeiculoModelForm
  success_message = 'Veiculo atualizado com sucesso.'
  success_url = reverse_lazy('core:veiculos')

class VeiculoReadView(BSModalReadView):
  model = Veiculo
  template_name = 'core/read_veiculo.html'

class VeiculoDeleteView(BSModalDeleteView):
  model = Veiculo
  template_name = 'core/delete_veiculo.html'
  success_message = 'Veiculo excluido com sucesso.'
  success_url = reverse_lazy('core:veiculos')