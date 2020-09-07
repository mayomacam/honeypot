<?php 
function redirect_to($loc){
		header("Location:".$loc);
	}
$conn=mysqli_connect("localhost","jayhawk","megatronstango","users");
	if(mysqli_connect_errno())
	{
		die("Argue With Programmer to fix this problem !!");
	}
$table = $_GET["table"];
$sql="SELECT * from ".$table;
$result=mysqli_query($conn,$sql);
?>
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Take Turns</title>
  <link href="https://fonts.googleapis.com/css?family=Exo+2|Indie+Flower|Lobster|Oswald|Ubuntu" rel="stylesheet">

 <style>
	body{
		margin: 0px;
		padding: 0px;
		background-color: coral;
		
	}
	 h1{
		 padding: 0px;
		 position: absolute;
		 left: 40%;
		 top:5%;
		 margin: 0px;
		 font-family: 'indie flower';
		 
	 }
	 h2 {
		 padding: 0px;
		 position: absolute;
		 left: 45%;
		 top:15%;
		 margin: 0px;
		 font-family: 'indie flower';
		 text-transform: capitalize;
	 }
	 #btn{
		height:40px;
		width: 200px;
		background-color: royalblue;
		border: none;
		outline: none;
		border: 1px solid whitesmoke;
		position: absolute;
		top:80%;
		left:48%;
		transform: translate(-50%,-50%);
		border-radius: 3px;
		font-family:lobster;
		font-size: 17px;
		color: #2d2d2d;
		cursor: pointer;
		overflow: hidden;
		
	}
	#btn:before{
		content:'';
		height:45px;
		width:0px;
		background-color: whitesmoke;
		position: absolute;
		top:50%;
		left:50%;
		transform: translate(-50%,-50%) skewX(-25deg);
		z-index: -1;
		transition: all .4s;
	}
	#btn:hover:before{
		width: 240px;
	}
	#btn a{
		text-decoration: none;
		color:black;
	}
	
	</style>
</head>

<body>
	<h1>Updated List</h1>
	<h2>
	<?php

		while($row = mysqli_fetch_assoc($result)){
		echo $row['name'];
		echo "<br><br>";
		}
		
	?>
	</h2>
	
<button id="btn" name="btn"><a href="index.php">EXIT</a></button>
</body>
</html>
<?php   
	mysqli_close($conn);	
?>