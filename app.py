from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    input_text = request.form['input_text']

    api_url = 'http://localhost:5000/summarize'
    response = requests.post(api_url, json={'input_text': input_text})

    if response.status_code == 200:
        summarized_text = response.json()['summarized_text']
        return render_template('result.html', input_text=input_text, summarized_text=summarized_text)
    else:
        return "Error processing the request", 500

if __name__ == '__main__':
    app.run(debug=True, port=8001)
