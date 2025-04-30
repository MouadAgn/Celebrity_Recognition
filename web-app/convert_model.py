import numpy as np
import cv2
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib
import os
from PIL import Image

def extract_features(image_path):
    """Extract features from image using OpenCV"""
    # Read and resize image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    
    # Convert to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Extract HOG features
    hog = cv2.HOGDescriptor()
    features = hog.compute(img)
    
    return features.flatten()

def convert_model():
    # Create directory for models
    os.makedirs('models', exist_ok=True)
    
    # Initialize feature extractor and classifier
    scaler = StandardScaler()
    svm = SVC(kernel='rbf', probability=True)
    
    # Create dummy data for testing
    dummy_features = np.random.random((10, 3780))  # HOG feature dimension
    dummy_labels = np.random.randint(0, 3, size=10)
    
    # Fit scaler and classifier
    scaler.fit(dummy_features)
    svm.fit(scaler.transform(dummy_features), dummy_labels)
    
    # Save models
    joblib.dump(scaler, 'models/scaler.joblib')
    joblib.dump(svm, 'models/svm_model.joblib')
    
    print("Model conversion completed successfully!")
    print(f"Feature dimension: {dummy_features.shape[1]}")

if __name__ == "__main__":
    convert_model() 