from django.urls import path
from .views import home, contacto, galeria, agregar_producto, listar_productos,modificar_producto, eliminar_producto,registro,CustomLoginView

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/',eliminar_producto, name="eliminar_producto" ),
    path('registro/',registro, name="registro" ),
    path('login/', CustomLoginView.as_view(), name='login'),
]