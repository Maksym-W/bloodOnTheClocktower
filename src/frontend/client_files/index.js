document.addEventListener('DOMContentLoaded', function() {
    // Fetch the client number from the server
    fetch('/client_number')
        .then(response => {
            // Check if the response is OK
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Log the client number to the console
            console.log('Client number:', data.client_number);
        })
        .catch(error => {
            // Handle errors and log them to the console
            console.error('Error fetching client number:', error);
        });

    // WebSocket connection setup
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

    // Create and append the 'End the Day' button
    const buttonDay = document.createElement("button");
    buttonDay.innerHTML = "End the Day";
    buttonDay.style.marginLeft = "25px";
    buttonDay.addEventListener("click", function() {
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "/end_day", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log("Response received:", xhr.responseText);
            }
        };
        xhr.send("test works!");

        const testText = document.createElement("h6");
        testText.innerHTML = "This is a test";
        document.body.appendChild(testText);
    });

    // Create and append the 'End the Night' button
    const buttonNight = document.createElement("button");
    buttonNight.innerHTML = "End the Night";
    buttonNight.style.marginLeft = "25px";
    buttonNight.addEventListener("click", function() {
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "/end_night", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log("Response received:", xhr.responseText);
            }
        };
        xhr.send("test works!");

        const testText = document.createElement("h6");
        testText.innerHTML = "This is a test";
        document.body.appendChild(testText);
    });

    // Append buttons to the document body
    document.body.appendChild(buttonDay);
    document.body.appendChild(buttonNight);
});
