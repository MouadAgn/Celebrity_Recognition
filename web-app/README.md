# Application Web de Reconnaissance de Célébrités

Cette application web permet de détecter des célébrités à partir d'images en utilisant un modèle de deep learning pré-entraîné.

## Structure du Projet

```
web-app/
├── app.py                  # Application Flask principale
├── requirements.txt        # Dépendances Python
├── run.bat                # Script d'exécution pour Windows
├── static/                # Fichiers statiques
│   ├── css/
│   │   └── style.css      # Styles CSS
│   ├── js/
│   │   └── main.js        # JavaScript client
│   └── uploads/           # Dossier pour les images uploadées
└── templates/
    └── index.html         # Template HTML principal
```

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Un navigateur web moderne

## Installation

1. Assurez-vous d'avoir Python installé sur votre système
2. Exécutez le script `run.bat` qui va :
   - Installer les dépendances nécessaires
   - Démarrer l'application web

## Utilisation

1. Lancez l'application et CD web-epp et exécutez `run.bat`
2. Ouvrez votre navigateur et accédez à `http://localhost:5000`
3. Cliquez sur "Sélectionner une image" pour choisir une image de célébrité
4. Cliquez sur "Analyser" pour lancer la détection
5. Le résultat s'affichera avec :
   - La célébrité détectée
   - Le niveau de confiance de la prédiction
   - Un aperçu de l'image analysée

## Fonctionnalités

- Interface utilisateur moderne et responsive
- Prévisualisation des images avant analyse
- Affichage des résultats avec niveau de confiance
- Gestion des erreurs et messages d'information
- Support des formats d'image courants (JPG, PNG, JPEG)

## Notes Techniques

- L'application utilise le modèle `face_recognition_model_transfer_learning.h5` pour la détection
- Le modèle est basé sur MobileNetV2 avec fine-tuning
- Les images sont prétraitées pour correspondre aux exigences du modèle
- L'interface utilise Bootstrap pour le design responsive

## Dépannage

Si vous rencontrez des problèmes :

1. Vérifiez que toutes les dépendances sont installées
2. Assurez-vous que le modèle et le fichier label_dict.pkl sont présents
3. Vérifiez que le port 5000 n'est pas utilisé par une autre application
4. Consultez les logs de l'application pour plus de détails 