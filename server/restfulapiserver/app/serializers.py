from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import App

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        # Table campaign
        fields = ['id',
                  'title',
                  'advertiser_id',
                  'startdate',
                  'enddate',
                  'type',
                  'created_at']