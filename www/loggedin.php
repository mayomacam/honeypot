<?php 
function redirect_to($loc){
		header("Location:".$loc);
	}
$conn=mysqli_connect("localhost","jayhawk","megatronstango","users");
	if(mysqli_connect_errno())
	{
		die("Argue With Programmer to fix this problem !!");
	}
$tbname=$_GET['table'];
$sql="SELECT * from ".$tbname;
$result=mysqli_query($conn,$sql);
$loginName=$_GET['user'];
$table=$_GET['table'];
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
	</style>
</head>

<body>
	<h1>Who's Turn Is It ?</h1>
	<form method="post">
		<input type="submit" id="btn" name="done" value="My Turn is Done">
	</form>
	<h2>
	<?php
		$count=0;
		while($row = mysqli_fetch_array($result)){
		$id[$count]=$row["id"];
		$userName[$count]=$row["name"];
		echo $row['name'];
			echo "<br><br>";
		$count++;
		}
	if(isset($_POST['done']))
	{
		for($i=0;$i<$count;$i++)
		{
			if($userName[$i]==$loginName)
			{
				$id[$i] =$id[$i]+$count;
				for($j=0;$j<$i;$j++)
				{
					if($id[$i]==$id[$j])
						$id[$i]++;
				}
				for($k=$i+1;$k<$count;$k++)
				{	
					if($id[$i]==$id[$k])
						$id[$i]++;
				}
				 $update="UPDATE ".$table." SET id=".$id[$i]." WHERE name='".$userName[$i]."'";
				$recordupdate=$conn->query($update);
				if($recordupdate === TRUE) 
				{
					redirect_to("display.php?table=".$table);
				}
				else{
					echo "Something's wrong Our developers are informed about this...";
					exit();
				}
			
			}
		}
	}
	?>
	</h2>
</body>
</html>
<?php   
	mysqli_close($conn);	
?>