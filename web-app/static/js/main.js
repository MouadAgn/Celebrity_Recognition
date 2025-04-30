document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const imageUpload = document.getElementById('imageUpload');
    const previewImage = document.getElementById('previewImage');
    const resultSection = document.getElementById('resultSection');
    const errorSection = document.getElementById('errorSection');
    const predictionResult = document.getElementById('predictionResult');
    const confidenceResult = document.getElementById('confidenceResult');

    // Vérifier le type de fichier avant l'upload
    imageUpload.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (file) {
            console.log('Type de fichier:', file.type);
            console.log('Nom du fichier:', file.name);
            
            // Vérifier le type MIME
            if (!file.type.match('image.*')) {
                errorSection.textContent = 'Veuillez sélectionner une image.';
                errorSection.style.display = 'block';
                resultSection.style.display = 'none';
                return;
            }

            const reader = new FileReader();
            reader.onload = function(e) {
                previewImage.src = e.target.result;
                resultSection.style.display = 'none';
                errorSection.style.display = 'none';
            }
            reader.readAsDataURL(file);
        }
    });

    // Gérer la soumission du formulaire
    uploadForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const file = imageUpload.files[0];
        if (!file) {
            errorSection.textContent = 'Veuillez sélectionner une image.';
            errorSection.style.display = 'block';
            return;
        }

        console.log('Envoi du fichier:', file.name, 'Type:', file.type);
        
        const formData = new FormData();
        formData.append('file', file);

        // Afficher le loader
        const submitButton = uploadForm.querySelector('button[type="submit"]');
        const originalButtonText = submitButton.textContent;
        submitButton.disabled = true;
        submitButton.textContent = 'Analyse en cours...';

        // Envoyer la requête
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            console.log('Status:', response.status);
            return response.json();
        })
        .then(data => {
            console.log('Réponse reçue:', data);
            if (data.error) {
                throw new Error(data.error);
            }
            
            // Afficher les résultats
            predictionResult.textContent = `Célébrité détectée : ${data.prediction}`;
            confidenceResult.textContent = `Confiance : ${(data.confidence * 100).toFixed(2)}%`;
            previewImage.src = `data:image/jpeg;base64,${data.image}`;
            resultSection.style.display = 'block';
            errorSection.style.display = 'none';
        })
        .catch(error => {
            console.error('Erreur:', error);
            errorSection.textContent = error.message;
            errorSection.style.display = 'block';
            resultSection.style.display = 'none';
        })
        .finally(() => {
            // Réinitialiser le bouton
            submitButton.disabled = false;
            submitButton.textContent = originalButtonText;
        });
    });
}); 