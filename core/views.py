from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import GrupoProdutoModelForm, ProdutoModelForm, GrupoServicoModelForm, ServicoModelForm, EspecialidadeModelForm, ProfissionalModelForm
from .models import GrupoProduto, Produto, GrupoServico, Servico, Especialidade, Profissional
from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)


# GrupoProduto
@method_decorator(login_required, name='dispatch')
class GrupoProdutoList(generic.ListView):
  model = GrupoProduto
  context_object_name = 'grupos_produtos'
  template_name = 'grupoproduto_list.html'
  queryset = GrupoProduto.objects.all()


@method_decorator(login_required, name='dispatch')
class GrupoProdutoCreateView(BSModalCreateView):
  template_name = 'core/create_grupo_produto.html'
  form_class = GrupoProdutoModelForm
  success_message = 'Grupo de produtos criado com sucesso.'
  success_url = reverse_lazy('core:grupos_produtos')


@method_decorator(login_required, name='dispatch')
class GrupoProdutoUpdateView(BSModalUpdateView):
  model = GrupoProduto
  template_name = 'core/update_grupo_produto.html'
  form_class = GrupoProdutoModelForm
  success_message = 'Grupo de produtos atualizado com sucesso.'
  success_url = reverse_lazy('core:grupos_produtos')


@method_decorator(login_required, name='dispatch')
class GrupoProdutoReadView(BSModalReadView):
  model = GrupoProduto
  template_name = 'core/read_grupo_produto.html'


@method_decorator(login_required, name='dispatch')
class GrupoProdutoDeleteView(BSModalDeleteView):
  model = GrupoProduto
  template_name = 'core/delete_grupo_produto.html'
  success_message = 'Grupo de produtos excluido com sucesso.'
  success_url = reverse_lazy('core:grupos_produtos')


# Produto
@method_decorator(login_required, name='dispatch')
class ProdutoList(generic.ListView):
  model = Produto
  context_object_name = 'produtos'
  template_name = 'produto_list.html'
  queryset = Produto.objects.all()


@method_decorator(login_required, name='dispatch')
class ProdutoCreateView(BSModalCreateView):
  template_name = 'core/create_produto.html'
  form_class = ProdutoModelForm
  success_message = 'Produto criado com sucesso.'
  success_url = reverse_lazy('core:produtos')


@method_decorator(login_required, name='dispatch')
class ProdutoUpdateView(BSModalUpdateView):
  model = Produto
  template_name = 'core/update_produto.html'
  form_class = ProdutoModelForm
  success_message = 'Produto atualizado com sucesso.'
  success_url = reverse_lazy('core:produtos')


@method_decorator(login_required, name='dispatch')
class ProdutoReadView(BSModalReadView):
  model = Produto
  template_name = 'core/read_produto.html'


@method_decorator(login_required, name='dispatch')
class ProdutoDeleteView(BSModalDeleteView):
  model = Produto
  template_name = 'core/delete_produto.html'
  success_message = 'Produto excluido com sucesso.'
  success_url = reverse_lazy('core:produtos')


# GrupoServico
class GrupoServicoList(generic.ListView):
  model = GrupoServico
  context_object_name = 'grupos_servicos'
  template_name = 'gruposervico_list.html'
  queryset = GrupoServico.objects.all()


class GrupoServicoCreateView(BSModalCreateView):
  template_name = 'core/create_grupo_servico.html'
  form_class = GrupoServicoModelForm
  success_message = 'Grupo de servicos criado com sucesso.'
  success_url = reverse_lazy('core:grupos_servicos')


class GrupoServicoUpdateView(BSModalUpdateView):
  model = GrupoServico
  template_name = 'core/update_grupo_servico.html'
  form_class = GrupoServicoModelForm
  success_message = 'Grupo de servicos atualizado com sucesso.'
  success_url = reverse_lazy('core:grupos_servicos')


class GrupoServicoReadView(BSModalReadView):
  model = GrupoServico
  template_name = 'core/read_grupo_servico.html'


class GrupoServicoDeleteView(BSModalDeleteView):
  model = GrupoServico
  template_name = 'core/delete_grupo_servico.html'
  success_message = 'Grupo de servicos excluido com sucesso.'
  success_url = reverse_lazy('core:grupos_servicos')


# Servico
class ServicoList(generic.ListView):
  model = Servico
  context_object_name = 'servicos'
  template_name = 'servico_list.html'
  queryset = Servico.objects.all()


class ServicoCreateView(BSModalCreateView):
  template_name = 'core/create_servico.html'
  form_class = ServicoModelForm
  success_message = 'Servico criado com sucesso.'
  success_url = reverse_lazy('core:servicos')


class ServicoUpdateView(BSModalUpdateView):
  model = Servico
  template_name = 'core/update_servico.html'
  form_class = ServicoModelForm
  success_message = 'Servico atualizado com sucesso.'
  success_url = reverse_lazy('core:servicos')


class ServicoReadView(BSModalReadView):
  model = Servico
  template_name = 'core/read_servico.html'


class ServicoDeleteView(BSModalDeleteView):
  model = Servico
  template_name = 'core/delete_servico.html'
  success_message = 'Servico excluido com sucesso.'
  success_url = reverse_lazy('core:servicos')


# Especialidades
class EspecialidadeList(generic.ListView):
  model = Especialidade
  context_object_name = 'especialidades'
  template_name = 'especialidade_list.html'
  queryset = Especialidade.objects.all()


class EspecialidadeCreateView(BSModalCreateView):
  template_name = 'core/create_especialidade.html'
  form_class = EspecialidadeModelForm
  success_message = 'Especialidade criada com sucesso.'
  success_url = reverse_lazy('core:especialidades')


class EspecialidadeUpdateView(BSModalUpdateView):
  model = Especialidade
  template_name = 'core/update_especialidade.html'
  form_class = EspecialidadeModelForm
  success_message = 'Especialidade atualizada com sucesso.'
  success_url = reverse_lazy('core:especialidades')


class EspecialidadeReadView(BSModalReadView):
  model = Especialidade
  template_name = 'core/read_especialidade.html'


class EspecialidadeDeleteView(BSModalDeleteView):
  model = Especialidade
  template_name = 'core/delete_especialidade.html'
  success_message = 'Especialidade excluida com sucesso.'
  success_url = reverse_lazy('core:especialidades')


# Profissionaiss
class ProfissionalList(generic.ListView):
  model = Profissional
  context_object_name = 'profissionais'
  template_name = 'profissional_list.html'
  queryset = Profissional.objects.all()


class ProfissionalCreateView(BSModalCreateView):
  template_name = 'core/create_profissional.html'
  form_class = ProfissionalModelForm
  success_message = 'Profissional criado com sucesso.'
  success_url = reverse_lazy('core:profissionais')


class ProfissionalUpdateView(BSModalUpdateView):
  model = Profissional
  template_name = 'core/update_profissional.html'
  form_class = ProfissionalModelForm
  success_message = 'Profissional atualizado com sucesso.'
  success_url = reverse_lazy('core:profissionais')


class ProfissionalReadView(BSModalReadView):
  model = Profissional
  template_name = 'core/read_profissional.html'


class ProfissionalDeleteView(BSModalDeleteView):
  model = Profissional
  template_name = 'core/delete_profissional.html'
  success_message = 'Profissional excluido com sucesso.'
  success_url = reverse_lazy('core:profissionais')
