document.addEventListener('DOMContentLoaded', function() {
    // -- The below code is for ending the day

    // Create a button element
    var button_day = document.createElement("button");
    // Set the button text
    button_day.innerHTML = "End the Day";

    // Position the button 25 pixels to the right of its original position
    button_day.style.marginLeft = "25px";

    // Add an event listener to the button for the click event
    button_day.addEventListener("click", function() {

        // Send an AJAX request to the Python server
        var xhr = new XMLHttpRequest();
        var data = "test works!"; 
        xhr.open("POST", "/end_day", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    // Request was successful, do something with the response
                    console.log("Response received:", xhr.responseText);
                }
            };
        xhr.send(data);


        // Create a new element to hold the text
        var testText = document.createElement("h6");
        // Set the text content
        testText.innerHTML = "this is a test";
        // Append the text element to the document body
        document.body.appendChild(testText);
    });

    // The below code is for ending the night

    // Create a button element
        var button_night = document.createElement("button");
        // Set the button text
        button_night.innerHTML = "End the night";

        // Position the button 25 pixels to the right of its original position
        button_night.style.marginLeft = "25px";

        // Add an event listener to the button for the click event
        button_night.addEventListener("click", function() {

            // Send an AJAX request to the Python server
            var xhr = new XMLHttpRequest();
            var data = "test works!"; 
            xhr.open("POST", "/end_night", true);
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    // Request was successful, do something with the response
                    console.log("Response received:", xhr.responseText);
                }
            };
            xhr.send(data);

            // Create a new element to hold the text
            var testText = document.createElement("h6");
            // Set the text content
            testText.innerHTML = "this is a test";
            // Append the text element to the document body
            document.body.appendChild(testText);
        });


    // Append the button to the document body
    document.body.appendChild(button_day);
    document.body.appendChild(button_night);
});
