
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),

    # Local apps
    path("", include("pages.urls") ),
    path("accounts/", include("accounts.urls")),

    # User management
    path("accounts/", include("django.contrib.auth.urls")),
    

]
