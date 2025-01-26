document.addEventListener("DOMContentLoaded", function() {
    const startChatBtn = document.getElementById("start-chat-btn");
    const characterSelection = document.getElementById("character-selection");
    const homePage = document.getElementById("home-page");

    // Handle Start Chat Button click
    startChatBtn.addEventListener("click", function() {
        homePage.classList.add("hidden"); // Hide the home page
        characterSelection.classList.remove("hidden"); // Show the character selection
    });

    const characterButtons = document.querySelectorAll(".character-btn");
    const chatContainer = document.querySelector(".chat-container");
    const characterTitle = document.getElementById("character-title");

    // Handle Character Selection
    characterButtons.forEach(button => {
        button.addEventListener("click", function() {
            const selectedCharacter = button.getAttribute("data-character");

            // Send the selected character to the server
            fetch("/select-character", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ character: selectedCharacter })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    // Hide character selection and show the chat interface
                    characterSelection.classList.add("hidden");
                    chatContainer.classList.remove("hidden");
                    characterTitle.textContent = `ZenBot - ${selectedCharacter}`;
                }
            })
            .catch(error => {
                console.error("Error selecting character:", error);
            });
        });
    });

    // Handle Chat Form submission
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");
    const chatbox = document.getElementById("chatbox");

    chatForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const message = userInput.value.trim();
        if (!message) return;

        // Display user message in chatbox
        const userMessage = document.createElement("div");
        userMessage.classList.add("user-message");
        userMessage.textContent = message;
        chatbox.appendChild(userMessage);
        userInput.value = ""; // Clear input field

        // Send message to the server
        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        })
        .then(response => response.json())
        .then(data => {
            const botMessage = document.createElement("div");
            botMessage.classList.add("bot-message");
            botMessage.textContent = data.response;
            chatbox.appendChild(botMessage);
            chatbox.scrollTop = chatbox.scrollHeight; // Scroll to the bottom
        })
        .catch(error => {
            console.error("Error in chat:", error);
        });
    });
});
