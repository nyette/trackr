from flask import render_template

def handle_error(e):
    return render_template("error.html", e = e), e.code
