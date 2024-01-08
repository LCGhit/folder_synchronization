<?php
session_start();
ini_set('display_errors', 'On');
error_reporting(E_ALL);
include_once "../includes/connection.php";
if($conn) {
    $query = mysqli_query($conn, sprintf("UPDATE Produtos SET price='%s', stock=%s WHERE id='%s';", $_POST['price'], intval($_POST['quantity']), $_POST['id']));
    if($query) {
        $_SESSION['warning'] = "changes successful";
        header('Location: login_page.php');
    } else {
        $_SESSION['warning'] = "something went wrong";
        header('Location: login_page.php');
    }
}
?>
