from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^genres/$', views.genres),
    url(r'^genres/(?P<genre>[\w\-]+)/$', views.genresList),
    url(r'^platforms/$', views.platforms),
    url(r'^platforms/(?P<platform>[\w\" "\-]+)/$', views.platformList),
    url(r'^publishers/$', views.publishers),
    url(r'^publishers/(?P<publisher>[\w\" "\&\w]+)/$', views.publisherList),
    url(r'^search/$', views.search),
    url(r'^ajax_search/$', views.ajax_search),
    url(r'^games/(?P<game>[\w\:\'\" "\-]+)/$', views.gameList),
    url(r'^gamelist/(?P<pk>\d+)$', views.GameDetailApiView.as_view()),
    url(r'^gamelist/(?P<pk>\d+)/edit$', views.GameUpdateApiView.as_view()),
    url(r'^gamelist?', views.GameList.as_view()),
    url(r'^genrelist', views.GenreList.as_view()),
    url(r'^platformlist', views.PlatformList.as_view()),
    url(r'^publisherlist', views.PublisherList.as_view()),
    url(r'^docs/', include('rest_framework_docs.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
