from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from risk_types import views as risk_type_views
from risks import views as risk_views


router = routers.DefaultRouter()
router.register(r'risk-types', risk_type_views.RiskTypeViewSet)
router.register(r'risks', risk_views.RiskViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='app'),
    path('api/', include(router.urls)),
]


if settings.DEBUG:
    import os
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode