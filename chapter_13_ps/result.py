from flask import Flask

app = Flask(__name__)

name = input("Enter you name: ")
marks = int(input("Enter your marks: "))
@app.route("/")
def home():
    if marks>33:
        return f"<h1>{name}, You are Pass</h1>"
    return f"<h1>{name}, You are Fail</h1>"
#     return "<h1>Home Page</h1>"



# Way to apply multiple routes in a single webpage
# @app.route("/about")
# def about():
#     return "<h1>About Page</h1><p>Ye about page hai!</p>"

# @app.route("/contact")
# def contact():
#     return "<h1>Contact Page</h1><p>Email: example@email.com</p>"

# if __name__ == "__main__":
#     app.run(debug=True)


app.run()