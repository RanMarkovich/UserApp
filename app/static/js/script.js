
// handle inputs in Register page.
function regInputsHandler(){
    if(event.target.id == 'fname'){
        if (event.target.value.length > 0) showMessage('message1', true);
        else showMessage('message1', false);
    }
    else if(event.target.id == 'lname'){
        if (event.target.value.length > 0) showMessage('message2', true);
        else showMessage('message2', false);
    }
    else if(event.target.id == 'uname'){
        if (event.target.value.length >= 2 && event.target.value.length <= 8) showMessage('message3', true);
        else showMessage('message3', false);
    }
    else if(event.target.id == 'email'){
        if (isValidEmailRegex(event.target.value)) showMessage('message4', true);
        else showMessage('message4', false);
    }
    else if(event.target.id == 'password'){
        if (event.target.value.length >= 4 && event.target.value.length <= 8) showMessage('message5', true);
        else showMessage('message5', false);
    }
}

// handle inputs in Login page.
function loginInputsHandler() {

    if(event.target.id == 'email'){
        if (isValidEmailRegex(event.target.value)) showMessage('message6', true);
        else showMessage('message6', false);
    }
    else if(event.target.id == 'password'){
        if (event.target.value.length >= 4 && event.target.value.length <= 8) showMessage('message7', true);
        else showMessage('message7', false);
    }
}

function showMessage(elementId, isValidMessage) {
    if (isValidMessage) document.getElementById(elementId).innerHTML = '<p class="valid">OK</p>';
    else document.getElementById(elementId).innerHTML = '<p class="invalid">Invalid</p>';
}

// When press on submit button check fields in Register or Login.
// register validMessagesCount = 5 , Login validMessagesCount = 2
function isValidFields(validMessagesCount) { //
    let validMessageList = document.getElementsByClassName('valid');
    if(validMessageList.length == validMessagesCount) return true;
    document.querySelector('.span').style.visibility ='visible';
    return false;
}

function isValidEmailRegex(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}