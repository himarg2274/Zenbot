document.addEventListener("DOMContentLoaded", () => {
    const characterSelection = document.getElementById("character-selection");
    const chatContainer = document.querySelector(".chat-container");
    const characterTitle = document.getElementById("character-title");
    const buttons = document.querySelectorAll(".character-btn");

    buttons.forEach((button) => {
        button.addEventListener("click", async () => {
            const character = button.getAttribute("data-character");
            characterTitle.textContent = `${character} ZenBot`;
            characterSelection.style.display = "none";
            chatContainer.classList.remove("hidden");

            // Send character selection to Flask
            await fetch("/select-character", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ character }),
            });
        });
    });

    // Chat logic
    const sendBtn = document.getElementById("send-btn");
    const userInput = document.getElementById("user-input");
    const chatbox = document.getElementById("chatbox");

    sendBtn.addEventListener("click", async () => {
        const userMessage = userInput.value.trim();
        if (userMessage) {
            appendMessage("user-message", userMessage);
            userInput.value = "";

            // Fetch bot response from Flask
            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage }),
            });
            const data = await response.json();
            appendMessage("bot-message", data.response || "Hmm, I need to think about that...");
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
