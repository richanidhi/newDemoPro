
from flask import Flask, redirect, url_for, request
app=Flask(__name__)

@app.route('/hello')
def hello_world():
	return 'Hello World'


@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello %s!' % name


@app.route('/blog/<int:postID>')
def show_blog(postID):
	return 'Blog number is %d' % postID

@app.route('/rev/<float:revNo>')
def show_revision(revNo):
	return 'Revision number is %f' % revNo


@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name

@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		user= request.form['nm']
		return redirect(url_for('success',name=user))
	else:
		user= request.args.get('nm')
		return redirect(url_for('success', name=user))	

if __name__ == '__main__':
	app.debug=True
	app.run()
	app.run(debug = True)
