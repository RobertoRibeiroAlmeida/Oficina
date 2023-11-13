from django.urls import path
from . import views


app_name = 'core'


urlpatterns = [
    path('grupos_produtos/', views.GrupoProdutoList.as_view(), name='grupos_produtos'),
    path('grupos_produtos/create/', views.GrupoProdutoCreateView.as_view(), name='create_grupo_produto'),
    path('grupos_produtos/update/<int:pk>', views.GrupoProdutoUpdateView.as_view(), name='update_grupo_produto'),
    path('grupos_produtos/read/<int:pk>', views.GrupoProdutoReadView.as_view(), name='read_grupo_produto'),
    path('grupos_produtos/delete/<int:pk>', views.GrupoProdutoDeleteView.as_view(), name='delete_grupo_produto'),
    path('produtos/', views.ProdutoList.as_view(), name='produtos'),
    path('produtos/create/', views.ProdutoCreateView.as_view(), name='create_produto'),
    path('produtos/update/<int:pk>', views.ProdutoUpdateView.as_view(), name='update_produto'),
    path('produtos/read/<int:pk>', views.ProdutoReadView.as_view(), name='read_produto'),
    path('produtos/delete/<int:pk>', views.ProdutoDeleteView.as_view(), name='delete_produto'),
    path('especialidades/', views.EspecialidadeList.as_view(), name='especialidades'),
    path('especialidades/create/', views.EspecialidadeCreateView.as_view(), name='create_especialidade'),
    path('especialidades/update/<int:pk>', views.EspecialidadeUpdateView.as_view(), name='update_especialidade'),
    path('especialidades/read/<int:pk>', views.EspecialidadeReadView.as_view(), name='read_especialidade'),
    path('especialidades/delete/<int:pk>', views.EspecialidadeDeleteView.as_view(), name='delete_especialidade'),
    path('profissionais/', views.ProfissionalList.as_view(), name='profissionais'),
    path('profissionais/create/', views.ProfissionalCreateView.as_view(), name='create_profissional'),
    path('profissionais/update/<int:pk>', views.ProfissionalUpdateView.as_view(), name='update_profissional'),
    path('profissionais/read/<int:pk>', views.ProfissionalReadView.as_view(), name='read_profissional'),
    path('profissionais/delete/<int:pk>', views.ProfissionalDeleteView.as_view(), name='delete_profissional')
]