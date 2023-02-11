#IMPORTING THE REQUIRED PACKAGES AND LIBRARIES 
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('about.html',)

@app.route('/index') 
def index():                                                 
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route("/practice")
def practice():
    """ return the rendered template """
    return render_template("practice.html")


def check_user_input(input):
    try:
        #CONVERTING INTO INTEGER
        val = int(input)
        
    except ValueError:
        try:                                                
            #CONVERTING INTO FLOAT 
            val = float(input)
            
        except ValueError:
            val=str(input)
    return val

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    l=[]
    
    for x in request.form.values() :
         z=x
         if isinstance(check_user_input(x),int)== True:                                      
                x=z
         elif isinstance(check_user_input(x),str)== True:                                    
               if x == 'yes':
                    x=1
               elif x=='no':
                    x=0
               elif x=='regular':
                    x=2
               elif x == 'irregular':
                    x=4

               else:
                   return render_template('practice.html', prediction_text='Kindly enter valid input ')
         else:                                                                                           
               return render_template('practice.html', prediction_text='Kindly enter valid input ')
      
         l.append(int(x))    
    
      
    final_features = [np.array(l)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output == 1:
        output ='You may have PCOS. Kindly consult your nearby doctor.Thank you for filling the form. '
        
    elif output == 0:
        output ='You may not have PCOS.Thank you for filling the form'

    return render_template('practice.html', prediction_text='DO I HAVE PCOS ? {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0',port=8000)
  