import os
import uuid

from flask import (Flask, flash, redirect, render_template, request,
                   send_from_directory, url_for)

#from style import main 


UPLOAD_FOLDER = './static/images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




# check if file extension is right
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/')
def index():
    return render_template('index.html')

# force browser to hold no cache. Otherwise old result might return.
@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# main flow of programme
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    try:
        # remove older files
        os.system("find static/images/ -maxdepth 1 -mmin +5 -type f -delete")
    except OSError:
        pass
    if request.method == 'POST':
        # check if the post request has the file part
        if 'content-file' and 'style-file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        content_file = request.files['content-file']
        style_file = request.files['style-file']
        files = [content_file, style_file]
        content_name = str(uuid.uuid4()) + ".png"
        style_name = str(uuid.uuid4()) + ".png"
        file_names = [content_name, style_name]
        for i, file in enumerate(files):
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_names[i]))

        #main(UPLOAD_FOLDER+file_names([0], UPLOAD_FOLDER+file_names[1]) 
        #return send_from_directory("./", "genrated.png")
        return send_from_directory(UPLOAD_FOLDER, "genrated.png")
        






if __name__ == "__main__":
    app.run(debug=True)