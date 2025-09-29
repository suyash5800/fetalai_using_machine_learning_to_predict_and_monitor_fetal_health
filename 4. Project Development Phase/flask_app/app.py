from flask import Flask, request, render_template
import joblib
import numpy as np

RF_model = joblib.load("fetalAI_model.pkl")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    pdec = request.form['prolongued_decelerations']
    abstv = request.form['abnormal_short_term_variability']
    ptabstv = request.form['percentage_of_time_with_abnormal_long_term_variability']
    hv = request.form['histogram_variance']
    hm = request.form['histogram_median']
    mlv = request.form['mean_value_of_long_term_variability']
    hmo = request.form['histogram_mode']
    acc = request.form['accelerations']
    print(pdec, abstv, ptabstv, hv, hm, mlv, hmo, acc)
    x = np.array([pdec, abstv, ptabstv, hv, hm, mlv, hmo, acc])


    output = RF_model.predict(x.reshape(1,-1))
    print(output)

    if output == 1:
        prediction = "Normal"
    elif output == 2:
        prediction = "Suspect"
    else:
        prediction = "Pathological"

    return render_template('index.html', prediction=prediction)



if __name__ == "__main__":
    app.run(debug=True)
