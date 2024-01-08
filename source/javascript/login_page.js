var hoveredForm = Array.from(document.getElementsByClassName('login_form'));

hoveredForm.forEach(form => {
    form.addEventListener('mouseover', () => {
        form.style.backgroundColor = 'rgba(230, 230, 230, .6)';
        form.addEventListener("mouseout", () => {
            form.style.backgroundColor = 'white';
        });
    });
});

let lastScroll = 0;
document.addEventListener("scroll", () => {
    if(window.scrollY > 150) {
        let navImg = document.getElementsByClassName('nav-logo')[0];
        navImg.style.opacity = 0;
    } else {
        let navImg = document.getElementsByClassName('nav-logo')[0];
        navImg.style.opacity = 1;
    }
});


// check form data
var signUpInput = Array.from(document.getElementById('signUpF').children);
// var newt = signUpInput[1];
signUpInput.splice(0,1);
signUpInput.pop();

signUpInput.forEach((item, index) => {
    console.log(signUpInput[index]+index);
    item.addEventListener('blur', (event) => {
        if(checkForm(index)) {
            item.style.backgroundColor = 'rgb(204, 255, 204)';
        } else {
            item.style.backgroundColor = 'rgb(255, 179, 179)';
        }
    });
});



function checkForm(input) {
    var field = document.getElementById('signUpF').children[input+1].value;
    switch(input) {
    case 0:
        console.log(input);
        var userReg = /^(([a-zA-Z\d]){5,20})$/;
        if(userReg.test(field)) {
            return true;
        } else {
            return false;
        }
    case 1:
        var passReg = /^(([a-zA-Z\d]){5,20})$/;
        if(passReg.test(field)) {
            return true;
        } else {
            return false;
        }
    case 2:
        var nameReg = /^([a-zA-Z\d]{5,20})$/;
        if(nameReg.test(field)) {
            return true;
        } else {
            return false;
        }
    case 3:
        var addressReg = /^([a-zA-Z\d\s]){5,20}$/;
        if(addressReg.test(field)) {
            return true;
        } else {
            return false;
        }
    case 4:
        if(field) {
            return true;
        } else {
            return false;
        }
    default:
        return true;
    }
}

document.getElementById('jsChecked').addEventListener('click', (event) => {
    signUpInput.forEach((item, index) => {
        console.log(index);
        if(checkForm(index)) {
            item.style.backgroundColor = 'rgb(204, 255, 204)';
        } else {
            item.style.backgroundColor = 'rgb(255, 179, 179)';
            event.preventDefault();
            return;
        }
    });
});
// check form data
