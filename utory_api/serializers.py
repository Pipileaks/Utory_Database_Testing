from rest_framework import serializers
from .models import *


class AchivementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achivements
        fields = "__all__"


class ErrorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Errors
        fields = "__all__"


class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class appRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppRating
        fields = "__all__"


class PlayedstorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayedStory
        fields = "__all__"


class StorycontentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryContent
        fields = "__all__"


class StoryhistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryHistory
        fields = "__all__"


class StorystatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryStatus
        fields = "__all__"


class UserstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatus
        fields = "__all__"


class StoryidSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryContent
        fields = '__all__'


class UseridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'uuid',)

class RecentlyStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ('uuid', 'title', 'username', 'rating', 'playcount',)

class MostPlayedStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ('uuid', 'title', 'username', 'rating', 'playcount',)

class HighestRatedStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ['uuid', 'title', 'username', 'rating', 'playcount']


class MyStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyStories
        fields = ['uuid', 'published', 'title']




