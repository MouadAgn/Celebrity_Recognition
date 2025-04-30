from flask import Flask, request, jsonify, render_template
import numpy as np
import cv2
import pickle
import joblib
from PIL import Image
import io

app = Flask(__name__)

# Charger les modèles
def load_models():
    try:
        model = joblib.load('celebrity_model.joblib')
        scaler = joblib.load('feature_scaler.joblib')
        with open('label_dict.pkl', 'rb') as f:
            label_dict = pickle.load(f)
        return model, scaler, label_dict
    except Exception as e:
        print(f"Erreur lors du chargement des modèles: {str(e)}")
        return None, None, None

# Préparer l'image pour la prédiction
def preprocess_image(image):
    # Convertir en niveaux de gris
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Redimensionner à 224x224
    resized = cv2.resize(gray, (224, 224))
    # Normaliser
    normalized = resized / 255.0
    # Aplatir
    flattened = normalized.flatten()
    return flattened

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier envoyé'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Aucun fichier sélectionné'})
    
    try:
        # Charger les modèles
        model, scaler, label_dict = load_models()
        if model is None:
            return jsonify({'error': 'Erreur lors du chargement des modèles'})
        
        # Lire l'image
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        img_array = np.array(img)
        
        # Préparer l'image
        processed_image = preprocess_image(img_array)
        
        # Normaliser les features
        features_scaled = scaler.transform([processed_image])
        
        # Faire la prédiction
        prediction = model.predict(features_scaled)[0]
        probabilities = model.predict_proba(features_scaled)[0]
        
        # Préparer les résultats
        results = {
            'prediction': label_dict[prediction],
            'confidence': float(probabilities[prediction]),
            'all_probabilities': {
                label_dict[i]: float(prob) 
                for i, prob in enumerate(probabilities)
            }
        }
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True) 