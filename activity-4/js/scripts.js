//welcome message
var user = "Sam";
var salutation = "What is up, ";
var greeting = salutation + user + "! Here are some of the latest NINTENDO SWITCH reviews!";
var greetingEl = document.getElementById('greeting');

greetingEl.textContent = greeting;


//Product prices
var price = 300;
    studentDiscount = .5,
    studentPrice = price - (price * studentDiscount),
    priceEl = document.getElementById('price'),
    studentPriceEl = document.getElementById('student-price');

priceEl.textContent = price.toFixed(2);
studentPriceEl.textContent = studentPrice.toFixed(2);