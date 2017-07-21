from django.conf.urls import url

from . import views, views_class
import movie.views
import recommend.views


urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^import', views.import_ratings, name='import_ratings'),

    url(r'^2login', views_class.AuthLoginView.as_view(), name='login-view'),

    url(r'^$', views.user_list, name='user_list'),
    url(r'^(?P<username>[-\w]+)/$', views.user_profile, name='user_profile'),
    url(r'^(?P<username>[-\w]+)/export$', views.export_ratings, name='export_ratings'),
    url(r'^(?P<username>[-\w]+)/edit/$', views.user_edit, name='user_edit'),

    url(r'^(?P<username>[-\w]+)/watchlist/$', movie.views.watchlist, name='watchlist'),
    url(r'^(?P<username>[-\w]+)/favourites/$', movie.views.favourite, name='favourite'),
    url(r'^(?P<username>[-\w]+)/recommend/$', recommend.views.recommend, name='recommend'),
]