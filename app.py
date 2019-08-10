from flask import *
import pdfsplitter
app=Flask(__name__)


@app.route("/")
def upload():
    return render_template("file_upload.html")


@app.route("/success",methods=["POST"])
def success():
    success.start_page=int(request.form['start'])
    success.end_page=int(request.form['end'])
    f=request.files['file']
    success.file_name=f.filename
    f.save(success.file_name)
    return render_template("success.html",start=success.start_page,
                           end=success.end_page,name=success.file_name)

@app.route("/convert")
def cropper():
    pdfsplitter.cropper(success.start_page,success.end_page,success.file_name)
    return render_template("download.html")



@app.route("/download")
def download():
    filename=success.file_name.split(".")[0]+"cropped.pdf"
    return send_file(filename,as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
