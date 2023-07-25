from rest_framework import permissions


# Permet à l'auteur et aux contributeurs d'effectuer
# des actions
class CustomAuthorPerm(permissions.BasePermission):
    message = "Seul l'auteur et les contributeurs peuvent faire cela"

    def has_object_permission(self, request, view, obj):
        # Autorise les méthodes sécurisées (GET, HEAD, OPTIONS)
        # sans restriction.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Vérifie si l'utilisateur effectuant la requête est
        # l'auteur de l'objet.
        return obj.author_user_id == request.user or obj.contributors.filter(
            user=request.user).exists()


# Permet uniquement à l'auteur de modifier les champs
class AuthorOrReadIssue(permissions.BasePermission):
    message = "L'auteur seul peut modifier"

    def has_object_permission(self, request, view, obj):
        # Autorise les méthodes sécurisées (GET, HEAD, OPTIONS)
        # sans restriction.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Vérifie si l'utilisateur effectuant la requête
        # est l'auteur du problème (issue).
        return obj.author == request.user


# Permet uniquement à l'auteur du commentaire de
# modifier son message
class AuthorOrReadComment(permissions.BasePermission):
    message = "Uniquement l'auteur de ce message peut faire cela"

    def has_object_permission(self, request, view, obj):
        # Autorise les méthodes sécurisées (GET, HEAD, OPTIONS)
        # sans restriction.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Vérifie si l'utilisateur effectuant la requête
        # est l'auteur du commentaire.
        return obj.author == request.user
