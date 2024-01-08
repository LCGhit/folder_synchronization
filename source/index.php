<?php
session_start();
include_once "includes/connection.php";
$_SESSION['itemsNum'] = getItemsNum();
function getItemsNum() {
    if($_SESSION['shopCart']) {
        foreach($_SESSION['shopCart'] as $value) {
            $items = intval($items) + intval($value['quantity']);
            if($value === end($_SESSION['shopCart'])) {
                return $items;
            }
        }
    } else {
        return '0';
    }
}
?>
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <title>Document</title>
        <link href="css/index.css" rel="stylesheet"/>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <body>
        <nav>
            <div class="nav-logo"></div>
            <input name="checkLabel" type="checkbox" id="checkLabel" />
            <label for="checkLabel">
                <span class="menu"></span>
                <span class="menu"></span>
                <span class="menu"></span>
            </label>
            <ul class="nav-list">
                <li class="nav-item" id="deleteMe"><a href="#">Home</a></li>
                <li class="nav-item"><a href="#footerContacts">Contacts</a></li>
                <li class="nav-item" id="accBtn"><a href="account_page/login_page.php">Sign in/up</a></li>
                <li class="nav-item" id="shopping_cart"><a href="cart/cart.php"><span id="cartCount"><?php echo $_SESSION['itemsNum']; ?></span>
                    <span id="cartCheckout">checkout</span></a></li>
            </ul>
            <?php
            if($_SESSION['loggedUser']) {
            ?>
                <script>
                 document.getElementById("accBtn").firstChild.innerHTML = "My Account";
                </script>
            <?php
            }
            ?>
        </nav>
        <aside>
            <span id="warning">
                <?php
                echo $_SESSION['warning'];
                unset($_SESSION['warning']);
                ?>
            </span>
        </aside>
        <header><img alt="dudi banner" src="pictures/dudi_banner_02.jpg" class="banner"/></header>
        <div class="main">
            <form name="orderItemsForm" method="post" action="index.php">
                <select id="orderItems" name="orderItems" value="">
                    <?php if(!($_POST['orderItems'])) {echo "<option name='default' value='' selected>Order by:</option>"; } ?>
                    <option name="ascending" value="asc"><span>price asc</span></option>
                    <option name="descending" value="desc"><span>price desc</span></option>
                </select>
                <script>document.querySelector("[value='<?php echo $_POST['orderItems']?>']").selected = true</script>
            </form>
            <article class="products">
                <?php
                include "includes/connection.php";
                if($conn) {
                    $product_info;
                    $query = mysqli_query($conn, "select p.id, p.price, p.picture, p.stock from Produtos p ORDER BY p.price ".$_POST['orderItems']);
                    if($query) {
                        while($row = mysqli_fetch_assoc($query)){
                            $product_info[] = $row;
                        }
                    } else {
                        $_SESSION['warning'] = "No items found";
                    }
                    foreach($product_info as $key) {
                        echo "<div class='productInfo' id='".$key['id']."'>";
                        echo "<img src='".$key['picture']."' style=width:100%></img>";
                        if($key['stock'] != 0) {
                            echo "<div class='priceBuy'>
<button class='buyBtn buy'>buy</button><br/><span class='priceTag'>".$key['price']."€</span></div>";
                        } else {
                            echo "<div class='priceBuy'>
<button class='disabledBuyBtn buy'>out of stock</button><br/><span class='priceTag'>".$key['price']."€</span></div>";
                        }
                        echo "<br/>";
                        echo "</div>";
                    }
                } else {
                    $_SESSION['warning'] = "Connection could not be established";
                }
                ?>
            </article>
        </div>
        <footer>
            <div id="footerContacts">
                <span class="footerSpan">Address: Rua Padre Atónio Vieira , Braga, Portugal, 4710-412</span>
                <span class="footerSpan">Phone: +351 915 041 450</span>
                <span class="footerSpan">Mail: dudi.loja@hotmail.com</span>
            </div>
            <div id="footerSocialMedia">
                <a href="#" class="fa fa-facebook"></a>
                <a href="#" class="fa fa-twitter"></a>
                <a href="#" class="fa fa-instagram"></a>
            </div>
        </footer>
        <!-- <script src="https://code.jquery.com/jquery-3.7.0.js"></script> -->
        <script src="javascript/index_js.js"></script>
    </body>
</html>
