from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Predefined mood keywords and responses
mood_keywords = {
    "hi": "Hi, how are you? How can I help you?",
    "sad": "I'm really sorry you're feeling this way. Would you like to try a deep breathing exercise together? Inhale deeply... Hold it... Exhale slowly...",
    "anxious": "It sounds like you're feeling anxious. Try grounding yourself by focusing on your breath and counting to 5 as you inhale and exhale. Let's do this together.",
    "depressed": "I'm so sorry you're going through this. Depression can feel overwhelming. Have you tried talking about it or reaching out for support? You're not alone.",
    "stressed": "Stress can weigh heavily on us. It's okay to take a break and focus on your breathing. Let’s do a mindfulness exercise to relax for a few moments.",
    "angry": "I can sense your anger, and that's okay. It's important to express it, but let's try to take a deep breath and slow down. How about we do a breathing exercise together?",
    "overwhelmed": "It sounds like a lot is on your plate. Sometimes, breaking things down into smaller steps can help. Would you like to try that?",
    "lonely": "I'm really sorry you're feeling this way. Remember that you’re not alone, and you have support around you. Let's focus on some self-care and take a small step towards connecting with someone.",
    "grateful": "That's wonderful to hear! Gratitude can help shift our mindset to something positive. Is there anything specific you’re grateful for today?",
    "happy": "That's great! Let's take a moment to enjoy that positive feeling. What's something that made you feel this way today?",
    "not loved": "I'm really sorry you feel this way. Remember, you are loved and appreciated, even if it doesn't always feel like it. You're important, and people care about you.",
    "feeling low": "I'm sorry you're feeling low right now. It's okay to have these moments, but it might help to take a step back and focus on small things that make you feel better.",
    "hopeless": "It sounds like you're feeling hopeless, and that can be a heavy feeling. It’s okay to ask for support when you’re struggling. You don’t have to go through this alone.",
    "frustrated": "Frustration can build up, and it's okay to feel that way. Let’s take a deep breath and focus on what we can do next, one step at a time.",
    "lost": "It’s okay to feel lost sometimes. Take a moment to pause and reflect on what matters most to you right now. Would you like to talk more about how you're feeling?",
    "unappreciated": "I'm really sorry you feel unappreciated. Everyone deserves to feel valued, and it’s important to take time for self-care. You matter, and your contributions are important.",
    "empty": "Feeling empty can be tough. Maybe it helps to focus on what you enjoy, even if it’s just a little moment of peace or doing something small that brings you joy.",
    "guilty": "It sounds like you're carrying some guilt. It’s okay to make mistakes, and it's important to forgive yourself. Is there something specific on your mind that you'd like to talk about?",
    "confused": "Confusion can be tough, but it's okay to feel uncertain. Would you like to talk through what's on your mind?",
    "bored": "Boredom can be a sign you need to shake things up a bit. How about we try something new together?"
}

