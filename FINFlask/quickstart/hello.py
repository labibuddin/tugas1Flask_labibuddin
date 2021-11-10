from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
   return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
   return 'Post %d'% post_id
@app.route('/hi')
def hi():
   return 'Hi, Guys'
if __name__ == "__main__":
    app.run()
