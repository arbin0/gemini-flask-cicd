import os
from flask import Flask, request, jsonify, render_template_string
import google.generativeai as genai

app = Flask(__name__)

# Retrieve API key from environment variable
API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

# HTML template for the UI
html_template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generative AI</title>
</head>
<body>
    <h1>Generative AI Text Generation V:-2.0</h1>
    <form action="/generate" method="post">
        <label for="prompt">Enter your prompt:</label><br>
        <input type="text" id="prompt" name="prompt"><br><br>
        <input type="submit" value="Generate">
    </form>
    {% if response %}
        <h2>Response:</h2>
        <p>{{ response }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.form['prompt']
    try:
        response = genai.generate_text(prompt=prompt)
        response_text = response.result  # Adjust based on the actual structure of the response
        return render_template_string(html_template, response=response_text)
    except Exception as e:
        return render_template_string(html_template, response=f'Error: {str(e)}')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)
