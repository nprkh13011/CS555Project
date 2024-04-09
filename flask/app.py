
from flask import request, jsonify
from config import app, db
from models import Results
import pandas as pd
import numpy as np
import pickle

machineModel = pickle.load(open('model.pkl','rb'))

@app.route("/results", methods=["GET"])
def get_results():
    results = Results.query.all()
    json_results = list(map(lambda x: x.to_json(), results))
    return jsonify({"results": json_results})


@app.route("/create_result", methods=["POST"])
def create_result():

    #dummy data for demonstration purposes
    EEG = pd.read_csv('RawWavesCombined.csv')
    X_EEG = EEG[['EEG.AF3', 'EEG.T7', 'EEG.Pz', 'EEG.T8', 'EEG.AF4']]
    X_EEG = np.array(X_EEG)
    number_of_rows = X_EEG.shape[0] 
    random_indices = np.random.choice(number_of_rows, size=1, replace=False)
    pred_on_X = X_EEG[random_indices, :]  

    #ideally, we'd want to retrieve some eeg data from a device but for now we'll use the aforementioned dummy data 
    eeg_af3 = pred_on_X[0][0]
    eeg_t7 = pred_on_X[0][1]
    eeg_Pz = pred_on_X[0][2]
    eeg_T8 = pred_on_X[0][3]
    eeg_AF4 = pred_on_X[0][4]
    true_false = machineModel.predict(pred_on_X)[0]

    if not true_false or not eeg_af3 or not eeg_t7 or not eeg_Pz or not eeg_T8 or not eeg_AF4:
        return (jsonify({"message": "details not included"}) , 400,)
    
    new_result = Results(true_false=true_false)
    try:
        db.session.add(new_result)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Complete"}), 201


@app.route("/update_result/<int:result_id>", methods=["PATCH"])
def update_result(result_id):
    result = Results.query.get(result_id)

    if not result:
        return jsonify({"message": "not found"}), 404
    
    data = request.json
    result.true_false = data.get("trueFalse", result.true_false)

    db.session.commit()

    return jsonify({"message": "update complete"})


@app.route("/delete_result/<int:result_id>", methods=["DELETE"])
def delete_result(result_id):
    result = Results.query.get(result_id)

    if not result:
        return jsonify({"message": "not found"}), 404
    
    db.session.delete(result)
    db.session.commit()

    return jsonify({"message": "deletion complete"})



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)




















# from flask import Flask, jsonify,render_template,request
# import pickle
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)


# model = pickle.load(open('model.pkl','rb'))

# @app.route('/', methods = ['GET'])
# def landing_page():
#     return jsonify({"Hello":"World"})

# if __name__ == '__main__':
#     app.run(debug=True)
