from django.urls import path    # 8.
from . import views             # 9.

app_name = 'shop'               # 10.

urlpatterns = [
    path('', views.product_list, name='product_list'),  # 11.
    # 21.
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    # 22.
    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail')
]
