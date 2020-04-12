from flask import Flask, escape, request, render_template
import pickle

app = Flask(__name__)


file = open('model.pkl', 'rb')

clf = pickle.load(file) 

file.close()

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        mydict = request.form
        print(mydict)
        fever = int(mydict['fever'])
        bodyPain = int(mydict['bodyPain'])
        age = int(mydict['age'])
        # sex = int(mydict['sex'])
        runnyNose = int(mydict['runnyNose'])
        diffBreathe = int(mydict['diffBreathe'])
        abroadHist = int(mydict['abroadHist'])
        test_symptoms = [[fever, bodyPain, age, runnyNose, diffBreathe, abroadHist]]
        infProb = clf.predict_proba(test_symptoms)[0][1]
        return render_template("result.html", inf=round(infProb * 100))         
    return render_template("index.html")
@app.route('/contact')
def contact():
    return render_template("contact.html")
@app.route('/about')
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.run('localhost', 8000, debug=True)

