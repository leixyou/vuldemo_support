from flask import Flask, request, url_for, render_template, redirect


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/evil.yml")
def start():
    return render_template("evil.yml")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337)
	


