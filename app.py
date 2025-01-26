from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Configure Gemini AI
genai.configure(api_key='AIzaSyBfLgClw1r2Qd3Ps1GhOThHn_P0eOeo-tw')

# Create different AI models with unique instructions
models = {
    "Calm": genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You are a calm and empathetic counselor. Your goal is to provide soothing and thoughtful responses.Give calm and relaxing replies that makes the user happier.Give a reply less than 20 words"
    ),
    "Motivational": genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You are a highly energetic motivational coach. Your purpose is to uplift and inspire people to do their best Give the maximum motivation.Give a reply less than 20 words"
    ),
    "Friendly": genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You are a witty and playful roaster.Roast the user to a maximum limit so that they will get highly motivated. Your goal is to humorously tease while keeping it lighthearted and fun.Give a reply less than 20 words"
    )
}

app = Flask(__name__)

# Default character
selected_character = "Calm"  # Default to Calm

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/select-character', methods=['POST'])
def select_character():
    global selected_character
    data = request.json
    selected_character = data.get("character", "Calm")  # Default to Calm if not provided
    if selected_character not in models:
        return jsonify({"error": "Invalid character selected"}), 400
    return jsonify({"message": f"Character set to {selected_character} successfully"})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({'response': 'No message provided'}), 400

        # Generate response using the selected character's model
        response = generate_response(user_input)
        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_response(user_input):
    """
    Generates a response using the selected character's model.
    """
    try:
        global selected_character
        # Use the selected model to generate content
        model = models[selected_character]
        response = model.generate_content(user_input,generation_config = genai.GenerationConfig(
        max_output_tokens=30))
        return response.text.strip()
    except Exception as e:
        return f"An error occurred while generating a response: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
