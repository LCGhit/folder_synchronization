<?php
session_start();
include "../includes/connection.php";
ini_set('display_errors', 'On');
error_reporting(E_ALL);
if($conn) {
    if($_POST['address']) {

        $username = mysqli_real_escape_string($conn, $_POST['username']);
        $checkusername = mysqli_fetch_array(mysqli_query($conn, sprintf("SELECT username FROM Utilizadores WHERE username='%s';", $username)));
        if($checkusername != 0) {
            $_SESSION['warning'] = "username already exists";
            header('Location: login_page.php');
        }

        $password = mysqli_real_escape_string($conn, $_POST['password']);
        $comleteName = mysqli_real_escape_string($conn, $_POST['completeName']);
        $address = mysqli_real_escape_string($conn, $_POST['address']);


        $compareBirthDate = date_create($_POST['birthDate']);
        $currentDate = date_create(date('m-d-Y'));
        $diff = date_diff($compareBirthDate, $currentDate);
        $age = $diff->format('%y');
        if($age < 18) {
            $_SESSION['warning'] = "You must be at least 18";
            header('Location: login_page.php');
            exit();
        }

        $query = "insert into Utilizadores values('".$username."','".password_hash($password, PASSWORD_DEFAULT)."','" .$comleteName."','" .$address."','" .$_POST['birthDate']."');";
        if(mysqli_query($conn, $query)) {
            $_SESSION['loggedUser'] = mysqli_fetch_assoc(mysqli_query($conn, "SELECT * FROM Utilizadores WHERE username='".$username."';"));
            $_SESSION['id'] = $username;
            if($_POST['finishP']) {
                header('Location: ../cart/completePurchase.php');
            } else {
                header('Location: login_page.php');
            }
        } else {
            $_SESSION['warning'] = "wrong username and/or password";
            echo "wrong username and/or password";
        }
    } else {
        $username = mysqli_real_escape_string($conn, $_POST['username']);
        $password = mysqli_real_escape_string($conn, $_POST['password']);
        $hash = mysqli_fetch_assoc(mysqli_query($conn, "SELECT password FROM Utilizadores WHERE
username='".$username."';"));
        if(password_verify($password,$hash['password'])) {
            $userInfo_query = "SELECT * FROM Utilizadores WHERE username='".$username."';";
            $_SESSION['loggedUser'] = mysqli_fetch_assoc(mysqli_query($conn, $userInfo_query));
            if($_POST['finishP']) {
                header('Location: ../cart/completePurchase.php');
            } else {
                header('Location: login_page.php');
            }
        } else {
            $_SESSION['warning'] = "wrong username/password";
            header('Location: login_page.php');
        }
    }
} else {
    $_SESSION['warning'] = "Connection could not be established";
    echo "Connection could not be established";
}
?>
