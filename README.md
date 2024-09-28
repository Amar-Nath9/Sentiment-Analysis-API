<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<h1>Sentiment Analysis API</h1>

<h2>Overview</h2>
<p>The <strong>Sentiment Analysis API</strong> is a Python-based RESTful API developed using Flask. It allows users to upload customer reviews in CSV or XLSX format, processes these reviews using the Groq API, and performs sentiment analysis. The API returns structured JSON responses containing sentiment scores, classifying each review as <strong>positive</strong>, <strong>negative</strong>, or <strong>neutral</strong>.</p>

<h2>Features</h2>
<ul>
    <li>Upload customer reviews in CSV or XLSX format.</li>
    <li>Perform sentiment analysis on the uploaded reviews.</li>
    <li>Return structured sentiment scores (positive, negative, neutral) in JSON format.</li>
    <li>Basic error handling for file uploads and data validation.</li>
</ul>

<h2>Prerequisites</h2>
<p>Before you begin, ensure you have the following installed:</p>
<ul>
    <li>Python 3.x</li>
    <li>Flask</li>
    <li>Pandas</li>
    <li>Openpyxl</li>
    <li>Groq API client library</li>
</ul>

<h2>Installation</h2>
<ol>
    <li><strong>Clone the Repository:</strong>
        <pre>
git clone https://github.com/Amar-Nath9/Sentiment-Analysis-API.git
cd Sentiment-Analysis-API
        </pre>
    </li>

    <li><strong>Create a Virtual Environment:</strong>
        <ul>
            <li><strong>On Windows:</strong>
                <pre>
python -m venv venv
venv\Scripts\activate
                </pre>
            </li>
            <li><strong>On macOS/Linux:</strong>
                <pre>
python3 -m venv venv
source venv/bin/activate
                </pre>
            </li>
        </ul>
    </li>

    <li><strong>Install Dependencies:</strong>
        <pre>
pip install Flask pandas openpyxl groq
        </pre>
    </li>

    <li><strong>Generate Groq API Key:</strong>
        <p>Visit <a href="https://console.groq.com/keys">Groq API Key Generation</a> and generate your API key.</p>
    </li>

    <li><strong>Set Your Groq API Key:</strong>
        <ul>
            <li><strong>On Windows:</strong>
                <pre>
set GROQ_API_KEY=your_api_key_here
                </pre>
            </li>
            <li><strong>On macOS/Linux:</strong>
                <pre>
export GROQ_API_KEY=your_api_key_here
                </pre>
            </li>
        </ul>
    </li>
</ol>

<h2>Running the API</h2>
<ol>
    <li><strong>Start the Flask Application:</strong>
        <pre>
python app.py
        </pre>
    </li>
    <li>The API will be available at: <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>.</li>
</ol>

<h2>API Usage</h2>
<h3>Upload Reviews</h3>
<p>To upload a file containing reviews, use the following POST request:</p>
<ul>
    <li><strong>Endpoint:</strong> <code>http://127.0.0.1:5000/upload</code></li>
    <li><strong>Method:</strong> <code>POST</code></li>
    <li><strong>Headers:</strong>
        <ul>
            <li><code>Content-Type: multipart/form-data</code></li>
        </ul>
    </li>
    <li><strong>Form Data:</strong>
        <ul>
            <li><code>file</code>: [Select your CSV/XLSX file]</li>
        </ul>
    </li>
</ul>

<h3>Example</h3>
<h4>Request:</h4>
<pre>
curl -X POST http://127.0.0.1:5000/upload \
-F "file=@reviews.csv" \
-H "Content-Type: multipart/form-data"
</pre>

<h4>Sample Input File (<code>reviews.csv</code>):</h4>
<table>
    <thead>
        <tr>
            <th>Review</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>The product was amazing!</td>
        </tr>
        <tr>
            <td>Very disappointing quality.</td>
        </tr>
        <tr>
            <td>It was okay, nothing special.</td>
        </tr>
    </tbody>
</table>

<h4>Response:</h4>
<pre>
{
  "positive": 1,
  "negative": 1,
  "neutral": 1
}
</pre>

<h3>Error Handling</h3>
<ul>
    <li><strong>No file provided:</strong>
        <pre>
{
  "error": "No file provided"
}
        </pre>
        Status Code: <code>400 Bad Request</code>
    </li>
    <li><strong>Empty file submitted:</strong>
        <pre>
{
  "error": "No selected file"
}
        </pre>
        Status Code: <code>400 Bad Request</code>
    </li>
    <li><strong>Invalid file format:</strong>
        <pre>
{
  "error": "Invalid file format. Only CSV or XLSX allowed."
}
        </pre>
        Status Code: <code>400 Bad Request</code>
    </li>
    <li><strong>Missing 'Review' column:</strong>
        <pre>
{
  "error": "'Review' column not found in the file"
}
        </pre>
        Status Code: <code>400 Bad Request</code>
    </li>
</ul>

<h2>Conclusion</h2>
<p>This <strong>Sentiment Analysis API</strong> provides a simple and efficient solution to analyze customer review sentiments. Using Flask, Pandas, and the Groq API, it delivers quick and structured feedback on review sentiments.</p>

</body>
</html>
