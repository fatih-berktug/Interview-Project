from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import include

from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('vira/', include('vira.urls')),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = 'education.Views.ErrorViews.page_not_found'
# handler500 = 'education.Views.ErrorViews.page_not_found'
