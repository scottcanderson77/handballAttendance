<?php

session_start();
if($_POST['user']=="tj" && $_POST['tj]=="tj"]){
$_SESSION['user'] = "tj";
$_SESSION['password'] = "tj"
header("Location: content.php");
}

else{
header("Location: "index2.php");
}
?>