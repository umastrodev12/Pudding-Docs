from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pudding_docs_home():
    return render_template ("index.html")

@app.route("/info-apache-pudding-docs")
def pudding_apache():
    return render_template ("apache-license-info.html")

if __name__== "__main__":
    app.run(debug=True)