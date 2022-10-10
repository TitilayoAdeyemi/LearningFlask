# from crypt import methods
from turtle import title
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

## I tampered with line 393 in 'validators.py'

app = Flask(__name__)
app.config['SECRET_KEY'] = '9e5f6290fe31f1cea01f9bc48654bf16'
posts = [
    {
        'author' : 'Jane Doe',
        'title' : 'Blog post',
        'content' : 'New post content',
        'date' : 'October 2020'
    },
     {
        'author' : 'John Doe',
        'title' : 'Cooking recipe',
        'content' : 'Jollof rice recipe',
        'date' : 'January 2021'
    },
     {
        'author' : 'Julian Doe',
        'title' : 'Crime report',
        'content' : 'What happened to spiderman',
        'date' : 'December 1994'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About ')

@app.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title= 'Register', form = form)

## when using a url_for, what follows is the name of the function not the name of the route

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title= 'Login', form = form)

if __name__ == '__main__':
    app.run(debug=True)
