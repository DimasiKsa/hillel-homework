from groups.views import hello_groups, get_groups, create_groups , update_group
from django.urls import path

app_name = 'groups'

urlpatterns = [
    path('', hello_groups, name='hello'),
    path('get_groups/', get_groups, name='list'),
    path('create_groups/', create_groups, name='create'),
    path('update_groups/<int:pk>/', update_group, name='update'),
]