var eachTable = document.querySelectorAll('.purchasesTable');
eachTable.forEach(table => {
    var totalCell = table.querySelector('tr:last-of-type td');
    var prices = Array.from(table.querySelectorAll('tr td:nth-child(2)'));
    var total = 0;
    prices.forEach(newItem => {
        total = parseFloat(+total) + parseFloat(+newItem.innerHTML);
    });
    totalCell.innerHTML = "total: "+total;
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

var cartForm = Array.from(document.getElementsByClassName('editCart'));
cartForm.forEach(form => {
    form.children[0].addEventListener('change', () => {
        form.submit();
    });
    form.children[1].addEventListener('click', () => {
        form.submit();
    });
});

var nextBtn = document.getElementById('purchaseSignInUp');
nextBtn.addEventListener('click', () => {
    document.querySelectorAll('article')[0].style.display = 'none';
    document.getElementById('log').style.display = 'grid';
    document.getElementById('warning').style.display = 'none';
});
var backToCart = document.getElementById('backToCart');
backToCart.addEventListener('click', () => {
    document.querySelectorAll('article')[0].style.display = 'flex';
    document.getElementById('log').style.display = 'none';
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
