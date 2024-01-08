<?php
include_once "../includes/connection.php";
session_start();
$productInfo = $_REQUEST['p'];
if($conn) {
    $query = mysqli_query($conn, "SELECT * FROM Produtos WHERE id='".$productInfo."';");
    if($query) {
        $array = mysqli_fetch_assoc($query);
        if($_SESSION['shopCart'][$array['id']]) {

            if(intval($_SESSION['shopCart'][$array['id']]['quantity'])+1 <= $array['stock']) {
                $_SESSION['shopCart'][$array['id']]['quantity'] = intval($_SESSION['shopCart'][$array['id']]['quantity'])+1;
                $_SESSION['shopCart'][$array['id']]['price'] = floatval($array['price'])*intval($_SESSION['shopCart'][$array['id']]['quantity']);
                echo $_SESSION['shopCart'][$array['id']]['name']." added to cart";
            } else {
                echo 'No more in stock';
            }
        } elseif($array['stock'] != 0) {
            $array['quantity'] = 1;
            $_SESSION['shopCart'][$array['id']] = $array;
            echo $_SESSION['shopCart'][$array['id']]['name'].' added to cart';
        } else {
            echo 'No more in stock';
        }
    } else {
        echo "could not add product";
    }
} else {
    echo "Could not establish connection";
}
?>
