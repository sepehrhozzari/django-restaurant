from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    # urls of installed packages
    path('', include("debug_toolbar.urls")),
    path('comment/', include('comment.urls')),
    path('', include("django.contrib.auth.urls")),
    path('', include('social_django.urls', namespace='social')),

    # urls of our apps
    path('', include("restaurant.urls")),
    path('account/', include("account.urls")),
    path('cart/', include("cart.urls")),
    path('food-blog/', include("food_blog.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
