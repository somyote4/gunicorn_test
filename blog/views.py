from flask import Blueprint

blog_app = Blueprint('blog_app', __name__)

@blog_app.route('/')
def index():
    return "<h1 style='color:blue'>Hello There!</h1>"