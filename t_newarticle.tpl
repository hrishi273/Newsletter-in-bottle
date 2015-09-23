<!DOCTYPE html>
<html>
<head>
	<title>Newsletter</title>
</head>
<body>
	<h1>Add New Article</h1>
	<br>
	<form action="/newarticle" method="POST"  enctype="multipart/form-data">
		<table>
			<tr>	
				<td>Title:</td>
				<td><input type="text" name="title"></td>
			</tr>
			<tr>
				<td>Body:</td>
				<td><textarea rows="8" name="body"></textarea></td>
			</tr>
			<tr>	
				<td>Choose image:</td>
				<td><input type="file" name="data"></td>
			</tr>
		</table>
		<br>
		<input type="submit"></td>
	</form>
</body>
</html
