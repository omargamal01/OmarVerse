from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio import views
urlpatterns = [path("admin/",admin.site.urls),path("",views.home,name="home"),path("about/",views.about,name="about"),path("projects/",views.projects,name="projects"),path("projects/<slug:slug>/",views.project_detail,name="project_detail"),path("contact/",views.contact,name="contact")]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
