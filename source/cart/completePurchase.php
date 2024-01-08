<?php
session_start();
include_once "../includes/connection.php";
if($conn) {
    $loggedUser = $_SESSION['loggedUser']['username'];
    $purchaseQ = mysqli_query($conn, "INSERT INTO Encomendas (user) values('".$loggedUser."');");

    if($purchaseQ) {
        $lastIDQ = mysqli_query($conn, "SELECT MAX(id) FROM Encomendas WHERE user='".$loggedUser."';");
        $lastID = mysqli_fetch_array($lastIDQ)[0];

        foreach($_SESSION['shopCart'] as $value) {
            $purchaseInfoQ = mysqli_query($conn, sprintf("INSERT INTO encomenda_info values('%s', '%s', '%s');", $lastID, $value['id'], $value['quantity']));
            $updateStock = mysqli_query($conn, sprintf("UPDATE Produtos SET stock=stock-%s WHERE id='%s';", $value['quantity'], $value['id']));
        }
    }
}
header('Location: purchaseSuccess.php');
?>
