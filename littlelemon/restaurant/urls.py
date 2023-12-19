from django.urls import path, include
#from django.contrib import admin
from restaurant import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    #path('menu', views.menuView.as_view()),
    path('booking/', include(router.urls)),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('category', views.CategoriesView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    

    
]