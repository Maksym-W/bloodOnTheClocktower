document.addEventListener('DOMContentLoaded', function() {
    fetchClientNumber();
    const ws = setupWebSocket();
    createAndAppendButton('Im a player', '/player', ws);
    createAndAppendButton('Im the game master', '/master', ws);
});

function fetchClientNumber() {
    fetch('/client_number')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Client number:', data.client_number);
        })
        .catch(error => {
            console.error('Error fetching client number:', error);
        });
}

function setupWebSocket() {
    const ws = new WebSocket('ws://localhost:8765');

    ws.onmessage = function(event) {
        console.log("Message received from server:", event.data);
        const message = document.createElement("p");
        message.textContent = "Server says: " + event.data;
        document.body.appendChild(message);
    };

    ws.onopen = function() {
        console.log('WebSocket connection opened');
    };

    ws.onclose = function() {
        console.log('WebSocket connection closed');
    };

    ws.onerror = function(error) {
        console.error('WebSocket error:', error);
    };

    return ws;
}

function createAndAppendButton(buttonText, endpoint, ws) {
    const button = document.createElement("button");
    button.innerHTML = buttonText;
    button.style.marginLeft = "25px";
    button.addEventListener("click", function() {
        const existingButtons = document.querySelectorAll("button");
        existingButtons.forEach((btn) => btn.remove());

        const xhr = new XMLHttpRequest();
        xhr.open("POST", endpoint, true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log("Response received:", xhr.responseText);
                testText.innerHTML = xhr.responseText;
                document.body.appendChild(testText);

                if (xhr.responseText.includes("game master")) {
                    setupMaster(ws);
                }
            }
        };
        xhr.send("test works!");

        // Send the message over WebSocket
        if (ws && ws.readyState === WebSocket.OPEN) {
            ws.send("test works!");
        } else {
            console.error("WebSocket is not open");
        }

        const testText = document.createElement("h6");
        testText.innerHTML = "This is a test";
        document.body.appendChild(testText);
    });

    document.body.appendChild(button);
}

function setupMaster(ws) {
    buttonText = "Start Game";
    endpoint = "/masterSet";

    const button = document.createElement("button");
    button.innerHTML = buttonText;
    button.style.marginLeft = "25px";
    button.addEventListener("click", function() {
        const existingButtons = document.querySelectorAll("button");
        existingButtons.forEach((btn) => btn.remove());

        const xhr = new XMLHttpRequest();
        xhr.open("POST", endpoint, true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log("Response received:", xhr.responseText);
                testText.innerHTML = xhr.responseText;
                document.body.appendChild(testText);
            }
        };
        xhr.send("test works!");

        // Send the message over WebSocket
        if (ws && ws.readyState === WebSocket.OPEN) {
            ws.send("test works!");
        } else {
            console.error("WebSocket is not open");
        }

        const testText = document.createElement("h6");
        testText.innerHTML = "This is a test";
        document.body.appendChild(testText);
    });

    document.body.appendChild(button);
}
