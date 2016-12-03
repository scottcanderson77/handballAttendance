<html>
<head>
	<title>Class Exercise 2</title>
</head>
<body>
	<?php
	$fileptr = fopen("names.txt", "r+");
	
	if(flock($fileptr, LOCK_SH)):
		$match = 0;
		while($currname = fgetss($fileptr)):
				if (strcmp($currname, $_POST["name"]) == 0):
					$yes = 1;
					endif;
					endwhile;
					
				#echo "final match: " . $match;
				if($match == 1):
					echo $_POST["name"] . ", You have already registered.";
			elseif($match==0):
			fwrite($fileptr, $_POST["name"] . "\n");
			echo $_POST["name"] . ", your name has been registered.";
			endif;
			endif;
	
	flock($fileptr, LOCK_UN);
	fclose($fileptr);
	?>
</body>
</html>