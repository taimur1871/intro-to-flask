from flask import Flask, request, render_template
from inference import get_category, plot_category

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def rock_paper_scissor():
    # Write the GET Method to get the index file

    # Write the POST Method to post the results file

    # Read file from upload
    # Get category of prediction
    # Plot the category
    # Render the result template
    pass


if __name__ == '__main__':
    app.run(debug=True)
