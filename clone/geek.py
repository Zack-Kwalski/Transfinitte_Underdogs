<!DOCTYPE html>
<html>
<head>
    <title>DogGPT Chatbot</title>
</head>
<body>
    <h1>DogGPT Chatbot</h1>
    <form method="post" id="chat-form">
        <input type="text" id="user_input" name="user_input" placeholder="Type your message here">
        <button type="button" id="record-button">Record</button>
        <input type="submit" value="Submit">
    </form>

    <div>
        <strong>User:</strong> <span id="user-message"></span><br>
        <strong>DogGPT:</strong> <span id="response"></span>
    </div>

    <script>
        const recordButton = document.getElementById("record-button");
        const userMessage = document.getElementById("user-message");
        const userInput = document.getElementById("user_input");

        recordButton.addEventListener("click", () => {
            // Check if the browser supports speech recognition
            if ("webkitSpeechRecognition" in window) {
                const recognition = new webkitSpeechRecognition();
                recognition.continuous = false;
                recognition.lang = "en-US";

                recognition.onresult = (event) => {
                    const result = event.results[0][0].transcript;
                    userMessage.textContent = result;
                    userInput.value = result;
                };

                recognition.start();
            } else {
                alert("Speech recognition is not supported in this browser.");
            }
        });
    </script>
</body>
</html>
