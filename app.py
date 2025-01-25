from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Configure Gemini AI
genai.configure(api_key='AIzaSyBfLgClw1r2Qd3Ps1GhOThHn_P0eOeo-tw')
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

# Selected character (can be dynamically changed later)
selected_character = "Friendly Roaster"  # Default character

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/select-character', methods=['POST'])
def select_character():
    global selected_character
    data = request.json
    selected_character = data.get("character", "Friendly Roaster")
    return jsonify({"message": "Character set successfully"})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({'response': 'No message provided'}), 400

        # Generate response using Gemini AI
        response = generate_response(user_input)
        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_response(user_input):
    """
    Generates a response using Gemini AI based on user input.
    """
    try:
        # Use the Gemini AI model to generate a response
        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        return f"An error occurred while generating a response: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
