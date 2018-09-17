from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def successful():
    print('Name: ', request.form['name'])
    print('Location: ', request.form['location'])
    print('Language: ', request.form['language'])
    print('Comments: ', request.form['comments'])
    return render_template('result.html')


@app.route('/danger')
def nope():
    print('\n')
    print('a user tired to visit/danger. we have redirected the user to /')
    print('\n')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
