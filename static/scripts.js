// Character selection logic
document.addEventListener("DOMContentLoaded", () => {
    const characterSelection = document.getElementById("character-selection");
    const chatContainer = document.querySelector(".chat-container");
    const characterTitle = document.getElementById("character-title");
    const buttons = document.querySelectorAll(".character-btn");

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            const character = button.getAttribute("data-character");
            characterTitle.textContent = `${character} ZenBot`;
            characterSelection.style.display = "none";
            chatContainer.classList.remove("hidden");
        });
    });

    // Chat logic (example)
    const sendBtn = document.getElementById("send-btn");
    const userInput = document.getElementById("user-input");
    const chatbox = document.getElementById("chatbox");

    sendBtn.addEventListener("click", () => {
        const userMessage = userInput.value.trim();
        if (userMessage) {
            appendMessage("user-message", userMessage);
            userInput.value = "";

            // Simulated bot response
            setTimeout(() => {
                appendMessage("bot-message", "Let me think about that...");
            }, 1000);
        }
    });

    function appendMessage(className, message) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add(className);
        messageDiv.textContent = message;
        chatbox.appendChild(messageDiv);
        chatbox.scrollTop = chatbox.scrollHeight;
    }
});
