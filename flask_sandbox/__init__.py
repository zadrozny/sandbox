from flask import Flask
from flask import render_template
app = Flask(__name__)    

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)	

@app.route('/q/<int:n>')
def child(n):
    return render_template('%d.html' % n)	


if __name__ == '__main__':
	app.run(debug=True)
