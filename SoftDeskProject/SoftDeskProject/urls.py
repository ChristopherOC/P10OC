"""
URL configuration for SoftDeskProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from project.views import (CommentView, ContributorView, IssueView, LoginView,
                           ProjectContributorView, ProjectView, RegisterView)
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

router = routers.SimpleRouter(trailing_slash=True)
router.register(r"project/?", ProjectView, basename="project")

issue_router = routers.NestedSimpleRouter(router, r"project/?",
                                          lookup="project")
issue_router.register(r"issue/?", IssueView, basename="issue")

comment_router = routers.NestedSimpleRouter(issue_router,
                                            r"issue/?", lookup="issue")
comment_router.register(r"comment/?", CommentView, basename="comment")

users_router = routers.NestedSimpleRouter(router, r"project/?",
                                          lookup="project")
users_router.register(r"contributors/?", ContributorView, basename="users")

contributors_router = routers.NestedSimpleRouter(router,
                                                 r"project/?",
                                                 lookup='project')
contributors_router.register(r"project_contributors/?",
                             ProjectContributorView,
                             basename="project_contributors")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='api_register'),
    path('login/', LoginView.as_view(), name='api_login'),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path(r'', include(router.urls)),
    path(r'', include(issue_router.urls)),
    path(r'', include(comment_router.urls)),
    path(r'', include(users_router.urls)),
    path(r'', include(contributors_router.urls))
]
