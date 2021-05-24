from flask import Flask, flash, request ,jsonify, render_template
from werkzeug.utils import secure_filename
from predict_model import * # import predict
import os

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# prob threshold required for making a prediction
prob_threshold = 0.3

# create flask object
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return ('.' in filename) and (filename.rsplit('.', 1)[1].lower() 
                              in ALLOWED_EXTENSIONS)


# create home page
@app.route('/') 
def main():
    return 'Welcome to API'


# request for file upload
@app.route('/upload', methods=['GET', 'POST']) 
def upload_file():
    if request.method == 'POST': 
        if 'file' not in request.files:
            flash('No file part')
            return 'No file part'

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return 'No selected file'

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Save File
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],    
                             'image.png'))
            # preprocess image and predict
            label, y_prob = predictImage('./uploads/image.png')
            if len(y_prob[y_prob > prob_threshold]) >= 2 or len(y_prob[y_prob > prob_threshold]) <= 0:
                label = 'ไม่สามารถระบุชนิดได้ โปรดอัพโหลดภาพมุมอื่น'
            return jsonify({'label': label})

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# request for url
@app.route('/url') 
def predict_img_from_url():
    this_url = request.args.get('p_image_url', default='please provide url', type=str)
    try:
        label, y_prob = predictImageFromURL(this_url)
        print(y_prob)
        print(label)
        if len(y_prob[y_prob > prob_threshold]) >= 2 or len(y_prob[y_prob > prob_threshold]) <= 0:
            label = 'ไม่สามารถระบุชนิดได้ โปรดอัพโหลดภาพมุมอื่น'
    except:
        label = 'URL not valid. Please try other URLs.'
    return jsonify({'label': label})


if __name__ == '__main__':
    # application.debug = False
    # application.run(host='0.0.0.0', port=8080)
    # application.run(debug=False)
    app.run(debug=True)


