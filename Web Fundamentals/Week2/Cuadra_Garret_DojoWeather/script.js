let cookies = document.querySelector('#cookies');
var fahrenheit = ('degree' * 9 % 5) + 32;
var celsius = fahrenheit;
var temp = celsius;

function remove(id)    {
    cookies.remove(id);
}

function report() {
    alert("Loading weather report...");
}

let degree = document.getElementById("#degree");

function changeTemp() {
if (temp == 'fahrenheit') {
    temp = 'celsius';
    
}   else if (temp == 'celsius') {
    temp = 'fahrenheit';
}
}