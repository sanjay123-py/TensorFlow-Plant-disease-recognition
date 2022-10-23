import os
import sys
from flask import Flask,render_template,url_for, request,flash,redirect
from Model import model
from scrap import ScrapExplanation
from Firebase.storage import Cloudapi
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

            # plant_image.save(os.path.join("static/uploads/",plant_image.filename))

            store_image=Cloudapi(plant_image,plant_image.filename)
            url=store_image.url
            url=url.replace('/','`')

            return redirect(url_for("predict",image_url=url[8:],selected_model=selected_model))
# After redirecting from the get_img we predict the disease and that is done by model class from Model.py

@app.route('/<image_url>/<selected_model>',methods=['POST','GET'])
def predict(image_url:str,selected_model):

    try:
    # image_path = os.path.join("static/uploads/",image_name)
        image_url=image_url.replace('`',"/")
        model1=model("https://"+image_url,selected_model)
        prediction=model1.predict_and_visualize()
        color='color:rgb(255, 50, 0);'
        if("healthy" in prediction.lower()):
            description=ScrapExplanation()
            color='color:green;'
            return render_template("result.html",path="https://"+image_url,
                                   prediction=prediction,
                                   scrap=description.content,
                                   color=color)
        else:
            description=ScrapExplanation(prediction)
            if(len(description.content)==0):
                return render_template("result.html", path="https://" + image_url,
                                       prediction=prediction,
                                       scrap=["Google scrapping limit exceeds...Sorry!!"], color=color)
            return render_template("result.html", path="https://"+image_url,
                                   prediction=prediction,
                                   scrap=description.content,
                                   color=color)
    except:
        flash("Someting error happend",category="error")
        return redirect(url_for("home"))
if __name__ == '__main__':
    app.run(debug=True)