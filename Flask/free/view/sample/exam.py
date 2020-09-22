from flask import Flask

app = Flask(__name__)

@app.route('/hello:')
def show_hello():
    return '<h1>こんにちは</h1>'

@app.route('/hello/<post_a>/<post_b>:')
def show_post(post_a,post_b):
    return f'こんにちは{post_a}{post_b}'

@app.route('/hello/<int:post_id_a>/<int:post_id_b>:')
def show_post_id(post_id_a,post_id_b):
    plus = post_id_a+post_id_b
    return f'{plus}'

if __name__ == '__main__':
    app.run()