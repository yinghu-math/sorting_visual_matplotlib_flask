from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def get_gif():
    file_name = request.args.get("sort_method")
    if file_name:
        img_url = url_for('static', filename=file_name)
        return render_template("index.html", filename = file_name, img_url = img_url)
    return render_template("index.html", filename = file_name)

if __name__=="__main__":
    app.run()
