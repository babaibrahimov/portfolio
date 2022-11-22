from django.urls import path
from portfolio import views

from .views import (index, 
                    aboutMe, 
                    social, 
                    projects,
                    )

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', index , name='home'),
    path('aboutme/', aboutMe, name='about'),
    path('socialmedia/', social, name='social'),
    path('myprojects/', projects, name='projects'),
]