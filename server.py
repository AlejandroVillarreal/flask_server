from flask import Flask, render_template
app = Flask(__name__)
print(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/<username>/<int:post_id>')
def show_username(username=None,post_id=None):
    return render_template('index.html',name=username,post_id=post_id)