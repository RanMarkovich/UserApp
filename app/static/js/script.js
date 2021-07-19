
var errorsAppears = false;

function validateReg() {

    if (errorsAppears) { errorsInit() }

    let fname = document.getElementById('fname').value;
    let lname = document.getElementById('lname').value;
    let userName = document.getElementById('uname').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let flag = true;

    if (fname.length != "") showMessage('message1', true);
    else {
        showMessage('message1', false);
        flag = false;
    }

    if (lname.length != "") showMessage('message2', true);
    else {
        showMessage('message2', false);
        flag = false;
    }
    if (userName.length >= 2 && userName.length <= 8) showMessage('message3', true);
    else {
        showMessage('message3', false);
        flag = false;
    }
    if (isValidEmailRegex(email)) showMessage('message4', true);
    else {
        showMessage('message4', false);
        flag = false;
    }
    if (password.length >= 4 && password.length <= 8) showMessage('message5', true);
    else {
        showMessage('message5', false);
        flag = false;
    }

    if (flag == true) return true;
    errorsAppears = true; 
    return false;
}

function validateLogin() {
    
    if (errorsAppears) { errorsInit() }
    
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let flag = true;

    if (isValidEmailRegex(email))
        document.getElementById('message6').innerHTML += '';
    else {
        showMessage('message6', false);
        flag = false;
    }
    if (password.length >= 4 && password.length <= 8)
        document.getElementById('message7').innerHTML += '';
    else {
        showMessage('message7', false);
        flag = false;
    }
   
    if (flag == true) return true;
    errorsAppears = true; 
    return false;
}

function showMessage(elementId, isValid) {
    if (isValid)
        document.getElementById(elementId).innerHTML += '<p class="valid">OK</p>';
    else
        document.getElementById(elementId).innerHTML += '<p class="invalid">Invalid</p>';
}

// if errors already appears clear them.
function errorsInit() {
    let validErrorList = document.getElementsByClassName('valid');
    let invalidErrorList = document.getElementsByClassName('invalid');

    for (const element of validErrorList) {
        element.innerHTML = "";
    }
    for (const element of invalidErrorList) {
        element.innerHTML = "";
    }
}

function isValidEmailRegex(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}
