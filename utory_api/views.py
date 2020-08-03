from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .serializers import *


class AchivementsAPI(viewsets.ModelViewSet):
    serializer_class = AchivementsSerializer
    queryset = Achivements.objects.all()


class ErrorsAPI(viewsets.ModelViewSet):
    serializer_class = ErrorsSerializer
    queryset = Errors.objects.all()


class StoriesAPI(viewsets.ModelViewSet):
    serializer_class = StoriesSerializer
    queryset = Stories.objects.all()


class UsersAPI(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class appRatingAPI(viewsets.ModelViewSet):
    serializer_class = appRatingSerializer
    queryset = AppRating.objects.all()


class PlayedstoryAPI(viewsets.ModelViewSet):
    serializer_class = PlayedstorySerializer
    queryset = PlayedStory.objects.all()


class StorycontentAPI(viewsets.ModelViewSet):
    serializer_class = StorycontentSerializer
    queryset = StoryContent.objects.all()


class StoryhistoryAPI(viewsets.ModelViewSet):
    serializer_class = StoryhistorySerializer
    queryset = StoryHistory.objects.all()


class StorystatusAPI(viewsets.ModelViewSet):
    serializer_class = StorystatusSerializer
    queryset = StoryStatus.objects.all()


class UserstatusAPI(viewsets.ModelViewSet):
    serializer_class = UserstatusSerializer
    queryset = UserStatus.objects.all()


class StoryidAPI(generics.ListCreateAPIView):
    serializer_class = StoryidSerializer
    queryset = StoryContent.objects.all()
    search_fields = ['=uuid']
    filter_backends = (filters.SearchFilter,)


class UseridAPI(generics.ListCreateAPIView):
    serializer_class = UseridSerializer
    queryset = Users.objects.all()
    search_fields = ['=uuid']
    filter_backends = (filters.SearchFilter,)

class RecentlyStoryAPI(generics.ListCreateAPIView):
    serializer_class = RecentlyStorySerializer
    def get_queryset(self):
        return Stories.objects.raw( ' select total.id, total.playcount, total.uuid, total.title, total.userName,total.rating '
                                    ' from Stories s '
                                    ' LEFT JOIN '
                                    ' ( select count(ps.id) playcount, coalesce(s.uuid, ss.uuid, ps.uuid) uuid, avg(if(ps.rating is null , 0, ps.rating))rating, s.id, s.title, s.userName '
                                    ' from Stories s '
                                    ' left join story_status ss on ss.uuid = s.uuid '
                                    ' left join played_story ps on ps.uuid = ss.uuid '
                                    ' where ss.published = true '
                                    ' group by s.uuid, s.id ) total on s.uuid = total.uuid '
                                    ' where total.uuid is not null '
                                    ' order by s.date desc '
                                    ' LIMIT 100;' )

class MostPlayedStoryAPI(generics.ListCreateAPIView):
    serializer_class = MostPlayedStorySerializer
    def get_queryset(self):
        return Stories.objects.raw( ' select total.id, total.playcount, total.uuid, total.title, total.userName,total.rating '
                                    ' from Stories s '
                                    ' LEFT JOIN '
                                    ' ( select count(ps.id) playcount, coalesce(s.uuid, ss.uuid, ps.uuid) uuid, avg(if(ps.rating is null , 0, ps.rating))rating, s.id, s.title, s.userName '
                                    ' from Stories s '
                                    ' left join story_status ss on ss.uuid = s.uuid '
                                    ' left join played_story ps on ps.uuid = ss.uuid '
                                    ' where ss.published = true '
                                    ' group by s.uuid, s.id ) total on s.uuid = total.uuid '
                                    ' where total.uuid is not null '
                                    ' order by total.playcount desc '
                                    ' LIMIT 100;' )

class HighestRatedPlayedStoryAPI(generics.ListCreateAPIView):
    serializer_class = HighestRatedStorySerializer
    def get_queryset(self):
        return Stories.objects.raw( ' select total.id, total.playcount, total.uuid, total.title, total.userName,total.rating '
                                    ' from Stories s '
                                    ' LEFT JOIN '
                                    ' ( select count(ps.id) playcount, coalesce(s.uuid, ss.uuid, ps.uuid) uuid, avg(if(ps.rating is null , 0, ps.rating))rating, s.id, s.title, s.userName '
                                    ' from Stories s '
                                    ' left join story_status ss on ss.uuid = s.uuid '
                                    ' left join played_story ps on ps.uuid = ss.uuid '
                                    ' where ss.published = true '
                                    ' group by s.uuid, s.id ) total on s.uuid = total.uuid '
                                    ' where total.uuid is not null '
                                    ' order by total.rating desc '
                                    ' LIMIT 100;' )



class MyStoriesAPI(generics.ListCreateAPIView):
    serializer_class = MyStoriesSerializer
    def get_queryset(self):
        userid = self.request.query_params.get('userid', None)
        title = self.request.query_params.get('title', None)
        return Stories.objects.raw(' select s.id, s.title, ss.published '
                                       ' from Stories s '
                                       ' left join Users u on u.uuid = s.userId '
                                       ' left join story_status ss on s.uuid = ss.uuid '
                                       ' where s.userid = %s and s.title = %s ', [userid, title]
                                       )























