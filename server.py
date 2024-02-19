from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)

@app.route("/<string:page>")
def html_page(page=None):
    return render_template(page)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    return 'somthing went wrong'