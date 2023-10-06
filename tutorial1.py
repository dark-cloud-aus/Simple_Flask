# My first attempt at a super-basic one page web app using Pytholn and Flask

# Import packages
from flask import Flask

app = Flask(__name__)

# Define the route of the home page
@app.route("/")

def home():
    return"Hello this is my web app <h1>HELLO WORLD<h>"

# This line of code will allow any subpage to typed in the browser (gog.com/) and will display the name of the page entered. 
@app.route("/<name>")
def step1():
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run()




