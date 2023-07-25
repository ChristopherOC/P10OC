# P10OC

### Ceci est une API Restful pour la société SoftDesk.
L'API doit respecter les directives suivantes :

Les utrilisateurs peuvent créer un compte et se connecter.
Un utilisateur peut crééer un projet, des "Issues" et des commentaires.
Selon un système  de permission, certains utilisateurs voient leurs actions restreintes pour certaines fonctionnalités.
Pour en savoir plus :

## Installation
Commencez tout d'abord par installer Python et un IDE de votre choix (PyCharm, VSCode...).

Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce répertoire:

> git clone (https://github.com/ChristopherOC/P10OC.git)

Placez-vous dans le dossier créé, créez l'environnement virtuel :

> python -m venv env

Activez le comme ceci : 

Windows :

> env\scripts\activate.bat

Linux :

> source env/bin/activate

Exécution
Pour lancer l'application, rendez-vous dans le terminal intégré de votre IDE. Entrez dans le dossier l'application avec la commande suivante :

cd softdeskproject

Lancez la commande suivante :

python manage.py runserver
