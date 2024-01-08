var select = document.getElementById('orderItems');
select.addEventListener('change', () => {
    select.form.submit();
});


var images = Array.from(document.getElementsByClassName('productInfo'));
images.forEach((image) => {
    image.addEventListener("mouseover", () => {
        image.firstChild.style.opacity = .7;
        image.children[1].style.opacity = 1;
        image.addEventListener("mouseout", () => {
            image.firstChild.style.opacity = 1;
            image.children[1].style.opacity = 0;
        });
    });
});


document.addEventListener("scroll", () => {
    if(window.scrollY > 150) {
        let navImg = document.getElementsByClassName('nav-logo')[0];
        navImg.style.opacity = 0;
    } else {
        let navImg = document.getElementsByClassName('nav-logo')[0];
        navImg.style.opacity = 1;
    }
});

function addItem(product) {
    var cart = document.getElementById('shopping_cart');
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            var responseAlert = xmlhttp.responseText;
            if(responseAlert !== "No more in stock") {
                cart = document.getElementById('cartCount');
                cart.innerHTML = parseInt(cart.innerHTML) + 1;
            }
            alert(xmlhttp.responseText);
        }
    };
    xmlhttp.open("GET", "index/addToCart.php?p=" + product, true);
    xmlhttp.send();
}

var allID = Array.from(document.getElementsByClassName('productInfo'));
allID.forEach((item, index) => {
    var itemID = item.id;
    var buyButton = document.getElementsByClassName('buy')[index];
    buyButton.addEventListener('click', () => {
        addItem(itemID);
    });
});
