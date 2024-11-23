# Flask route for handling feedback submission

from flask import Flask, request, jsonify, render_template
import csv

app = Flask(__name__)

# Route to render feedback form
@app.route('/feedback', methods=['GET'])
def feedback():
    # You can dynamically pass the response to be rated in 'response' variable
    response = "Example response from LLM to be rated"
    return render_template('feedback.html', response=response)

# Route to handle feedback submission
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    rating = request.form['rating']
    comments = request.form['comments']
    model_response = request.form['model-response']
    
    # Save feedback to a CSV file
    with open('feedback.csv', mode='a') as feedback_file:
        feedback_writer = csv.writer(feedback_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        feedback_writer.writerow([model_response, rating, comments])
    
    return jsonify(status='success', message='Thank you for your feedback!')

if __name__ == "__main__":
    app.run(debug=True)
