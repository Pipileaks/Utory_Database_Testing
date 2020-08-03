"""UtoryTesting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from utory_api import views


router = routers.DefaultRouter()


router.register('Achivements', views.AchivementsAPI)
router.register('Errors', views.ErrorsAPI)
router.register('Stories', views.StoriesAPI)
router.register('Users', views.UsersAPI)
router.register('Apprating', views.appRatingAPI)
router.register('playedStory', views.PlayedstoryAPI)
router.register('Storycontent', views.StorycontentAPI)
router.register('Storyhistory', views.StoryhistoryAPI)
router.register('Storystatus', views.StorystatusAPI)
router.register('Userstatus', views.UserstatusAPI)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('storyid/', views.StoryidAPI.as_view()),
    path('userid/', views.UseridAPI.as_view()),
    path('recentlystories/', views.RecentlyStoryAPI.as_view()),
    path('mostplayedstories/', views.MostPlayedStoryAPI.as_view()),
    path('highestratedstories/', views.HighestRatedPlayedStoryAPI.as_view()),
    path('mystories/', views.MyStoriesAPI.as_view()),
]
