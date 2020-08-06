# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone


class Achivements(models.Model):
    uuid = models.CharField(max_length=64, blank=True, null=True)
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=56)
    description = models.CharField(max_length=128)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'Achivements'
        verbose_name_plural = 'Achivements'

class Errors(models.Model):
    uuid = models.CharField(max_length=64, blank=True, null=True)
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    date = models.DateTimeField(default=timezone.now)
    error = models.CharField(max_length=1024)
    layer = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'Errors'
        verbose_name_plural = 'Errors'



class Users(models.Model):
    uuid = models.CharField(max_length=64)
    username = models.CharField(unique=True, max_length=32)
    email = models.CharField(max_length=64)
    signedfacebook = models.IntegerField(db_column='signedFacebook', blank=True, null=True)  # Field name made lowercase.
    signedgoogle = models.IntegerField(db_column='signedGoogle', blank=True, null=True)  # Field name made lowercase.
    signedtwitter = models.IntegerField(db_column='signedTwitter', blank=True, null=True)  # Field name made lowercase.
    signedemail = models.IntegerField(db_column='signedEmail', blank=True, null=True)  # Field name made lowercase.
    subdate = models.DateTimeField(db_column='subDate', default=timezone.now)  # Field name made lowercase.
    tutorialdone = models.IntegerField(db_column='tutorialDone', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)
    lastlogin = models.DateTimeField(db_column='lastLogin', default=timezone.now)  # Field name made lowercase.
    language = models.CharField(max_length=16, blank=True, null=True)
    pushedallowed = models.IntegerField(db_column='pushedAllowed', blank=True, null=True)  # Field name made lowercase.
    premium = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'
        verbose_name_plural = 'Users'

class AppRating(models.Model):
    uuid = models.CharField(max_length=64, blank=True, null=True)
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'app_rating'
        verbose_name_plural = 'AppRating'

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PlayedStory(models.Model):
    uuid = models.CharField(max_length=64, blank=True, null=True)
    userid = models.CharField(db_column='userId', blank=True, null=True, max_length=64)  # Field name made lowercase.
    storyid = models.IntegerField(db_column='storyId', blank=True, null=True)  # Field name made lowercase.
    rating = models.FloatField(default=0.0)
    successful = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    physicalhealth = models.IntegerField(db_column='physicalHealth', blank=True, null=True)  # Field name made lowercase.
    mentalhealth = models.IntegerField(db_column='mentalHealth', blank=True, null=True)  # Field name made lowercase.
    rollcount = models.IntegerField(db_column='rollCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'played_story'
        verbose_name_plural = 'PlayedStory'

class StoryContent(models.Model):
    uuid = models.CharField(max_length=64)
    pagenumber = models.IntegerField()
    title = models.CharField(max_length=64)
    bodytext = models.CharField(db_column='bodyText', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    phytext = models.CharField(db_column='phyText', max_length=512, blank=True, null=True)  # Field name made lowercase.
    mnttext = models.CharField(db_column='mntText', max_length=512, blank=True, null=True)  # Field name made lowercase.
    failend = models.CharField(db_column='failEnd', max_length=512, blank=True, null=True)  # Field name made lowercase.
    introcheck = models.BooleanField(db_column='introCheck', blank=True, null=True)  # Field name made lowercase.
    storyintro = models.CharField(db_column='storyIntro', max_length=512, blank=True, null=True)  # Field name made lowercase.
    sucend = models.CharField(db_column='sucEnd', max_length=512, blank=True, null=True)  # Field name made lowercase.
    pstr = models.BooleanField(db_column='pStr', blank=True, null=True)  # Field name made lowercase.
    mstr = models.BooleanField(db_column='mStr', blank=True, null=True)  # Field name made lowercase.
    pcon = models.BooleanField(db_column='pCon', blank=True, null=True)  # Field name made lowercase.
    mcon = models.BooleanField(db_column='mCon', blank=True, null=True)  # Field name made lowercase.
    pdex = models.BooleanField(db_column='pDex', blank=True, null=True)  # Field name made lowercase.
    mdex = models.BooleanField(db_column='mDex', blank=True, null=True)  # Field name made lowercase.
    pint = models.BooleanField(db_column='pInt', blank=True, null=True)  # Field name made lowercase.
    mint = models.BooleanField(db_column='mInt', blank=True, null=True)  # Field name made lowercase.
    pwis = models.BooleanField(db_column='pWis', blank=True, null=True)  # Field name made lowercase.
    mwis = models.BooleanField(db_column='mWis', blank=True, null=True)  # Field name made lowercase.
    pcha = models.BooleanField(db_column='pCha', blank=True, null=True)  # Field name made lowercase.
    mcha = models.BooleanField(db_column='mCha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'story_content'
        verbose_name_plural = 'StoryContent'

class StoryHistory(models.Model):
    storyid = models.IntegerField(db_column='storyId', blank=True, null=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleId')  # Field name made lowercase.
    revnote = models.CharField(db_column='revNote', max_length=512, blank=True, null=True)  # Field name made lowercase.
    deletenote = models.CharField(db_column='deleteNote', max_length=512, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(default=timezone.now)
    uuid = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'story_history'
        unique_together = (('id', 'roleid'),)
        verbose_name_plural = 'StoryHistory'

class StoryStatus(models.Model):
    uuid = models.CharField(max_length=64, blank=True, null=True)
    roleid = models.IntegerField(db_column='roleId', blank=True, null=True)  # Field name made lowercase.
    published = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    review = models.BooleanField(blank=True, null=True, default=False)
    seen = models.BooleanField(blank=True, null=True, default=False)
    resuming = models.BooleanField(blank=True, null=True, default=False)
    trash = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'story_status'
        verbose_name_plural = 'StoryStatus'

class UserStatus(models.Model):
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleId')  # Field name made lowercase.
    role = models.CharField(max_length=48)
    roledate = models.DateTimeField(db_column='roleDate', default=timezone.now)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_status'
        verbose_name_plural = 'UserStatus'


class Stories(models.Model):
    uuid = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=64)
    username = models.CharField(db_column='userName', max_length=32)  # Field name made lowercase.
    userid = models.CharField(db_column='userId', max_length=64)  # Field name made lowercase.
    totalpage = models.IntegerField(db_column='totalPage', blank=True, null=True)  # Field name made lowercase.
    difficulty = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=16, blank=True, null=True)
    genre = models.CharField(max_length=32, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    playcount = models.IntegerField(db_column='playCount', default=0)  # Field name made lowercase.
    datepublish = models.DateTimeField(blank=True, null=True)
    rating = models.FloatField(default=0.0)

    class Meta:
        managed = False
        db_table = 'Stories'
        verbose_name_plural = 'Stories'

class MyStories(models.Model):
    uuid = models.CharField(max_length=64, blank=True, null=True)
    roleid = models.IntegerField(db_column='roleId', blank=True, null=True)  # Field name made lowercase.
    published = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    review = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)
    resuming = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)
    title = models.CharField(max_length=64)
    playcount = models.IntegerField(db_column='playCount', default=0)
    rating = models.FloatField(default=0.0)
    username = models.CharField(max_length=32, blank=True, null=True)

