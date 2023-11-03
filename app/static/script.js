// // JavaScript
// var promptInput = document.getElementById("chat-input");

// function handleKeyUp(event) {
//   if (event.keyCode === 13) {
//     // Enter key is pressed
//     // You can call a function or perform an action here
//     processUserInput(promptInput.value);
//     // Clear the input field if needed
//     promptInput.value = "";
//   }
// }

// function processUserInput(input) {
//   // This function is called when Enter key is pressed
//   // You can perform some action with the user's input here
//   console.log("User input: " + input);
//   // Add your logic for processing the input
// }


// ===================My code starts here======================
function save_topic(topic){
    var my_topic = document.getElementById('chat-input')
    
    var data = {
        'topic': my_topic.value
    }
    console.log(data)
    // now call python funct to prounce

        fetch(`/respond`,
        {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(data),
            cache: 'no-cache',
            headers: new Headers({
                'content-type': 'application/json'
            })

        })// Then do something other withe respond...
        .then(function (response) {
            if (response.status != 200) {
                console.log(`Response status were not 200: ${response.status}`);
                return;
            }
            response.json().then(function (data) {
                console.log(data)

            })
        })// End of then
    
}
