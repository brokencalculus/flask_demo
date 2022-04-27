"""Page rendering simple html."""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def see_cats():
    cat_name = 'Rex'
    return render_template('cats.html', name = cat_name)


if __name__ == '__main__':
    app_debug = True
    app.run()