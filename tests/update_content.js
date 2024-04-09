document.addEventListener('DOMContentLoaded', function() {
    // Create a button element
    var button = document.createElement("button");
    // Set the button text
    button.innerHTML = "Show Message";

    // Add an event listener to the button for the click event
    button.addEventListener("click", function() {
        // Remove the button from the document
        document.body.removeChild(button);

        // Create a new element to hold the text
        var testText = document.createElement("h6");
        // Set the text content
        testText.innerHTML = "this is a test";
        // Append the text element to the document body
        document.body.appendChild(testText);
    });

    // Append the button to the document body
    document.body.appendChild(button);
});
