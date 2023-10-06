from flask import Flask, render_template

# ==========
# init Flask
# ==========

app = Flask(__name__)

# ==========
# API Routing
# ==========

# instead of hardcoding HTML, we will use the render_template method
# ALL template must be inside the "templates" folder
# ALL static files (css, image, etc) must be inside the "static" folder

# chrome will cache your static file, so if you add static file, just hold SHIFT and click the reload button on chrome
@app.route("/")
def home_page():
    return render_template("index.html")


# ==============
# Activate Flask
# ==============

if __name__ == "__main__":
    app.run(debug=True)