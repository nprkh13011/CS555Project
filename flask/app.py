
from flask import request, jsonify
from config import app, db
from models import Results

@app.route("/results", methods=["GET"])
def get_results():
    results = Results.query.all()
    json_results = list(map(lambda x: x.to_json(), results))
    return jsonify({"results": json_results})


@app.route("/create_result", methods=["POST"])
def create_result():
    true_false = request.json.get("trueFalse")

    if not true_false:
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
