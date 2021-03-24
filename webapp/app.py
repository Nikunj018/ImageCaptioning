import flask
import pickle
from flask import render_template,redirect,request
from captioning import generate_desc

app = flask.Flask(__name__, template_folder='templates') # Construct an instance of Flask class for our webapp

# model = pickle.load(open('model.pkl','rb')

@app.route('/')
def main():
    return(flask.render_template('main.html'))

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        f = request.files['input_image']
        path = "./static/uploaded images/{}".format(f.filename) #save uploaded image
        f.save(path)
        #output = "generated caption"
        #img = Image.open(img_path)
        
        output = generate_desc(path)

        result_dic = {
            'image' : path,
            'caption' : output
        }

    # return render_template('main_return.html', generated_caption='Generated Caption :  {}'.format(output))
    return render_template('main_return.html', generated_caption=result_dic)

if __name__ == '__main__':  #Script executed directly
    app.run(debug=True)  # Launch built-in web server and run this Flask webapp

