<?php
session_start();
include_once "../includes/connection.php";

/* populate empty form fields with existing user info */
if($_POST['password'] !== '') {
    $_POST['password'] = password_hash($_POST['password'], PASSWORD_DEFAULT);
}
$postInfo = [];
foreach($_POST as $key => $value) {
    if($value === '') {
        $postInfo[$key] = $_SESSION['loggedUser'][$key];
    } else {
        $postInfo[$key] = $_POST[$key];
    }
}
/* make changes */
if($conn) {
    $query = sprintf("update Utilizadores set username='%s', password='%s', name='%s', address='%s', birthDate='%s' where username='%s';", mysqli_real_escape_string($conn,$postInfo['username']), mysqli_real_escape_string($conn,$postInfo['password']), mysqli_real_escape_string($conn,$postInfo['name']), mysqli_real_escape_string($conn,$postInfo['address']), mysqli_real_escape_string($conn,$postInfo['birthDate']), $_SESSION['loggedUser']['username']);

    if(mysqli_query($conn, $query)) {
        $newInfo = mysqli_query($conn, sprintf("select * from Utilizadores where username='%s';", $postInfo['username']));
        $_SESSION['loggedUser'] = mysqli_fetch_assoc($newInfo);
        $_SESSION['warning'] = "Changes successful";
        header("Location: login_page.php");
    } else {
        $_SESSION['warning'] = "Could not make changes";
        header("Location: login_page.php");
    }
} else {
    $_SESSION['warning'] = "Connection failed to establish";
    header("Location: login_page.php");
}
?>
