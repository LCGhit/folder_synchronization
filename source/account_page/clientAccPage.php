<?php
session_start();
?>
<div id="sidemenu">
    <ul>
        <li><button class="sidemenuChoice">Purchases</button></li>
        <li><button class="sidemenuChoice">Personal Info</button></li>
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
<script src="../javascript/clientAccPage.js"></script>
