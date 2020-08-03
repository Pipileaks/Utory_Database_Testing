from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .serializers import *
userid2 = ''
title2 = ''

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
                                    ' ( select count(ps.id) playcount, ps.uuid, avg(ps.rating)rating, s.id, s.title, s.userName '
                                    '  from played_story ps '
                                    ' left join Stories s on s.uuid = ps.uuid '
                                    ' left join story_status ss on ss.uuid = ps.uuid '
                                    ' where ss.published = true '
                                    ' group by ps.uuid, s.id ) total on s.uuid = total.uuid '
                                    ' order by s.date desc '
                                    ' LIMIT 100 ')

class MostPlayedStoryAPI(generics.ListCreateAPIView):
    serializer_class = MostPlayedStorySerializer
    def get_queryset(self):
        return Stories.objects.raw( ' select total.id, total.playcount, total.uuid, total.title, total.userName,total.rating '
                                    ' from Stories s '
                                    ' LEFT JOIN '
                                    ' ( select count(ps.id) playcount, ps.uuid, avg(ps.rating)rating, s.id, s.title, s.userName '
                                    '  from played_story ps '
                                    ' left join Stories s on s.uuid = ps.uuid '
                                    ' left join story_status ss on ss.uuid = ps.uuid '
                                    ' where ss.published = true '
                                    ' group by ps.uuid, s.id ) total on s.uuid = total.uuid '
                                    ' order by playcount desc '
                                    ' LIMIT 100 ')

class HighestRatedPlayedStoryAPI(generics.ListCreateAPIView):
    serializer_class = HighestRatedStorySerializer
    def get_queryset(self):
        return Stories.objects.raw( ' select total.id, total.playcount, total.uuid, total.title, total.userName,total.rating '
                                    ' from Stories s '
                                    ' LEFT JOIN '
                                    ' ( select count(ps.id) playcount, ps.uuid, avg(ps.rating)rating, s.id, s.title, s.userName '
                                    '  from played_story ps '
                                    ' left join Stories s on s.uuid = ps.uuid '
                                    ' left join story_status ss on ss.uuid = ps.uuid '
                                    ' where ss.published = true '
                                    ' group by ps.uuid, s.id ) total on s.uuid = total.uuid '
                                    ' order by rating desc '
                                    ' LIMIT 100 ')



class DenemeAPI(generics.ListCreateAPIView):
    serializer_class = DenemeSerializer
    def get_queryset(self):
        userid = self.request.query_params.get('userid', None)
        title = self.request.query_params.get('title', None)
        print(userid, title, 'Giderken')
        userid2 = userid
        title2 = title
        print(userid2, title2, 'Giderken2')

        print(userid2, title2, 'Gelirken')
        return Stories.objects.raw(' select s.id, s.title, ss.published '
                                       ' from Stories s '
                                       ' left join Users u on u.uuid = s.userId '
                                       ' left join story_status ss on s.uuid = ss.uuid '
                                       ' where s.userid = %s and s.title = %s ', [userid2, title2]
                                       )
        print(userid2, title2, 'Gelirken2')
        return userid2, title2





















