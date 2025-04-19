from flask import Flask, request, render_template

app = Flask(__name__)

users = { "test1": "Password1@", "test2": "Password2#" }

@app.route('/')
def view_form():
    return render_template( "/Volumes/DRIVE/BAP/TEMPLATES/MAIN.html" )

@app.route( "/handle_post", methods = [ "POST" ] )
def handle_post():
    uname = request. form[ "username" ]
    pwd = request. form[ "password" ]
    if uname in users and users[ uname ] == pwd:
        return "<h1>Welcome !!!< /h1>"
    else:
        return "<h1>invalid credentials !< /h1>"

if __name__ == '__main__':
    app.run( port = 9001 )