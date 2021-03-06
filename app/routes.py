from app import app
from flask import render_template, jsonify, request
import time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bookTitles', methods=["POST"])
def bookTitles():

    # Get start and end point for book titles to generate
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    # Generate list of Book Titles
    data = []
    for i in range(start, end + 1):
        data.append("Book Title #{}".format(i))

    # Artificially delay speed of response, this caused problems
    #       with the counter, but the scroll workd fine when it is off
    #time.sleep(1)

    return jsonify(data)
