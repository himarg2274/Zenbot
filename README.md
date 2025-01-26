# ZenBot


## A web application that offers mental health support by analyzing user input


### Team Name: Brainy Bunch


### Team Members
- Member 1: Hima Rose George - Saintgits College Of Engineering
- Member 2: Aleesha Mariam Sabu - Saintgits College Of Engineering
- Member 3: Eunice Freeda T - Saintgits College Of Engineering

### Hosted Project Link
https://zenbot-1.onrender.com/

### Project Description
The chatbot platform, accessible through a website, features three unique character bots—Calm, Motivational, and Friendly Roaster. Depending on the user's input, the bot adapts its response to provide personalized support. The Calm bot offers soothing, reassuring responses, the Motivational bot gives uplifting and encouraging advice, and the Friendly Roaster adds a touch of humor with light-hearted roasts, all tailored to the user's emotional state.

### The Problem statement
In a world where people often struggle with feelings of loneliness and isolation, having someone to talk to can make a significant difference. However, not everyone has access to supportive listeners at critical moments. Whether it’s due to social stigma, busy schedules, or difficulty finding someone they trust, people often feel isolated with no outlet to share their thoughts and emotions. This lack of connection can lead to increased stress, anxiety, and even depression.

### The Solution
ZenBot aims to bridge this gap by providing a compassionate, AI-driven conversational companion that adapts to the user’s emotional needs, offering personalized interactions, empathetic responses, and constructive guidance to improve emotional well-being. ZenBot keeps users engaged by offering conversations tailored to their mood and preferences. It features dynamic personas like calm, motivational, or humorous styles to suit user needs. Its 24/7 availability ensures users always have someone to talk to.

## Technical Details
### Technologies/Components Used
For Software:
- Python, HTML, CSS, JavaScript
- Flask (Backend)
- google-generativeai, Fetch API (JavaScript)
- Gunicorn, Git/GitHub, Visual Studio Code (VS Code), Browser



### Implementation
For Software:
# Installation
git clone https://github.com/yourusername/zenbot.git

# Run
python app.py

### Project Documentation
For Software:
Project Overview: ZenBot is an AI-driven chatbot designed to provide an emotionally intelligent and personalized conversational experience. It adapts to different user needs, offering responses in various styles such as calm, motivational, or friendly roasting, making it an engaging companion for users seeking conversation or emotional support.

Main Features:

    Character Selection: Users can select one of three personalities (Calm, Motivational, Friendly) to customize their experience.
    Real-time Chat: The chatbot responds in real-time based on user input.
    Interactive Frontend: Dynamic interaction through a clean and user-friendly interface with the option to chat with ZenBot.
    Flexible Backend: The Flask-based backend handles routing, integrates with the Google Gemini AI API, and serves the responses.

Functionality:

    Chat: Users send messages, and ZenBot generates responses based on the selected character.
    Character Update: Users can change the character mid-session, and ZenBot will adapt its responses accordingly.

Key Routes:

    /: Displays the main interface where users can select their character and start chatting.
    /select-character: Endpoint to set the selected character based on user input (via POST).
    /chat: Handles sending user messages and generating AI responses (via POST).

Folder Structure:

    app.py: Main application file running the Flask server and handling routes.
    templates/index.html: Frontend HTML file where the user interface is rendered.
    static/styles.css: Styling for the ZenBot web interface.
    static/scripts.js: JavaScript code that handles character selection, message sending, and dynamic updates to the chat interface.
    requirements.txt: File containing all the Python dependencies for the project (Flask, google-generativeai, etc.).
# Screenshots 
![Screenshot (1)]![ss1]![image](https://github.com/user-attachments/assets/cb96ca97-770c-4400-ad8c-8f7a6e48ffa0)
 Welcome page

![image](https://github.com/user-attachments/assets/594c5968-0aa7-416e-9551-17d184e2aa81)

It enables the user to choose the character of the bot they want to talk to.

!![Screenshot (2)]![image](https://github.com/user-attachments/assets/4ea305c9-69ac-4eca-b64d-b5873ad07daa)


It is an interface where we are talking to calm zenbot

!![Screenshot (3)](https://github.com/user-attachments/assets/0bf5576f-94eb-49a4-8ab9-7e5f738e0b13)
It is an interface where we are talking to Friendly roaster zenbot

# Diagrams
Welcome Page
    |
    |-- User clicks "Start"
    V
Character Selection Page
    |
    |-- User selects a character (Calm, Motivational, Friendly)
    |-- Sends selection to /select-character endpoint
    V
Chat Interface
    |
    |-- User types a message and clicks "Send"
    |-- Sends message to /chat endpoint
    |
    |-- Backend processes message:
    |   - Retrieves selected character
    |   - Generates AI response using the character model
    |
    |-- Response is returned to frontend
    |-- Chat interface displays bot response
End


# Build Photos
![image](https://github.com/user-attachments/assets/03017d83-7dc5-44e0-ae92-1c1fc9d9ec7c)
Our team(Brainy Bunch)

[Build]
To build your application, start by setting up the backend using Flask, ensuring all required packages like `Flask` and `google-generativeai` are installed. Place your backend code (`app.py`) in the root directory and ensure it includes routes for `/`, `/select-character`, and `/chat`. For the frontend, save the provided HTML in the `templates/` folder and CSS/JavaScript files in the `static/` folder, ensuring the files are correctly linked using Flask's `url_for` function. Test the workflow locally to verify that clicking "Start" redirects to the character selection page, character choices are sent to the `/select-character` route, and chat interactions send messages to `/chat`, returning AI-generated responses based on the selected character. Once functional, deploy the backend to platforms like Heroku or Render, including a `requirements.txt` and `Procfile`. Securely configure environment variables, such as your API keys, on the hosting platform. If needed, host the frontend separately and link it to the backend. Finally, thoroughly test the application in the deployed environment to ensure seamless functionality and a responsive user experience.


### Project Demo
 Video
https://drive.google.com/file/d/1J630xGiOsgGJBo19_Ikohhu2lqQtcFoy/view?usp=drivesdk



## Team Contributions
- Aleesha Mariam Sabu: Frontend
- Hima Rose George: Backend
- Eunice Freeda T: AI integration

---
Made with ❤️ at TinkerHub
