from bottle import *
import pymongo,gridfs

connection_string="mongodb://te3143:te3143@192.168.4.91:27017/te3143db"

@route("/")
def root():
	return template("t_welcome")
	
@get("/signup")
def getSignup():
	return template("t_signup")
	
@post("/signup")
def postSignup():
	uname=request.forms.get("user")
	password=request.forms.get("password")
	
	connection=pymongo.Connection(connection_string,safe=True)
	db=connection.te3143db
	names=db.names
	
	nameMap={"uname":uname,"password":password}
	
	names.insert(nameMap)
	
	return "Sign up Successful!!"
	
@get("/signin")
def getSignin():
	return template("t_signin")
	
@post("/signin")
def postSignin():
	uname=request.forms.get("user")
	password=request.forms.get("password")
	
	connection=pymongo.Connection(connection_string,safe=True)
	db=connection.te3143db
	names=db.names
	
	unameList=names.find()
	
	for n in unameList:
		if(n["uname"]==uname):
			return redirect("/newsletter")
		
	return redirect("/signup")
	
@get("/signout")
def signout():
	return redirect("/")

@get("/newsletter")
def blog():
	connection=pymongo.Connection(connection_string,safe=True)
	db=connection.te3143db
	entries=db.entries

	entryList=entries.find()
	
	fs = gridfs.GridFS(db)
	images=db.fs.files
	imageList=images.find()
	imgname=[]
	for n in imageList:
		imgname.append(n["filename"])
	
	return template("t_newsletter",entryList=entryList,imgname=imgname)

@get("/newarticle")
def getNewPost():
	return template("t_newarticle")

@post("/newarticle")
def postNewPost():
	connection=pymongo.Connection(connection_string,safe=True)
	db=connection.te3143db
	entries=db.entries

	title=request.forms.get("title")
	body=request.forms.get("body")
	newEntry={"title":title,"body":body}
	entries.insert(newEntry)
	
	fs = gridfs.GridFS(db)

	data=request.files.get('data')
	img_content=data.file.read()
	fname=data.filename

	fs.put(img_content,filename=fname)

	return redirect("/newsletter")

@route('/static/img/gridfs/<filename>')
def gridfs_img(filename):
	connection = pymongo.Connection(connection_string,safe=True)
	db = connection.te3143db
	fs = gridfs.GridFS(db)
	thing = fs.get_last_version(filename=filename)
	response.content_type = 'image/jpeg'
	return thing

run(host='localhost',port=8082,debug=True)
