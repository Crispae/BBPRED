from flask import Flask,render_template,request,jsonify,make_response
from processing import Predictor
app = Flask(__name__)

predict_object = Predictor()


@app.route("/")
def index():
    return  render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == "POST":
        data = request.get_json(force=True)
        smiles = data["smiles"]
        algo = data["algo"]
        if (smiles) and (algo) :
            try:
                smiles_data = predict_object.test_data(smiles)
                final_result = predict_object.final_predict(smiles_data)
            except ValueError:
                return jsonify({'result' : 'Predcition Error occured!'})
            print(final_result)
            return jsonify({'result' : final_result[0]})
        return jsonify({'result' : 'Missing data!'})
    else:
        return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"),404

        


if __name__ == "__main__":
    app.run(debug=True)
