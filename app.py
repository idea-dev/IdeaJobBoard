from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/jobs')
@app.route('/home')
def jobs():
    return render_template('jobs.jinja2')


@app.route('/applicants', methods=['GET'])
def applicants():
    return render_template('applicants.jinja2')


if __name__ == '__main__':
    app.run()
