from flask import Flask, render_template, url_for, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    if request.method == 'POST':
        message = request.form['message'] 
        blobline = TextBlob(message) 
        detect = blobline.detect_language() 
        return render_template('result.html',prediction = detect)

if __name__ == '__main__': 
    app.run(debug=True)
