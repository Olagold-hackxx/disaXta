#!/usr/bin/python3
""" Flask Application """

from os import environ
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from ...analysis_model import prediction
from ...recognition_model import recognition

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.route("/api/v1/models/analysis", methods=['POST'], strict_slashes=False)
def analysis_model_inference():
    location = request.form['location']
    start_date = request.form['startDate']
    end_date = request.form['endDate']
    disaster_type = request.form['disasterType']
    key = request.form["apiKey"]
    return jsonify(prediction.predict(location, start_date, end_date, disaster_type, key))

@app.route("/api/v1/models/status", strict_slashes=False)
def model_status():
    return jsonify({"status": "OK"})

@app.route("/api/v1/models/recognition", methods=['POST'], strict_slashes=False)
def recognition_model_inference():
    image_file = request.files["image_file"]
    if image_file:
        recognition_response = recognition.process_image(image_file=image_file)
        return jsonify({"status": 200, "data": recognition_response, "ok": True})
    else:
        return jsonify({"status": 400, "error": "Bad request", "message": "image_file must be provided as FormData", "ok": False})

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)



if __name__ == "__main__":
    """ Main Function """
    host = environ.get('MODEL_HOST')
    port = environ.get('MODEL_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '6000'
    app.run(host=host, port=port, threaded=True)

