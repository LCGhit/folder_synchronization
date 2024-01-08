<?php
session_start();
$_SESSION['unset'] = 'unset';
?>
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <title>Document</title>
        <link href="../css/index.css" rel="stylesheet"/>
        <link href="../css/cart.css" rel="stylesheet"/>
        <style>
         aside {
             text-align: center;
             flex-direction: column;
             width: min-content;
             align-items: center;
             width: 100%;
         }
         #icon {
             width:auto;
             height:12em;
         }
        </style>
    </head>
    <body>
        <aside>
            <h2 id="warning">Thank you!</h2>
            <img id="icon" alt="dudi icon" src="../pictures/dudi_icon_02.jpg"/>
        </aside>
        <?php
        echo <<< openTable
        <button id="backToCart"><a href="../account_page/login_page.php">Return</a></button>
        <article>
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
            echo "</tr>";
        }
        echo " <tr>";
        echo " <td></td>";
        echo "</tr>";
        echo "</tbody>";
        echo "</table>";
        echo "</article>";
        ?>
    </body>
</html>
