import os
from flask import Flask, render_template, request, jsonify, render_template_string
import openai
import time

# Set your OpenAI API key here
api_key = "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"  # Replace with your OpenAI API key

openai.api_key = api_key

# Initialize Flask app
app = Flask(__name__)

# Store AI response temporarily (or use a database)
latest_answer = ""

# Route for Website 1 (Question Page)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the question from the form
        user_input = request.form.get('question')

        if user_input:
            try:
                # Get AI response from OpenAI API
                chat_completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # You can use gpt-4 if you have access
                    messages=[{"role": "user", "content": user_input}]
                )
                global latest_answer
                latest_answer = chat_completion['choices'][0]['message']['content']
                print(f"AI Response: {latest_answer}")  # Debug print to check AI response
            except Exception as e:
                latest_answer = f"Error: {str(e)}"
        return render_template('index.html')  # Keep the form if no question is asked
    return render_template('index.html')  # GET request, just display the form

# Route for Website 2 (Hologram Response Page)
@app.route('/ai-response')
def ai_response():
    global latest_answer
    return render_template('index3.html', answer=latest_answer)

# You can also add a route to refresh the AI answer if you like
@app.route('/get-answer')
def get_answer():
    return jsonify({"answer": latest_answer})

if __name__ == '__main__':
    app.run()
