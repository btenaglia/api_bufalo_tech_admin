from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from src.users.api.views import UserViewSet
from src.clients.api import views as clients_api_view
from src.providers.api import views as providers_api_view
from src.expenses.api import views as expenses_api_view


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("clients", clients_api_view.ClientsViewSet)
router.register("providers", providers_api_view.ProvidersViewSet)
router.register("expenses/types", expenses_api_view.TypesViewSet)


app_name = "api"
urlpatterns = router.urls
