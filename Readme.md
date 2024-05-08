
__Spam Detection Web Application with Flask__

__Overview__

This web application utilizes a Multinomial Naive Bayes classifier to detect spam msg. Users can input text data via a web form, and the application predicts whether the input text is spam or not. The classifier is trained on a dataset containing labeled messages, distinguishing between spam and non-spam (ham) msg. By leveraging text preprocessing techniques and machine learning algorithms, the application provides an efficient solution for identifying spam msg in real-time.

__Key Features__

__User-friendly web interface__: Allows users to input text data through a simple web form.

__Real-time prediction__: Provides instant predictions on whether the input text is spam or not.

__Model integration__: Integrates a trained Multinomial Naive Bayes classifier for accurate spam detection.

__Text preprocessing__: Cleans and preprocesses text data to improve prediction accuracy.

__Flask-based backend__: Utilizes Flask, a lightweight Python web framework, for handling web requests and serving predictions.


__Getting Started__

__Installation__

Clone this repository: git clone <repository-url>
Navigate to the project directory: cd text_spam_classifier

__Usage__

Ensure you have the necessary trained model files (nb_classifier_model.pkl and vocab.pkl) in the project directory.

Run the Flask application: python app.py
Open a web browser and navigate to http://localhost:5000 to access the web interface.

Enter text data into the provided form and click the "Submit" button to receive a prediction.

Technologies Used

Python

Flask

HTML/CSS (for web interface)

NLTK

Scikit-learn

Dataset

The dataset used to train the spam detection model .


__Author__ :

pradhumansharma2@gmail.com
