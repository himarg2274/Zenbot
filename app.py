from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Predefined mood keywords and responses
mood_keywords = {
    "hi":"hi how are you? How can i help you",
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
    "anxious": "Feeling anxious can be overwhelming, but there are ways to manage it. Let's try some deep breathing together or talk about what's making you anxious."
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Retrieve the JSON data from the request
        user_input = request.json.get('message')  # Expecting JSON with 'message' key
        print("User input:", user_input)

        if not user_input:
            return jsonify({'response': 'No message provided'}), 400

        # Scan the user's input for mood-related keywords and provide a response
        response = scan_input_for_mood(user_input)
        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def scan_input_for_mood(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if any keyword exists in the user's input
    for mood, response in mood_keywords.items():
        if mood in user_input:
            return response

    # Default response if no mood-related keyword is found
    return "It’s okay to feel however you're feeling right now. Let’s talk about it together."


def daily_affirmation():
    affirmations = [
        "You are enough, just as you are.",
        "Every day is a new opportunity for growth.",
        "You have the strength to overcome any challenge.",
        "You are worthy of love and kindness."
    ]
    return random.choice(affirmations)


def save_mood_log(mood):
    with open('mood_log.txt', 'a') as file:
        file.write(f"Mood: {mood}\n")


def view_mood_log():
    try:
        with open('mood_log.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "No mood log found."


def cognitive_restructuring():
    print("Let's identify a negative thought you are having.")
    negative_thought = input("What negative thought is on your mind right now? ")
    print(f"Now, let's challenge that thought. Is there evidence that this thought is 100% true?")
    response = input("Yes/No: ")

    if response.lower() == "no":
        print("Great! You are challenging your negative thought. Now, let's reframe it. What is a more positive way to view the situation?")
        positive_thought = input("Enter your positive thought: ")
        print(f"That's a great reframe! Keep practicing positive thinking.")
    else:
        print("It’s okay if you still feel this way. Sometimes, it helps to take a deep breath and reflect.")


def show_mental_health_resources():
    resources = {
        "National Helpline": "1-800-123-4567",
        "Crisis Text Line": "Text HOME to 741741",
        "Online Therapy": "www.therapy.com",
    }
    for resource, contact in resources.items():
        print(f"{resource}: {contact}")


def mindfulness_breathing():
    print("Let's do a mindfulness breathing exercise.")
    print("Sit in a comfortable position. Close your eyes if you'd like.")
    input("Press Enter to begin...")

    print("Take a deep breath in... Hold it for 3 seconds... Now, exhale slowly...")
    input("Press Enter when ready for the next breath...")
    print("Great! Keep breathing deeply, and focus on the present moment.")


def journal_prompt():
    prompts = [
        "What made you feel good today?",
        "What was the hardest part of your day?",
        "How are you feeling right now? Can you describe your emotions?",
        "What are you grateful for today?"
    ]
    print("Here's your journaling prompt for today:")
    print(random.choice(prompts))


def thought_record():
    thought = input("What negative thought are you having right now? ")
    alternative = input("What is a more positive or realistic way to view this? ")
    with open("thought_log.txt", "a") as file:
        file.write(f"Negative thought: {thought}\nReframe: {alternative}\n\n")
    print("Great job! You've successfully reframed your thought.")


def log_mood():
    mood = input("How are you feeling today? (happy, sad, anxious, etc.): ")
    with open("mood_log.txt", "a") as file:
        file.write(f"User's mood: {mood}\n")
    print(f"Thank you for sharing! Your mood has been logged.")


def breathing_exercise():
    print("Let's do a quick breathing exercise. Follow these steps:")
    print("1. Breathe in deeply for 4 seconds...")
    print("2. Hold your breath for 4 seconds...")
    print("3. Breathe out slowly for 4 seconds...")
    print("Repeat 5 times to feel more relaxed.")


def get_therapy_response(emotion):
    responses = {
        "sad": "I'm sorry you're feeling sad. Try taking a moment to breathe deeply and focus on something you're grateful for.",
        "anxious": "It might help to practice deep breathing or take a walk. Remember, this moment will pass.",
        "stressed": "Stress is tough. Try writing down your worries, and see if you can break them down into smaller, more manageable tasks."
    }
    return responses.get(emotion.lower(), "It's okay not to have the right words. Take care of yourself.")


if __name__ == '__main__':
    app.run(debug=True)
