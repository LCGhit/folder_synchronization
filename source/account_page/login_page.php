<?php
session_start();
include_once "../includes/connection.php";
/* ini_set('display_errors', 'On');
 * error_reporting(E_ALL); */
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
        <link href="../css/login.css" rel="stylesheet"/>
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
                <li class="nav-item"><a href="../index.php">Home</a></li>
                <li class="nav-item" id="accBtn"><a href="#">Sign in/up</a></li>
                <li class="nav-item" id="shopping_cart"><a href="../cart/cart.php"><span id="cartCount"><?php echo $_SESSION['itemsNum']; ?></span>
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
        <?php
        if($_SESSION['loggedUser']) {
            if($_SESSION['loggedUser']['username'] !== "admin") {
                echo "<div class='changeInfo'>";
                include "clientAccPage.php";
                echo "</div>";
        ?>
            <script>
             document.getElementById("accBtn").firstChild.innerHTML = "My Account";
            </script>
        <?php
        } else if($_SESSION['loggedUser']['username'] === "admin") {
            echo "<div class='changeInfo'>";
            include "adminAccPage.php";
            echo "</div>";
        ?>
            <script>
             document.getElementById("accBtn").firstChild.innerHTML = "My Account";
            </script>
        <?php
        }
        } else {
        ?>
            <div class="login_wraper">
                <form class="login_form" id="signInF" name="signin_form" method="post" action="signin_up.php">
                    <h4>Sign in</h4>
                    <input name="username" type="text" value="" placeholder="username" />
                    <input name="password" type="password" value="" placeholder="password" />
                    <button type="submit" class="switchSignIn_Up">Sign in</button>
                </form>
                <form class="login_form" id="signUpF" name="signup_form" method="post" action="signin_up.php">
                    <h4>Sign up</h4>
                    <input name="username" type="text" value="" placeholder="Username" />
                    <input name="password" type="password" value="" placeholder="Password" />
                    <input name="completeName" type="text" value="" placeholder="Your Name" />
                    <input name="address" type="text" value="" placeholder="Address" />
                    <input name="birthDate" type="date" value="" placeholder="Date of birth" />
                    <input name="" type="submit" class="switchSignIn_Up" value="Create account" id="jsChecked" />
                </form>
            </div>

        <?php
        }
        ?>
        <script src="../javascript/login_page.js"></script>
    </body>
</html>
