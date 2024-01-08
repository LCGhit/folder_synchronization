<?php
session_start();
include_once "../includes/connection.php";
if($_POST['remove']) {
    unset($_SESSION['shopCart'][$_POST['id']]);
} else {
    if($_POST['quantity'] == 0) {
        unset($_SESSION['shopCart'][$_POST['id']]);
    } else {
        $currentPrice = $_SESSION['shopCart'][$_POST['id']]['price'];
        $currentQuantity = $_SESSION['shopCart'][$_POST['id']]['quantity'];
        $originalPrice =  $currentPrice/$currentQuantity;


        $stockQ = mysqli_query($conn, sprintf("SELECT stock FROM Produtos WHERE id='%s';", $_SESSION['shopCart'][$_POST['id']]['id']));
        $stock = mysqli_fetch_array($stockQ)[0];
        if($_POST['quantity'] <= $stock) {
            $_SESSION['shopCart'][$_POST['id']]['quantity'] = $_POST['quantity'];
            $_SESSION['shopCart'][$_POST['id']]['price'] = $_POST['quantity']*$originalPrice;
        } else {
            $_SESSION['shopCart'][$_POST['id']]['quantity'] = $stock;
            $_SESSION['shopCart'][$_POST['id']]['price'] = $stock*$originalPrice;
            $_SESSION['warning'] = 'Only '.$stock.' in stock';
        }
    }
}
header('Location: cart.php');
?>
