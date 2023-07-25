from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Comment, Contributor, Issue, MyCustomUser, Project


# Obtention du TokenJWT
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


# Sérialiseur du model MyCustomUser
class UserSerialiser(ModelSerializer):
    class Meta:
        model = MyCustomUser
        # Définition des champs à sérialiser
        fields = ['id', 'username', 'first_name', 'last_name',
                  'password', 'email']

    def create(self, verified_data):
        # Permet la création de nouvel utilisateur
        user = MyCustomUser.objects.create(
            username=verified_data['username'],
            first_name=verified_data['first_name'],
            last_name=verified_data['last_name'],
            email=verified_data['email']
        )
        # Définit le mot de passe et enregistre
        # l'utilisateur dans la base de donnée
        user.set_password(verified_data['password'])
        user.save()

        return user


# Sérialiseur du model projet
class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        # Définition des champs à sérialiser
        fields = ['title', 'description', 'project_type', 'author_user_id']


# Sérialiseur du model Issue
class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        # Définition des champs à sérialiser
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "status",
            "project",
            "author_id",
            "assigned_users",
            "created_time"
        ]


# Sérialiseur du model comment
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        # Définition des champs à sérialiser
        fields = ["id", "description", "author", "issue", "created_time"]


# Sérialiseur du model contributor
class ContributorSerializer(ModelSerializer):
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = Contributor
        # Définition des champs à sérialiser
        fields = ["id", "user", "project", "role", "user_details"]

    def get_user_details(self, obj):
        # Récupère l'utilisateur lié au contributeur
        # et sérialise ses données
        user = MyCustomUser.objects.get(pk=obj.user_id)
        user_serializer = UserSerialiser(user)
        return user_serializer.data
