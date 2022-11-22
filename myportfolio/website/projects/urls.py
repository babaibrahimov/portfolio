from django.urls import path
from .views import (addproject,
                    projectDetail,
                    project
                    )
from . import views

urlpatterns = [
    path('project/add/', addproject, name='addProject'),
    path('project/<int:pk>/', projectDetail, name='projectDetail'),
    path('', project, name='project')
]

# urlpatterns = [
#     path("", views.project_index, name="project_index"),
#     path("<int:pk>/", views.project_detail, name="project_detail"),
# ]
