function rename(id) {
    let jane = document.querySelector(id);
    jane.innerText = "Lebron James";
}

function remove(id) {
    let element = document.querySelector(id);
    let request = document.querySelector('#req');
    element.remove();
    request.innerText--;
}

function remove1(id) {
    let element = document.querySelector(id);
    let request = document.querySelector('#req');
    let connect = document.querySelector("#connect")
    element.remove();
    request.innerText--;
    connect.innerText++;
}