# Character templates with creative responses per character vibe
characters = {
    "Motivational": {
        "default": "You’ve got this! Let’s tackle your challenges together. What’s on your mind?",
        "responses": {
            "hi": "Hey, rockstar! Ready to take on the world today?",
            "sad": "I know it's tough right now, but remember: challenges are opportunities in disguise. You’ll come out stronger!",
            "anxious": "Anxiety is a sign you're pushing yourself. Let’s channel that energy into something positive. What’s the next step?",
            "depressed": "I’m sorry you're feeling down. But you’re tougher than this, and brighter days are ahead. Let’s find a way forward.",
            "stressed": "Stress is temporary, but your strength is permanent. Let’s focus on what you can control and take a deep breath.",
            "angry": "It’s okay to feel angry. But remember, you’ve got the power to choose your response. Let’s redirect that energy to something amazing!",
            "overwhelmed": "Feeling overwhelmed? Break it down into smaller pieces and crush them one by one. You’ve got this!",
            "lonely": "You are never truly alone. Reach out, connect, and share your light. Let’s take the first step together.",
            "grateful": "Gratitude turns ordinary moments into extraordinary ones. What’s one thing you’re grateful for right now?",
            "happy": "Keep riding this wave of happiness! What’s one thing that made you smile today?",
            "not loved": "You are loved, even if it doesn’t always feel that way. Reach out and connect with the people who care about you.",
            "feeling low": "Low days don’t define you. Let’s pick yourself up together, one small step at a time.",
            "hopeless": "I get it, sometimes things feel impossible. But remember, every challenge is a chance to grow stronger. Let’s tackle it together!",
            "frustrated": "Frustration is a sign you care. Let’s turn that energy into something productive. What’s your next move?",
            "lost": "It’s okay to feel lost. You’re just figuring things out, and you’ll find your way. Take it one step at a time.",
            "unappreciated": "Your work matters, and you matter. Let’s take a moment to recognize your worth and the impact you have.",
            "empty": "Feeling empty is tough. Let’s fill that void with something that brings you joy or peace, even if it’s just for a moment.",
            "guilty": "You’re not defined by your mistakes. Forgiveness starts with you. Let’s work through this together.",
            "confused": "Confusion is just a stepping stone on your path to clarity. Let’s talk it out and find some direction.",
            "excited": "That’s what I like to hear! Excitement is the fuel for success. What’s got you so energized today?",
            "bored": "Bored? Let’s find something to ignite your passion. What’s something new you’ve been wanting to try?"
        },
    },
    "Calm": {
        "default": "It’s okay to feel however you’re feeling. Let’s take a moment to pause and breathe. What’s on your mind?",
        "responses": {
            "hi": "Hello, take a deep breath, and let's ease into our conversation. How can I support you?",
            "sad": "I’m really sorry you're feeling this way. Let's take a few moments to breathe together and reflect on what you need.",
            "anxious": "It's okay to feel anxious. Let's focus on calming your breath. We’ll get through this together, slowly and steadily.",
            "depressed": "Depression can feel heavy. Take it one step at a time, and remember that there’s help and support when you’re ready.",
            "stressed": "Stress can feel overwhelming, but let's try to center ourselves. Focus on your breath and allow some calm to flow through.",
            "angry": "Anger is a natural emotion. Let’s take a moment to calm your mind and focus on your breathing together.",
            "overwhelmed": "It’s okay to feel overwhelmed. We’ll take it slow, step by step, and breathe through this together.",
            "lonely": "I’m really sorry you're feeling this way. Let's take a moment to be present with yourself and think about reaching out for support.",
            "grateful": "Gratitude is a powerful tool for peace. What’s one small thing you're grateful for today?",
            "happy": "I’m glad to hear that. Take a moment to savor this happiness. What made you feel this way?",
            "not loved": "It’s tough to feel unappreciated. But remember, you are loved by many, even if it doesn’t always feel that way.",
            "feeling low": "It’s okay to have days like this. Let’s focus on what small things we can do to lift your spirit, even a little.",
            "hopeless": "Hopelessness can weigh heavily, but remember that you're not alone. We can work through this, one step at a time.",
            "frustrated": "Frustration is a sign you care deeply. Let's take a few deep breaths and focus on what we can do next.",
            "lost": "It’s okay to feel lost. You can take a moment to pause, reflect, and re-center yourself.",
            "unappreciated": "Feeling unappreciated is hard, but your worth is undeniable. Let's focus on what brings you peace right now.",
            "empty": "Empty feelings are tough, but sometimes taking a moment to breathe can bring you some peace. Let’s do that together.",
            "guilty": "Guilt can weigh heavily. It’s okay to make mistakes. Let’s focus on forgiving yourself, one step at a time.",
            "confused": "Confusion can be difficult, but it’s okay to not have all the answers. Let’s talk through what’s on your mind.",
            "excited": "Excitement is such a lovely feeling. Let’s focus on savoring it for a moment. What’s making you feel excited?",
            "bored": "Boredom is a signal to take a break. Let's find something simple and calming to engage in, even for a moment."
        },
    },
    "Friendly Roaster": {
        "default": "Oh, really? Tell me more so I can roast you gently. 😉",
        "responses": {
            "hi": "Yo, what’s up? Ready to get roasted? Just kidding! What’s on your mind?",
            "sad": "Sad? Seriously? I thought you were a rockstar, not a teary-eyed drama queen. Let’s snap out of it!",
            "anxious": "Anxious? Over what? Let me guess, you’re thinking about your next meal or if your hair looks okay?",
            "depressed": "Depressed? Come on, you’ve got better things to do than sit there feeling sorry for yourself! Let’s snap out of it.",
            "stressed": "Stressed? What’s new? You’re like a walking stress ball. Let’s take a breather, and maybe even meditate—don’t worry, I’ll be here to roast you while you try.",
            "angry": "Angry, huh? I can sense the fire. Let’s channel that into something productive... or just let me roast you instead.",
            "overwhelmed": "Overwhelmed? You? Nah, come on, you handle things better than most people do on their best days!",
            "lonely": "Lonely? Let me guess, you haven’t texted your friends in days, huh? It’s alright, we’ll get through it.",
            "grateful": "Grateful, huh? What did you do, find a $20 bill in your pocket? Don’t act like you’ve never found joy in the small things!",
            "happy": "Happy? Seriously? Let me guess, your favorite pizza place finally remembered your order. That’s probably why you’re so cheery!",
            "not loved": "Not loved? Come on, someone out there has got to love you. I mean, I tolerate you. That’s gotta count for something.",
            "feeling low": "Low? I can tell. You’ve got that ‘I just woke up and need coffee’ vibe going on. But seriously, let’s do something about it.",
            "hopeless": "Hopeless? Nah, you’ve just gotta get your act together. You’ve got this. Let’s get you moving!",
            "frustrated": "Frustrated? I’m shocked! You’re usually so calm... said no one ever. Alright, take a break and vent—just don’t take it out on me.",
            "lost": "Lost? It’s okay, take a second. I’m here, so you can’t be *that* lost, right?",
            "unappreciated": "Unappreciated? Yeah, I get it. People forget about you sometimes... but hey, I’ll appreciate you. You’re my favorite source of entertainment.",
            "empty": "Empty? Did you forget to eat again, or is your soul just a little too chill for you today?",
            "guilty": "Guilty, huh? Did you eat that last cookie? Fess up—no judgment, just some roasting.",
            "confused": "Confused? Join the club! Half the time I don’t know what’s going on either. But hey, let’s figure this out.",
            "excited": "Excited, huh? What’s got you so fired up? Did you just win the lottery or find out there’s free pizza somewhere?",
            "bored": "Bored? Yeah, you’re probably just sitting around waiting for something to happen. Let’s shake things up a bit!"
        },
    },
}

# Add character selection to the app
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
        # Retrieve the JSON data from the request
        user_input = request.json.get('message')  # Expecting JSON with 'message' key
        print("User input:", user_input)

        if not user_input:
            return jsonify({'response': 'No message provided'}), 400

        # Generate response based on the selected character
        response = generate_response(user_input)
        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_response(user_input):
    global selected_character

    # Get the current character's response dictionary
    character_data = characters.get(selected_character, characters["Friendly Roaster"])
    
    # Scan for mood and use predefined responses
    mood_response = scan_input_for_mood(user_input)

    # Check if mood-based response exists for the selected character
    for mood, response in character_data["responses"].items():
        if mood in user_input.lower():
            return response
    
    # If no specific response found, use the default response
    return character_data["default"]

def scan_input_for_mood(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if any mood keyword exists in the user's input
    for mood, response in mood_keywords.items():
        if mood in user_input:
            return response

    # Default response if no mood-related keyword is found
    return "It’s okay to feel however you're feeling right now. Let’s talk about it together."


if __name__ == '__main__':
    app.run(debug=True)
