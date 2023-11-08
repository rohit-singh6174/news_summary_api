from transformers import pipeline, BartTokenizer
from flask import Flask, request, jsonify
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize the summarization pipeline with your model
hub_model_id = "tuhia/bart-base-finetuned-BBC"
summarizer = pipeline("summarization", model=hub_model_id)
tokenizer = BartTokenizer.from_pretrained(hub_model_id)

@app.route('/summarize', methods=['POST'])
def summarize():
    input_text = request.json.get('input_text')

    if input_text:
        summarized_text = summarize_text(input_text)
        return jsonify({'summarized_text': summarized_text}), 200

    return jsonify({'error': 'Please provide input text.'}), 400

def summarize_text(text):
    # Generate a summary
    summary_ids = summarizer(text, max_length=190, min_length=50, do_sample=False)[0]['summary_text']
    return summary_ids


@app.route('/')
def home():
    print("News Alive")
    return jsonify({'summarized_text':"News Summary A Live Use /summarize POST request to sen "}), 200





if __name__ == '__main__':
    app.run(debug=True) #port 5000
