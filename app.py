from flask import Flask, render_template

# Create Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
    return render_template("index.html")

# localhost:5002/user/john
@app.route('/user/<name>')
def user(name):
    order = ["order1", "order2", "order3"]
    return render_template("user.html", 
        user_name=name,
        order=order
        )


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html" ), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html" ), 500