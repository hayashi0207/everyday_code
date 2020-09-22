from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hello!!!<h1>'

# @app.route('/post/<post_name>')
# def show_post(post_name):
#     print(type(post_name))
#     return post_name

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     print(type(post_id))
#     return f'{post_id}'

# @app.route('/post/<float:post_id>')
# def show_post(post_id):
#     print(type(post_id))
#     return f'{post_id}'

# @app.route('/post/post')
@app.route('/post/<int:post_id>/<post_str>')
def show_post(post_id,post_str):
    print(type(post_id,post_str))
    return f'{post_id}{post_str}'



if __name__ == '__main__':
    app.run(debug=True)