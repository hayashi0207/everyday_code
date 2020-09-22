from flask import Flask, render_template

app = Flask(__name__,template_folder='html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/<string:user_name>/<int:age>')
def home(user_name,age):
    login_user = {
        'name' : user_name,
        'age' : age
    }
    return render_template('home.html',user_info = login_user)

@app.route('/userlist')
def user_list():
    users=[
        'Taro','Jiro','Saburo','Shiro','hanako','ichiro'
    ]
    is_login = False
    return render_template('userlist.html',users = users)

if __name__ == '__main__':
    app.run(debug = True)