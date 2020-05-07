from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/projects')
@app.route('/home')
def projects():
    return render_template('projects.jinja2')


@app.route('/support')
def support():
    return render_template('support.jinja2')


@app.route('/about')
def about():
    return render_template('about.jinja2')


if __name__ == '__main__':
    app.run()
