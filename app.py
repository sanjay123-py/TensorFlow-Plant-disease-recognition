import os
import sys
from flask import Flask,render_template,url_for, request,flash,redirect
from Model import model

#Create an app
app=Flask(__name__)
app.secret_key="sanjay"

#Allowe file extensions
ALLOWED_EXTENSION=['jpeg','jpg','png']


#Home page
@app.route("/",methods=['POST','GET'])
def home():
    return render_template("index.html")

'''
Funtion to check whether the extension of the uploaded file is in ALLOWED_EXTENSION list
'''

def check_file_name(filename:str):
    if(filename.split(".")[-1].lower() in ALLOWED_EXTENSION):
        return True
    return False

'''
Get and save the image and redirect the image for preprocessing and prediction of the image
'''

@app.route("/get_img",methods=["POST"])
def get_img():
    if request.method=='POST':
        if("image" not in  request.files):
            flash("No image is selected.",category="error")
            return redirect(url_for("home"))
        plant_image=request.files['image']

        if(plant_image.filename==''):
            flash("No image is selected to be uploaded",category="error")
            return redirect(url_for("home"))

        if(not check_file_name(plant_image.filename)):
            flash("File with .jpeg, .jpg, .png is only accepted.",category="error")
            return redirect(url_for("home"))
        selected_model=request.form.get("sel_mod")
        if(selected_model=="None"):
            flash("No Model is selected.",category="error")
            return redirect(url_for("home"))
        else:
            plant_image.save(os.path.join("static/uploads/",plant_image.filename))
            return redirect(url_for("predict",image_name=plant_image.filename,selected_model=selected_model))

# After redirecting from the get_img we predict the disease and that is done by model class from Model.py

@app.route('/<image_name>/<selected_model>',methods=['POST','GET'])
def predict(image_name,selected_model):
    try:
        image_path = os.path.join("static/uploads/",image_name)
        model1=model(image_path,selected_model)
        prediction=model1.predict_and_visualize()
        return render_template("result.html",path=image_path,prediction=prediction)
    except:
        flash("Someting error happend",category="error")
        return redirect(url_for("home"))
if __name__ == '__main__':
    app.run(port=4321)