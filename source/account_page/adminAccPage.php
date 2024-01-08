<?php
session_start();
/* ini_set('display_errors', 'On');
 * error_reporting(E_ALL); */
?>
<div id="sidemenu">
    <ul>
        <li><button class="sidemenuChoice">Purchases</button></li>
        <li><button class="sidemenuChoice">Personal Info</button></li>
        <li><button class="sidemenuChoice">Stock</button></li>
        <li><a href='logout.php' class="sidemenuChoice logoutBtn">Logout</a></li>
    </ul>
</div>
<div class="purchasesInfo">
    <?php
    include_once "../includes/connection.php";
    if($conn) {
        $purchases_num = mysqli_query($conn, sprintf("select e.id from Encomendas e WHERE user='%s' GROUP BY e.id;", $_SESSION['loggedUser']['username']));
        while($row = mysqli_fetch_assoc($purchases_num)) {
            $pNum[] = $row;
        }
        foreach($pNum as $array) {
            foreach($array as $value) {
                echo "<table class='purchasesTable'>";
                echo "<thead>";
                $purchases_query = sprintf("SELECT e.id as 'purchase ID', p.name as 'item', p.price*i.quantity as price, i.quantity, p.picture FROM Produtos p INNER JOIN encomenda_info i ON i.product = p.id INNER JOIN Encomendas e ON e.id = i.encomenda WHERE e.id='%s';", $value);
                $get_purchases = mysqli_query($conn, $purchases_query);
                $new_get_purchases = mysqli_query($conn, $purchases_query);
                echo "<tr>";
                foreach(mysqli_fetch_assoc($new_get_purchases) as $key => $value) {
                    if($key === 'picture') {
                        echo "<th></th>";
                    } else {
                        echo "<th>".$key."</th>";
                    }
                }
                echo "</tr></thead>";
                echo "<tbody>";
                while($row = mysqli_fetch_assoc($get_purchases)) {
                    echo "<tr>";
                    foreach($row as $key => $value) {
                        if($key==='picture') {
                            echo "<td><img src='../".$value."'/></td>";
                        } elseif($key==='total'){

                        }
                        else {
                            echo "<td>".$value."</td>";
                        }
                    }
                    echo "</tr>";
                }
                echo <<<lastRow
                <tr>
                <td></td>
                </tr>
                </tbody>
                </table>
lastRow;
            }
        }
    }
    ?>
</div>
<div class="personalInfoForm">
    <form name="userInfo_form" class="userInfo" method="post" action="usersInfoChanges.php">
        <h4>Personal Information</h4>
        <input name="username" class="personalInfoInput" type="text" value="" placeholder="<?php echo $_SESSION['loggedUser']['username']?>"/>
        <input name="password" class="personalInfoInput" type="password" value="" placeholder="<?php echo "***" ?>"/>
        <input name="name" class="personalInfoInput" type="text" value="" placeholder="<?php echo $_SESSION['loggedUser']['name']?>"/>
        <input name="address" class="personalInfoInput" type="text" value="" placeholder="<?php echo $_SESSION['loggedUser']['address']?>"/>
        <input name="birthDate" class="personalInfoInput" type="text" value="" placeholder="<?php echo $_SESSION['loggedUser']['birthDate']?>"/>
        <input name="sendForm" type="submit" class="switchSignIn_Up" value="update"/>
    </form>
</div>
<div id="editProducts">
    <?php
    include_once '../includes/connection.php';
    echo <<< openTable
    <table id='allProducts'>
    <thead>
    <tr>
    <th>name</th>
    <th>price</th>
    <th></th>
    <th>stock</th>
    <th></th>
    </tr></thead>
    <tbody>
    openTable;
    if($conn) {
        $productsQuery = mysqli_query($conn, "SELECT * FROM Produtos;");
        while($row = mysqli_fetch_assoc($productsQuery)) {
            echo "<tr id='".$row['id']."'>";
            foreach($row as $key => $value) {
                if($key==='picture') {
                    echo "<td><img src='../".$value."'></td>";
                } else if($key === 'id' || $key === 'stock') {
                    continue;
                } else if($key === 'price') {
                    echo "<td class='editCell'>
                 <form method='post' class='editCart' action='updateProducts.php'>
                     <input name='price' type='text' value='".$value."'/>
                 </td>";
                } else {
                    echo "<td>".$value."</td>";
                }
            }
            echo "<td class='editCell'>
                     <input name='quantity' type='number' value='".$row['stock']."'/>
<input name='update' type='submit' value='update' class='removeItemBtn'/>
                     <input name='id' type='hidden' value='".$row['id']."'/>
                 </form></td>";
            echo "</tr>";
        }
    }
    echo "<tr><td><button id='addBtn'>add new product</button></td></tr>";
    echo " <tr>";
    echo " <td>
<form method='post' class='editCart' action='addProduct.php'>
<input name='name' placeholder='name' type='text' value=''/></td>
<td><input name='price' placeholder='price' type='text' value=''/></td>
<td><input name='stock' placeholder='stock' type='text' value=''/></td>
<td><input name='picture' placeholder='picture' type='text' value=''/></td>
<td><input name='addProduct'
type='submit' value='add'/>
</form>
</td>";
    echo "</tr>";
    echo "</tbody>";
    echo "</table>";
    ?>
</div>

<script src="../javascript/adminAccPage.js"></script>
