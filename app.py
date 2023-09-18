from flask import Flask, render_template,request, jsonify
from utils import make_pred

app = Flask(__name__)

@app.route("/")
def home():
    # text = ""
    # if request.method == "POST":
    #     text = request.form.get("email-content")
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    #if request.method == "POST":
    email_text = request.form.get("email-content")
    predictions = make_pred(email_text)

    return render_template("index.html",predictions=predictions,email_text=email_text)

@app.route("/api/predict",methods=["POST"])
def api_predict():
    data = request.get_json(force=True)
    email_text = data["content"]
    predictions = make_pred(email_text)
    return jsonify({predictions:predictions})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)