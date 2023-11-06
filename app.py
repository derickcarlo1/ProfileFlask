from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/work')
def redirect_to_github():
    github_url = 'https://github.com/derickcarlo1?tab=repositories'
    return redirect(github_url)

@app.route('/touppercase', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/areaOfTriangle', methods=['GET','POST'])
def triangle_area():
    result= None
    if request.method == 'POST':
        base = float(request.form.get('base',''))
        height = float(request.form.get('height',''))
        result = 0.5 * base * height
    return render_template('areaOfTriangle.html',result=result)

@app.route('/areaofcircle', methods=['GET', 'POST'])
def areacircle():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        result = 3.14*(int(radius)**2)
    return render_template('areacofcircle.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
