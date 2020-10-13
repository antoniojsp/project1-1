from flask import Flask, request, render_template, make_response, url_for, redirect
import configparser
from werkzeug.utils import secure_filename
import os



# Instantiate the app
app = Flask(__name__)
config = configparser.ConfigParser()
config.read("credentials.ini")
ALLOWED_EXTENSIONS = set(['txt'])

#uploads_dir = os.path.join(app.instance_path, '/upload_folder')
#os.makedirs(uploads_dir, exist_ok=True)



# Helper Function
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

"""Login Page Logic"""
@app.route("/", methods=["GET", "POST"])
def get():

    if request.method == 'POST':
        #if request.form['submitted_data']: # or request.form['password'] != 'admin':
        #    return request.form['submitted_data']
        app.logger.debug('Juicy')
        file_ = request.files['submitted_data']
        app.logger.debug('Juiced')
        if file_.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file_ and allowed_file(file_.filename):
            filename = secure_filename(file_.filename)
            with open(filename) as f:
                app.logger.debug(f)
            #file_.save(os.path.join(uploads_dir, filename))
            #file_.save(os.path.join(config['DEFAULT']['UPLOAD_FOLDER'], str(filename)))
            return redirect(url_for('/',
                                    filename=filename))



    return render_template('submit_data.html')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
