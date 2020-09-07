<?php ob_start();
	function redirect_to($loc){
		header("Location:".$loc);
	}
	$conn=mysqli_connect("localhost","jayhawk","megatronstango","users");
	if(mysqli_connect_errno())
	{
		die("Argue With Programmer to fix this problem !!");
	}

?>
   <html>
    <head>
       <title>Take Turns Login</title>
        <link href="Main.css" rel="stylesheet"/>
         <link href="https://fonts.googleapis.com/css?family=Exo+2|Indie+Flower|Lobster|Oswald|Ubuntu" rel="stylesheet">
        <script src="jquery-1.10.2.min.js"></script>
        <script src="JQUERY%20Main.js"></script>
        <style>
		h1{
		 padding: 0px;
		 position: absolute;
		 left: 40%;
		 top:5%;
		 margin: 0px;
		 font-family: lobster;
		font-weight: lighter;
		color: aliceblue;
			font-size: 40px;
			word-spacing: 15px;
	 }
		</style>
    </head>
    <body>
           <h1>Take Your Turn</h1>
        <div id="main">
            <table border="0" cellspacing="10">
                <tr>
                    <td> <form name="frmsignin" method="post">
                        <div id="title">SIGN IN</div>
                        <hr size="1px" width="100px" color="black"/>
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
                    <td align="right">
                        <div id="frt">FORGOT PASSWORD</div>
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        <input type="submit" value="SIGN IN" id="signInBtn" name="signin"/>
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        <div id="signUpMsg">DON'T HAVE AN ACCOUNT <a href="#" id="flipToSignUp">SIGN UP</a></div>
                    </td></form>
                </tr>
            </table>
        </div>
        
        
<?php
if(isset($_POST['signin']))
{
	$user=$_POST['user'];
	$passIn=$_POST['pass'];
	$sql="Select * From users";
	$result=mysqli_query($conn,$sql);
	while($row = mysqli_fetch_array($result)){
		if($user==$row["name"] && $passIn==$row["pass"])
		{
			redirect_to("loggedin.php?user=".$user);
		}
	}
		echo "<br><center>Enter Valid Data</center>";
	
		
}
?>

        
        <div id="signUpForm">
            <table border="0" cellspacing="10">
                <tr>
                    <td>
                        <div id="title">SIGN UP</div>
                        <hr size="1px" width="100px" color="black"/>
                    </td>
                </tr>
                <tr>
                    <td>
                       				<form method="post" name="frmsignout" action="">
                       				
                        <input type="text" placeholder="FULL NAME" name="newuser"/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <input type="password" placeholder="PASSWORD" name="newpass"/>
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        <input type="submit" value="SIGN UP" id="signUpBtn" name="signup"/>
                    </td>
                </tr>
                <tr>
                    <td align="center">
                        <div id="signInMsg">HAVE AN ACCOUNT <a href="#" id="flipToSignIn">SIGN IN</a></div>
					</td></form>
               <?php
			if(isset($_POST['signup']))
		{
			$name=$_POST['newuser'];
			$pass=$_POST['newpass'];
			$query2="INSERT INTO users(name, pass)";
			$query2.="VALUES ";
			$query2.="('{$name}','{$pass}')";
			$result2= mysqli_query($conn,$query2);
			if(!$result2){
				echo "Something's wrong Our developers are informed about this...";
					}
			else{
				redirect_to("loggedin.php?user=".$name);
			}
		}
	?>
	
                </tr>
            </table>
        </div>
    </body>
</html>
<?php   
	mysqli_close($conn);	
?>