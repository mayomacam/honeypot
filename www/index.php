<?php ob_start();
function redirect_to($loc){
		header("Location:".$loc);
	}
$conn=mysqli_connect("localhost","jayhawk","megatronstango","users");
	if(mysqli_connect_errno())
	{
		die("Argue With Programmer to fix this problem !!");
	}
$sql="SELECT * from users";
$result=mysqli_query($conn,$sql);
$loginName=$_GET['user'];
?>
<!doctype html>
   <html>
    <head>
        <link href="style.css" rel="stylesheet"/> 
        <link href="https://fonts.googleapis.com/css?family=Indie+Flower|Lobster|Ubuntu" rel="stylesheet">
        <script src="jquery-3.3.1.min.js"></script>
		<script SRC="JQUERY Main.js"></script>
    </head>
    <body>
		<div class="login_signup">
			<div class="login">
            <table border="0" cellspacing="10">
                <form name="frmsignin" method="post"><tr>
                    <td>
                        <div class="title"><nobr>SIGN IN</nobr></div>
                        <hr color="royalblue">
                    </td>
                </tr>
					<tr>
                    <td>
                        <input type="text" placeholder="TEAM/CLAN ID" name="tabName"/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <input type="text" placeholder="USER ID" name="user"/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <input type="password" placeholder="PASSWORD" name="pass"/>
                    </td>
                </tr>
                <tr>
                    <td><br><a href="#">Forgot Password</a>
                    <br></td>
                </tr>
                <tr>
                    <td>
                        <input type="submit" value="SIGN IN" id="signInBtn" name="signin"/>
                    </td>
                </tr>			
<?php
if(isset($_POST['signin']))
{
	$tabname=$_POST["tabName"];
	$user=$_POST['user'];
	$passIn=$_POST['pass'];
    $sql="Select * From ".$tabname;
	$result=mysqli_query($conn,$sql);
	while($row = mysqli_fetch_array($result)){
		if($user==$row["name"] && $passIn==$row["password"])
		{
			redirect_to("loggedin.php?user=".$user."&table=".$tabname);
		}
	}
		echo "<br><center>Enter Valid Data</center>";
}?>
                <tr>
                    <td>
                        <div id="signUpMsg">Don't Have An Account ?<a href="#" id="flipToSignUp">SIGN UP</a></div>
                    </td>
                </tr></form>
            </table>
        </div>
        <div class="signup">
            <table border="0" cellspacing="10">
                <form method="post" name="frmsignout" action="">  
				<tr>
                    <td>
                        <div class="title"><nobr>SIGN UP</nobr></div>
                        <hr color="royalblue">
                    </td>
				</tr>	
                <tr>
                    <td>
                        <input type="text" placeholder="TEAM NAME" name="newtable"/>
                    </td>
                </tr>
				<tr>
                    <td>
                        <input type="radio" name="existing" value='1'/>Existing
                        <input type="radio" name="createtab" value='1'/>New
                    </td>
                </tr>
		<?php
			if(isset($_POST['Existing'])){
				$table=$_POST["newtable"];
				$sql="Select * From ".$table;
				$result=mysqli_query($conn,$sql);
				if(mysqli_connect_errno()){
					die("There is no such table");
					}
			}
					?>
                <tr>
                    <td>
                        <input type="text" placeholder="YOUR NAME" name="newuser"/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <input type="password" placeholder="PASSWORD" name="newpass" id="passtry1"/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <input type="password" placeholder="CONFIRM PASSWORD" name="confirmpass" id="passtry2"/>
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        <input type="submit" value="SIGN UP" id="signUpBtn" name="signup"/>
                    </td>
                </tr>
		<?php
			if(isset($_POST['signup']))
			{
			$table=$_POST["newtable"];
			$name=$_POST['newuser'];
			$pass=$_POST['newpass'];
				if(isset($_POST['createtab'])){
					$query3="Create table ".$table."( ID INT not null Auto_increment, name varchar(30) not null, password varchar(30) not null ,primary key(id));";
					$result3= mysqli_query($conn,$query3);
						if(!$result3){
							echo "Something's wrong Our developers are informed about this...";
					}
				}
			$query2="INSERT INTO ".$table."(name, password)";
			$query2.="VALUES ";
			$query2.="('{$name}','{$pass}')";
			$result2= mysqli_query($conn,$query2);
			if(!$result2){
				echo "Something's wrong Our developers are informed about this...";
					}
			else{
				redirect_to("loggedin.php?user=".$name."&table=".$table);
			}
		}
	?>
                <tr>
                    <td align="center">Already Have An Account 
					<a href="#" id="flipToSignIn">SIGN IN</a></div>
					</td>
				</tr>
	   			</form>
			  </table>
		</div> <table id="social_media">
			<tr align="center">
					<td>
					 <img src="Facebook%20Square.png"/>
					</td>
					<td>
					 <img src="Twitter%20Square.png"/>
					</td>
					<td>
					 <img src="Instagram%20Square.png"/>
					</td>
			</tr>
		</table>
	   </div>
		 <div id="main">
            <img src="logo.png"/>
        <p>Aren't you tired of reminding your friend , roommate or anyone you live with that it's there turn to do the room's chores, like throwing trash away or cleaning the room or any other task. Our website solves this problem ,register your roommates, and it will simply show who's turn it is to do the job.</p><img src="teamsuccess.png" alt="">
        <div id="btn"><a href="signinup.php">DISCOVER MORE</a></div>  
		</div>
      </body>
</html><?php   
	mysqli_close($conn);
ob_flush();
?>
