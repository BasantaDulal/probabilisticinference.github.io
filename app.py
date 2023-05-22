from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the table data from the request
    table_data = request.get_json()

    # Perform the calculations and return the updated probabilities
    # Replace this with your actual calculations based on the table data

    return {
        'marginal_probabilities': {...},
        'likelihoods': {...},
        'posteriors': {...},
    }


if __name__ == '__main__':
    app.run(debug=True)
