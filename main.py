from flask import Flask, render_template
from post import Post
import requests


app = Flask(__name__)

blog_url = "https://api.npoint.io/f8b9cce0347af5bc4402"
response = requests.get(blog_url)
response.raise_for_status()
all_posts = response.json()

@app.route('/')
def home():
    global all_posts
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:num>')
def get_post(num):
    for post in all_posts:
        obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        if obj.id == num:
            title = obj.title
            body = obj.body
    return render_template("post.html", title=title, body=body)

if __name__ == "__main__":
    app.run(debug=True)
