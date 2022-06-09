from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [path('', views.index, name='login page'),
              path('signup/', views.signup, name='signup page'),
              path('profile/', views.my_profile, name='my profile'),
              path('rooms/', views.rooms, name='available rooms'),
              path('trend/', views.trends, name='trendings'),
              path('recovery/', views.forgot_pass, name='recovery'),
              path('logout/', views.log_out, name='log out'),
              path('phil/', views.philosophy, name='philosophy'),
              path('rel/', views.relationship, name='relationship'),
              path('gen/', views.general, name='general'),
              path('science/', views.science, name='science'),
              path('person/', views.personality, name='personality'),
              # path('post-img/', views.post_img, name=' posting image'),
              path('uploaded/', views.uploaded, name='my uploaded images'),
              path('settings/', views.settings, name='settings'),
              path('remove_post/', views.remove_post, name='delete post'),
              path('recov-info/', views.recover_pass, name='recov-info')
            ]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
