from flask import Flask, request, render_template
from inference import get_category, plot_category

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

@app.route('/', methods=['GET', 'POST'])
def rock_paper_scissor():
    # Write the GET Method to get the index file
    if request.method == 'POST':
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect('index.html')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
        render_template('index.html')
        
    # Write the POST Method to post the results file


    # Read file from upload
    # Get category of prediction
    # Plot the category
    # Render the result template
    
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
