var sideMenu = Array.from(document.getElementsByClassName('sidemenuChoice'));
var purchasesInfo = document.getElementsByClassName('purchasesInfo')[0];
var personalInfoForm = document.getElementsByClassName('personalInfoForm')[0];
var editProducts = document.getElementById('editProducts');

purchasesInfo.style.display = 'none';
personalInfoForm.style.display = 'none';

sideMenu[0].addEventListener('click', () => {
    personalInfoForm.style.display = 'none';
    purchasesInfo.style.display = 'flex';
    editProducts.style.display = 'none';
    document.getElementById('warning').style.display = 'none';
});

sideMenu[1].addEventListener('click', () => {
    purchasesInfo.style.display = 'none';
    personalInfoForm.style.display = 'flex';
    editProducts.style.display = 'none';
    document.getElementById('warning').style.display = 'none';
});

sideMenu[2].addEventListener('click', () => {
    purchasesInfo.style.display = 'none';
    editProducts.style.display = 'flex';
    personalInfoForm.style.display = 'none';
    document.getElementById('warning').style.display = 'none';
});

var eachTable = document.querySelectorAll('.purchasesTable');
eachTable.forEach(table => {
    var totalCell = table.querySelector('tr:last-of-type td');
    var prices = Array.from(table.querySelectorAll('tr td:nth-child(3)'));
    var total = 0;
    prices.forEach(newItem => {
        total = +total + +newItem.innerHTML;
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

document.getElementById('addBtn').addEventListener('click', () => {
    document.querySelector('tbody').lastChild.style.display = 'block';
});
