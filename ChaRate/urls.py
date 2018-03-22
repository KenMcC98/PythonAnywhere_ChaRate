from django.conf.urls import url
from ChaRate import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_tv/$', views.add_tv, name='add_tv'),
    url(r'^add_mov/$', views.add_mov, name = 'add_mov'),

    #2 of each kind for tv and movie but both link to same view
#    url(r'^tvpage/(?P<tv_name_slug>[\w\-]+)/$',
#        views.tvpage, name='tvpage'),
#    url(r'^movpage/(?P<mov_name_slug>[\w\-]+)/$',
#        views.movpage, name='movpage'),

#    url(r'^tvpage/(?P<tv_name_slug>[\w\-]+)/add_character/$',
#        views.create_character, name='create_character'),
#    url(r'^movpage/(?P<mov_name_slug>[\w\-]+)/add_character/$',
#        views.create_character, name='create_character'),
               
#    url(r'^(?P<character_name_slug>[\w\-]+)/$',
#        views.character, name='Character'),
               
               
    url(r'^movie_title/$', views.show_movie, name = 'movie'),
    url(r'tvshow_title/$', views.show_tvShow, name = 'tvshow'),
    url(r'^Character/$', views.show_character, name='character'),
    url(r'^add_character/$', views.add_character, name = 'add_character'),
    url(r'^link_movie/$', views.link_movie, name = 'link_movie'),
    url(r'^link_tvshow/$', views.linkTv, name = 'link_tv'),
    url(r'^mov_filter/$', views.mov_filter, name = 'filter_mov'),
    url(r'tv_filter/$', views.tv_filter, name = 'filter_tv'),
    url(r'account/$', views.Account, name = 'account'),
    url(r'search/$', views.search, name = 'search'),
    url(r'add_comment/$', views.add_comment, name = 'add_comment'),


    url(r'^login/$', views.user_login, name ='login'),
    url(r'^register/$', views.register, name='register'),
    
#    url(r'^logout/$', views.user_logout, name='logout'),
    #restricted +/ logout
    # No restricted page required

]
