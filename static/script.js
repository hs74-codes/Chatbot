const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");

async function sendMessage() {
    const message = userInput.value.trim();
    if (message === "") return;

    appendMessage("You", message, "user");
    userInput.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await response.json();
    appendMessage("Bot", data.response, "bot");
}

function appendMessage(sender, text, className) {
    const msg = document.createElement("div");
    msg.classList.add("message", className);
    msg.innerHTML = `<b>${sender}:</b> ${text}`;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

userInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
