//Variable for speed ran 
let mph = 6;

//Loop for amount of miles ran and candy given.
for (let milesRan = 2 ; milesRan <= 8; milesRan += 2) {

//If statement to give candy
if (milesRan <= 6 && mph >= 5.5) {
    console.log('Have some candy!');
}
//Else if statement to stop giving out candy
else {
            console.log('No more candy for you.');
}
}