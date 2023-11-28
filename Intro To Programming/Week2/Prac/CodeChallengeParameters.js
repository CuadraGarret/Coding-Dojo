function greet(name, time) {
//statement for if name is count dooku
    if (name === 'Count Dooku'){
        console.log("I'm coming for you, Dooku!");
        return;
}
//
    else if (time >= 6 && time < 18) {
        console.log("Good day, " + (name));
    }
    else if (time >= 18 && time < 24 || time < 5) {
        console.log("Good night, " + (name));
    }
}
greet('Count Dooku', 10);