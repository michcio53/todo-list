from rest_framework.routers import SimpleRouter

from core.api.account import AccountAPIViewSet

account_router = SimpleRouter(trailing_slash=False)
account_router.register('', AccountAPIViewSet, 'account')
