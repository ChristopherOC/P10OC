from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Comment, Contributor, Issue, MyCustomUser, Project
from .permission import (AuthorOrReadComment, AuthorOrReadIssue,
                         CustomAuthorPerm)
from .serializers import (CommentSerializer, ContributorSerializer,
                          IssueSerializer, MyTokenObtainPairSerializer,
                          ProjectSerializer, UserSerialiser)


# Vue permettant l'inscription des utilisateurs
class RegisterView(generics.CreateAPIView):
    queryset = MyCustomUser.objects.all()
    serializer_class = UserSerialiser


# Vue permettant la connexion des utilisateurs
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Vue permettant les différentes opérations CRUD
# sur le model Projet
class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [CustomAuthorPerm]

    def perform_create(self, serializer):
        # Permet la création de model Projet et associe
        # l'auteur de la requête à l'auteur du projet
        author_user = self.request.user
        serializer.save(author_user_id=author_user)
        project = serializer.instance
        # Crée un nouvel objet Contributor pour l'auteur
        # du projet avec le rôle "Auteur"
        Contributor.objects.create(user=author_user, project=project,
                                   role=Contributor.AUTHOR)

    def get_queryset(self):
        # Récupère le projet filtré par son identifiant (pk)
        project = Project.objects.filter(pk=self.kwargs["pk"])
        return project


# Vue permettant les différentes opérations CRUD
# sur le model Issue
class IssueView(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, AuthorOrReadIssue]

    def perform_create(self, serializer):
        # Assigne l'auteur actuel (utilisateur authentifié)
        # au problème (issue) créé
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Récupère les problèmes (issues) filtrés par
        # l'identifiant du projet parent (project_pk)
        project = self.kwargs['project_pk']
        return Issue.objects.filter(project_id=project)

    def update(self, request, *args, **kwargs):
        # Autorise les mises à jour partielles (PATCH)
        # pour les problèmes (issues)
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

# Vue permettant les différentes opérations CRUD
# sur le model Comment
class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, AuthorOrReadComment]

    def perform_create(self, serializer):
        # Assigne l'auteur actuel (utilisateur authentifié)
        # au commentaire créé
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Récupère les commentaires filtrés par
        # l'identifiant du problème parent (issue_pk)
        project = self.kwargs['issue_pk']
        return Comment.objects.filter(issue_id=project)

    def update(self, request, *args, **kwargs):
        # Autorise les mises à jour partielles (PATCH)
        # pour les commentaires
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


# Vue permettant les différentes opérations CRUD
# sur le model Contributor
class ContributorView(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Crée un nouvel objet Contributor associé à
        # un utilisateur et un projet spécifiés
        user = MyCustomUser.objects.get(pk=self.request.POST["user"])
        project = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(user=user, project=project,
                        role=Contributor.CONTRIBUTOR)

    def get_queryset(self):
        # Récupère les contributeurs associés à
        # l'utilisateur actuel (utilisateur authentifié)
        user = self.request.user
        return Contributor.objects.filter(user=user)


# Vue pour afficher les contributeurs d'un projet
# en lecture seulement
class ProjectContributorView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Récupère les contributeurs associés à un
        # projet spécifié (project_pk)
        project_pk = self.kwargs.get('project_pk')
        print(project_pk)
        return Contributor.objects.filter(project_id=project_pk)
