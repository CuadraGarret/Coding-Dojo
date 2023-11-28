function howMuchLeftOverCake(numberOfPieces, numberOfPeople) {
//number of pieces - number of people = greater than 5
if (numberOfPieces - numberOfPeople > 5) {
    console.log("Hold Another Party!");
}
//number of pieces - number of people = between 5 and 3
if (numberOfPieces - numberOfPeople <= 5 && numberOfPieces - numberOfPeople >= 3) {
    console.log("You have leftovers to share");
}
//number of pieces - number of people = 1,2,3
if (numberOfPieces - numberOfPeople < 3 && numberOfPieces - numberOfPeople >= 1) {
    console.log("You have some leftovers");
}
//number of pieces - number of people = 0
if (numberOfPieces - numberOfPeople === 0) {
    console.log("No leftovers for you!")
}
return;
}
howMuchLeftOverCake();