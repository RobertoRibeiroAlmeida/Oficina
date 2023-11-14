from .models import GrupoProduto, Produto, GrupoServico, Servico, Especialidade, Profissional
from bootstrap_modal_forms.forms import BSModalModelForm


class GrupoProdutoModelForm(BSModalModelForm):
    class Meta:
        model = GrupoProduto
        exclude = ['id']


class ProdutoModelForm(BSModalModelForm):
    class Meta:
        model = Produto
        exclude = ['id']


class GrupoServicoModelForm(BSModalModelForm):
    class Meta:
        model = GrupoServico
        exclude = ['id']


class ServicoModelForm(BSModalModelForm):
    class Meta:
        model = Servico
        exclude = ['id']


class EspecialidadeModelForm(BSModalModelForm):
    class Meta:
        model = Especialidade
        exclude = ['id']


class ProfissionalModelForm(BSModalModelForm):
    class Meta:
        model = Profissional
        exclude = ['id']
