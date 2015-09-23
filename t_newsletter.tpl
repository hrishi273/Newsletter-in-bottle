<!DOCTYPE html>
<html>
<head>
	<title>Newsletter</title>
</head>
<body>

WEB NEWSLETTER<a href="/signout" style="float:right">Sign out</a><br><hr>

%for entry1,img in zip(entryList,imgname):
<div class="grid">
	<div class="col-1-2" style="float:left;width:70%;">
		<h2>{{entry1["title"]}}</h2>
		<p>{{entry1["body"]}}</p>
	</div>
	<div class="col-2-2" style="float:left;width:30%;">
		<img src="/static/img/gridfs/{{img}}" width="300px">
	</div>
</div>
%end
<br>
<a href="/newarticle">Add Article</a>
</body>
</html>
 
