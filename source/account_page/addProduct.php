<?php
session_start();
ini_set('display_errors', 'On');
error_reporting(E_ALL);
include_once "../includes/connection.php";
if($conn) {
    $query = mysqli_query($conn, sprintf("insert into Produtos (name, price, stock, picture) values('%s', '%s', '%s', '%s')", mysqli_real_escape_string($conn, $_POST['name']), mysqli_real_escape_string($conn, $_POST['price']), mysqli_real_escape_string($conn, $_POST['stock']), mysqli_real_escape_string($conn, $_POST['picture'])));
    if($query) {
        $_SESSION['warning'] = "product added successfully";
        header('Location: login_page.php');
    } else {
        $_SESSION['warning'] = "something went wrong";
        header('Location: login_page.php');
    }
}
?>
