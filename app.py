from flask import Flask, request, jsonify
import pandas as pd
import os
from groq import Groq

# Initialize the Flask app
app = Flask(__name__)

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Groq API configuration
API_KEY = os.getenv('GROQ_API_KEY')  # Ensure your API key is set in the environment
client = Groq(api_key=API_KEY)

# Basic route for testing if the API is running
@app.route('/')
def index():
    return "Welcome to the Sentiment Analysis API"

# Helper function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle file uploads and process the reviews
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the file part is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    # Check if the file is valid
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        try:
            # Read the file into a pandas DataFrame
            if file.filename.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.filename.endswith('.xlsx'):
                df = pd.read_excel(file)

            # Ensure the file has a 'Review' column
            if 'Review' not in df.columns:
                return jsonify({"error": "'review' column not found in the file"}), 400

            # Extract the 'Review' column as a list of reviews
            reviews = df['Review'].tolist()

            

            # Perform sentiment analysis using Groq
            sentiment_result = perform_sentiment_analysis(reviews)

            # Return the sentiment analysis results as a JSON response
            return jsonify(sentiment_result)

        except Exception as e:
            # Catch any errors during file processing and return a 500 error
            return jsonify({"error": str(e)}), 500

    else:
        return jsonify({"error": "Invalid file format. Only CSV or XLSX allowed."}), 400

# Function to perform sentiment analysis using the Groq API
def perform_sentiment_analysis(reviews):
    positive, negative, neutral = 0, 0, 0
    total_reviews = len(reviews)

    for review in reviews:
        try:
            # Prepare the payload for the Groq API request
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": review,
                    }
                ],
                model="llama3-8b-8192"  # Replace with the actual model you are using
            )

            # Parse response for sentiment analysis (assuming the Groq model gives positive/negative/neutral analysis)
            response_content = response.choices[0].message.content

            # (Note: Customize how you interpret the response here based on Groq's API structure)
            if "positive" in response_content.lower():
                positive += 1
            elif "negative" in response_content.lower():
                negative += 1
            else:
                neutral += 1

        except Exception as e:
            # If there's an error with Groq API, return the error message
            return {"error": f"Error analyzing review: {str(e)}"}

    # Return the aggregated sentiment results
    return {
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }

# Run the Flask app when this file is executed
if __name__ == '__main__':
    app.run(debug=True)
