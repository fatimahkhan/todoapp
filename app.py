from flask import Flask, render_template


app = Flask(__name__)

items = {
    1: "do shopping",
    2: "homework",
    3:"tidy"
}






@app.route('/')
def index():
    return render_template("index.html",todos=items)



if __name__ == '__main__':
    app.run(debug=True)
