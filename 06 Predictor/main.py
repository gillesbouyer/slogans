from flask import Flask, request, render_template
from py_GICS_Predict import predictcigs

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_cigs page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_cigs/', methods=['GET', 'POST'])

def render_message():

    # user-entered ingredients
    ingredients = ['Slogan']

    # error messages to ensure correct units of measure
    messages = ["Invalid Slogan"]

    # hold all amounts as floats

    lesdonnees = []
    render_template('index.html', message=" ")
    # takes user input and ensures it can be turned into a floats
    for i, ing in enumerate(ingredients):
        user_input = request.form[ing]
        try:
#            print("aaa",user_input)
            data_entered = str(user_input)
        except:
            return render_template('index.html', message=messages[i])
        lesdonnees.append(data_entered)
#        print("amounts",amounts)
    # show user final message
#    print("before final_message")
    final_message = predictcigs(lesdonnees)
#    print("after final_message")
    return render_template('index.html', message=final_message)

if __name__ == '__main__':
    app.run(debug=True)
