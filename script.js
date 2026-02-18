const chat = document.getElementById("chat");
const userinput = document.getElementById("user-input");
const sendbtn = document.getElementById("send-btn");

function addMessage(sender, text) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);
  messageDiv.textContent = text;
  chat.appendChild(messageDiv);
  chat.scrollTop = chat.scrollHeight;
}

sendbtn.addEventListener("click", async () => {
  const message = userinput.value.trim();
  if (!message) return;

  addMessage("user", message);
  userinput.value = "";

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    addMessage("ai", data.response);

  } catch (error) {
    addMessage("ai", "Error connecting to backend.");
  }
});

userinput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    sendbtn.click();
  }
});
