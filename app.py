from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/projects')
@app.route('/home')
def projects():
    return render_template('projects.jinja2')

if __name__ == '__main__':
    app.run()
