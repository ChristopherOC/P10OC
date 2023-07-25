from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


# Model utilisateur avec des champs supplémentaires
class MyCustomUser(AbstractUser):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'

    def __str__(self) -> str:
        return self.username


# Model de projets avec des types différents
class Project(models.Model):
    project_types = [('FE', 'Front-end'),
                     ('BE', 'Back-end'),
                     ('Android', 'Android'),
                     ('IOS', 'IOS')]

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    project_type = models.CharField(max_length=7, choices=project_types)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.RESTRICT,
                                       related_name='created_by')

    def __str__(self):
        return self.title


# Model de contributeur liés à un projet
class Contributor(models.Model):
    AUTHOR = 'AUTHOR'
    CONTRIBUTOR = 'CONTRIBUTOR'

    CHOICES = [
        (AUTHOR, 'Auteur'),
        (CONTRIBUTOR, 'Contributeur'),
    ]
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             null=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE,
                                null=True,
                                related_name='project_contributor')
    role = models.CharField(max_length=30, choices=CHOICES,
                            verbose_name='role')


# Model d'une "Issue" lié à un projet
class Issue(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='issue_author')
    assigned_users = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE,
                                       related_name='assigned_users')
    priority = models.CharField(max_length=30)
    tag = models.CharField(max_length=30)
    status = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE,
                                related_name='issues')

    def __str__(self):
        return self.title


# Model d'un commentaire lié à une "Issue"
class Comment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name="comments")
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE,
                              related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)
