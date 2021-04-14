//Array to store messages
var messages = [];

//Message type to lookup obj
var messageType = {
    out: 'out-message',
    in: 'in-message',
    unknown: 'unknown-message'
};

//Seed Data
var data = [
    {
        type: messageType.out,
        user: "Sam",
        message: "Hey, you free to play some more Forest?"
    },
    {
        type: messageType.in,
        user: "Nathan",
        message: "Yeah! Im all free right now!"
    },
    {
        type: messageType.in,
        user: "Nathan",
        message: "Just finished my school work."
    },
    {
        type: messageType.out,
        user: "Sam",
        message: "Sweet! Hosting the world now!"
    }
];

//Message Constructor
function Message(type, user, message) {
    this.type = type;
    this.user = user;
    this.message = message;
}

//Function to create and return an element for the supplied message
function createMessageElement(message) {
    //Create text element
    var messageText = document.createTextNode(
        message.user + ': ' + message.message
    );

    //Create element and add text
    var messageEl = document.createElement("div");
    messageEl.appendChild(messageText);

    //Add a class using message type
    messageEl.className = message.type;

    return messageEl
}


//Button click event handler to add a new message
function addMessageHandler(event){
    var user,type;
    var messageInput = document.getElementById('message-input');
    var messagesContainerEl = docuent.getElementById('message-container');

    //Determine type and set var accordingly
    switch (event.target.id) {
        case 'send-button':
            user = "Sam";
            type = messageType.out;
            break;
        case 'reply-button':
            user = "Nathan"
            type = messageType.in;
            break;
        default:
            user = 'unknown'
            type = messageType.unknown;
    }

    //create new message
    if (messageInput.value != '') {
        //Construct a message and add to array
        var message = new Message(type, user, messageInput.value);
        messages.push(message);

        //create element
        var el = createMessageElement(message);

        //Add message to DOM
        messagesContainerEl.appendChild(el);

        //Reset input
        messageInput.value = '';
    }
}


//Load seed data from array above
function loadSeedData(){
    for(var i =0; i < data.length; i++){
        var message = new Message(data[i].type, data[i].user, data[i].message);
        messages.push(message);
    }

    //Load view with pre-loaded messages
    var messagesContainerEl = document.getElementById('message-container');

    for (var i = 0; i < messages.length; i++) {
        var message = messages[i];
        var el = createMessageElement(message)

        messagesContainerEl.appendChild(el);
    }
}

var init = function(){
    //Wire event handlers
    document.getElementById('send-button').onclick = addMessageHandler;
    document.getElementById('reply-button').onclick = addMessageHandler;

    //load seed data
    loadSeedData();
};

init();