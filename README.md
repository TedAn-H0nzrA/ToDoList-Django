# ToDoList - Application Django avec MySQL

## Description du projet

Une application web de gestion de tâches développée avec Django et MySQL. Cette application permet aux utilisateurs de créer, organiser et suivre leurs tâches quotidiennes avec une interface simple et intuitive.

## Technologies utilisées

- **Framework**: Django
- **Base de données**: MySQL
- **Frontend**: HTML, CSS
- **Langages**: Python

## Fonctionnalités

- Création et gestion de tâches
- Suivi des statuts (Non commencée, En cours, Terminée)
- Tableau de bord avec statistiques
- Système d'authentification des utilisateurs
- Interface responsive (compatible avec les appareils mobiles)

## Installation

### Prérequis

- Python 3.8+
- MySQL
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. Clonez le dépôt:

```bash
git clone https://github.com/TedAn-H0nzrA/ToDoList-Django.git
cd ToDoList-Django
```

2. Créez un environnement virtuel:

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

1. Installez les dépendances:

```bash
pip install -r requirements.txt
```

4. Configurez la base de données MySQL dans `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ToDoList_DB',  
        'USER': 'ToDoList_user',  
        'PASSWORD': 'todo5mdp',
        'HOST': 'localhost',
        'PORT': '3306',

    }
}
```

5. Effectuez les migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Créez un superutilisateur:

```bash
python manage.py createsuperuser
```

7. Lancez le serveur:

```bash
python manage.py runserver
```

## Accès depuis un appareil mobile (même réseau Wi-Fi)

### Lancer le serveur Django en réseau

```bash
python manage.py runserver 0.0.0.0:8000
```

### Configurer les hôtes autorisés

Dans `settings.py`, ajoutez votre IP locale:

```python
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0', 'votre_ip_locale']
```

### Accéder à l'application

1. Connectez votre téléphone au même réseau Wi-Fi que votre ordinateur
2. Dans le navigateur de votre téléphone, accédez à:

```
http://votre_ip_locale:8000
```

## Structure du projet

- `Core/` - Application principale avec les vues de base
- `Auth/` - Gestion de l'authentification
- `Tasks/` - Gestion des tâches (modèles, vues, formulaires)
- `Static/` - Fichiers statiques (CSS, JS)
- `Templates/` - Templates HTML

## Utilisation de MySQL

L'application utilise MySQL pour stocker les données des utilisateurs et des tâches, offrant:

- Persistance des données
- Requêtes rapides et efficaces
- Relations entre les différentes entités

## Résolution des problèmes courants

- Si vous ne pouvez pas accéder à l'application depuis un appareil mobile, vérifiez que votre pare-feu autorise le port 8000
- Pour les problèmes de connexion à MySQL, vérifiez vos identifiants et que le service MySQL est bien en cours d'exécution
