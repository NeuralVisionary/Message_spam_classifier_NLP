from flask import Flask, request, render_template, jsonify
import re
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import joblib

# Load the trained model
loaded_nb_classifier = joblib.load('nb_classifier_model.pkl')

# Initialize Flask app
app = Flask(__name__)

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    text = ' '.join(filtered_words)
    return text

# Load vocabulary from training data
with open('vocab.pkl', 'rb') as f:
    vocab = joblib.load(f)

# Initialize a new CountVectorizer with the loaded vocabulary
vectorizer = CountVectorizer(vocabulary=vocab)

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for form submission
@app.route('/predict', methods=['POST'])
def predict():
    # Get text from form submission
    text = request.form['text']
    
    # Preprocess the text
    preprocessed_text = preprocess_text(text)
    
    # Vectorize the preprocessed text
    text_vec = vectorizer.transform([preprocessed_text])

    # Make predictions using the loaded model
    prediction = loaded_nb_classifier.predict(text_vec)

    # Return the predicted label as JSON response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
