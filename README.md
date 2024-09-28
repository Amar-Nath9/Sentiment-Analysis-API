# Sentiment Analysis API

## Overview
The **Sentiment Analysis API** is a Python-based RESTful API developed using Flask. It allows users to upload customer reviews in CSV or XLSX format, processes these reviews using the Groq API, and performs sentiment analysis. The API returns structured JSON responses containing sentiment scores, classifying each review as positive, negative, or neutral.

## Features
- Upload customer reviews in CSV or XLSX format.
- Perform sentiment analysis on the uploaded reviews.
- Return structured sentiment scores (positive, negative, neutral) in JSON format.
- Basic error handling for file uploads and data validation.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Flask
- Pandas
- Openpyxl
- Groq API client library

## Installation

### Clone the Repository:

```bash
git clone https://github.com/Amar-Nath9/Sentiment-Analysis-API.git
cd Sentiment-Analysis-API
```
## Create a virtual environment:
```bash
python -m venv venv
```
## Activate the virtual environment:
```bash
venv\Scripts\activate
```
## Install the required packages:
```bash
pip install Flask pandas openpyxl groq

```
 OR
```bash
pip install -r requirements.txt
```
## Set your Groq API key:
```bash
set GROQ_API_KEY=your_api_key_here

```
# Running the API\
To run the API, execute the following command in your terminal:
```bash
python app.py
```
The API will start at http://127.0.0.1:5000.

## API Usage
# Upload Reviews
To upload a file containing reviews, use the following POST request:

Endpoint: http://127.0.0.1:5000/upload
Headers:
Content-Type: multipart/form-data
Form Data:
file: [Select your CSV/XLSX file]
## Example Request:
Using Postman or curl, send a POST request with the file.

```bash
curl -X POST http://127.0.0.1:5000/upload \
    -F "file=@reviews.csv"
```
## Example Response:
```json
{
    "positive": 0.76,
    "negative": 0.15,
    "neutral": 0.09
}
```
