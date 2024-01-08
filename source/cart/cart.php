<?php
session_start();
if($_SESSION['unset']) {
    unset($_SESSION['shopCart']);
    unset($_SESSION['unset']);
}
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
        <link href="../css/index.css" rel="stylesheet"/>
        <link href="../css/cart.css" rel="stylesheet"/>
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
                <li class="nav-item" id="deleteMe"><a href="../index.php">Home</a></li>
                <li class="nav-item"><a href="#footerContacts">Contacts</a></li>
                <li class="nav-item" id="accBtn"><a href="../account_page/login_page.php">Sign in/up</a></li>
                <li class="nav-item" id="shopping_cart"><a href="cart.php">
                    <span id="cartCount"><?php echo $_SESSION['itemsNum']; ?></span>
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
        <article>
            <?php
            echo <<< openTable
            <table class='purchasesTable'>
            <thead>
            <tr>
            <th>name</th>
            <th>price</th>
            <th></th>
            <th>quantity</th>
            <th></th>
            </tr></thead>
            <tbody>
            openTable;
            foreach($_SESSION['shopCart'] as $array) {
                echo "<tr id='".$array['id']."'>";
                foreach($array as $key => $value) {
                    if($key==='picture') {
                        echo "<td><img src='../".$value."'></td>";
                    } else if($key === 'id' || $key === 'stock') {
                        continue;
                    } else {
                        echo "<td>".$value."</td>";
                    }
                }
                echo "<td class='editCell'>
                    <form method='post' class='editCart' action='updateForm.php'>
                        <input name='quantity' type='number' value='".$array['quantity']."'/>
                        <input name='remove' type='submit' value='remove' class='removeItemBtn'/>
                        <input name='id' type='hidden' value='".$array['id']."'/>
                    </form></td>";
                echo "</tr>";
            }
            echo " <tr>";
            echo " <td></td>";
            echo "</tr>";
            echo "</tbody>";
            echo "</table>";

            if($_SESSION['loggedUser'] && $_SESSION['shopCart']) {
            ?>
                <form method="post" action="completePurchase.php" id="completePurchase">
                    <input name="" type="submit" value="buy"/>
                </form>
            <?php
            } elseif($_SESSION['shopCart']) {
            ?>
                <button id="purchaseSignInUp" value="next">proceed</button>
            <?php
            }
            ?>
        </article>
        <div id="log">
            <div class="login_wraper">
                <form class="login_form" id="signInF" name="" method="post" action="../account_page/signin_up.php">
                    <h4>Sign in</h4>
                    <input name="username" type="text" value="" placeholder="username" />
                    <input name="password" type="password" value="" placeholder="password" />
                    <input name="finishP" type="hidden" value="finishPurchase"/>
                    <button type="submit" class="switchSignIn_Up">Sign in</button>
                </form>
                <form class="login_form" id="signUpF" name="" method="post" action="../account_page/signin_up.php">
                    <h4>Sign up</h4>
                    <input name="username" type="text" value="" placeholder="Username" />
                    <input name="password" type="password" value="" placeholder="Password" />
                    <input name="completeName" type="text" value="" placeholder="Your Name" />
                    <input name="address" type="text" value="" placeholder="Address" />
                    <input name="birthDate" type="date" value="" placeholder="Date of birth" />
                    <input name="finishP" type="hidden" value="finishPurchase"/>
                    <input name="" type="submit" class="switchSignIn_Up" value="Create account" id="jsChecked"/>
                </form>
            </div>
            <button id="backToCart" value="">back to cart</button>
        </div>
        <script src="../javascript/cart.js"></script>
    </body>
</html>
