from django.urls import path
from . import views


app_name = 'veiculos'


urlpatterns = [
    path('marcas/', views.MarcaList.as_view(), name='marcas'),
    path('marcas/create/', views.MarcaCreateView.as_view(), name='create_marca'),
    path('marcas/update/<int:pk>', views.MarcaUpdateView.as_view(), name='update_marca'),
    path('marcas/read/<int:pk>', views.MarcaReadView.as_view(), name='read_marca'),
    path('marcas/delete/<int:pk>', views.MarcaDeleteView.as_view(), name='delete_marca'),
    path('modelos/', views.ModeloList.as_view(), name='modelos'),
    path('modelos/create/', views.ModeloCreateView.as_view(), name='create_modelo'),
    path('modelos/update/<int:pk>', views.ModeloUpdateView.as_view(), name='update_modelo'),
    path('modelos/read/<int:pk>', views.ModeloReadView.as_view(), name='read_modelo'),
    path('modelos/delete/<int:pk>', views.ModeloDeleteView.as_view(), name='delete_modelo'),
    path('clientes/', views.ClienteList.as_view(), name='clientes'),
    path('clientes/create/', views.ClienteCreateView.as_view(), name='create_cliente'),
    path('clientes/update/<int:pk>', views.ClienteUpdateView.as_view(), name='update_cliente'),
    path('clientes/read/<int:pk>', views.ClienteReadView.as_view(), name='read_cliente'),
    path('clientes/delete/<int:pk>', views.ClienteDeleteView.as_view(), name='delete_cliente'),
    path('veiculos/', views.VeiculoList.as_view(), name='veiculos'),
    path('veiculos/create/', views.VeiculoCreateView.as_view(), name='create_veiculo'),
    path('veiculos/update/<int:pk>', views.VeiculoUpdateView.as_view(), name='update_veiculo'),
    path('veiculos/read/<int:pk>', views.VeiculoReadView.as_view(), name='read_veiculo'),
    path('veiculos/delete/<int:pk>', views.VeiculoDeleteView.as_view(), name='delete_veiculo')
]