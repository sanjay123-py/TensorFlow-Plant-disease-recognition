import keras.models
import tensorflow as tf
import os
import numpy as np
class model:
    def __init__(self,filename,selected_model):
        self.filename=filename
        self.selected_model=selected_model

        self.labels={"Apple_model" : ['Apple Scab disease',
                              'Apple Black_rot',
                              'Apple edar_apple_rust',
                              'Apple healthy'],
        "Corn_model" : ['Corn_(maize) Cercospora_leaf_spot Gray_leaf_spot',
                             'Corn_(maize) Northern_Leaf_Blight',
                             'Corn_(maize) healthy'],
        "Peach_model" : ['Peach Bacterial_spot',
                              'Peach healthy'],
        "Tomato_model" : ['Tomato Bacterial_spot',
                               'Tomato Early_blight',
                               'Tomato Late_blight',
                               'Tomat Leaf_Mold',
                               'Tomato Septoria_leaf_spot',
                               'Tomato Spider_mites Two-spotted_spider_mite',
                               'Tomato Target_Spot',
                               'Tomato Tomato_Yellow_Leaf_Curl_Virus',
                               'Tomato Tomato_mosaic_virus',
                               'Tomato healthy'],
        "Potato_model" :['Potato Early_blight',
                               'Potato Late_blight',
                               'Potato healthy'],
        "Grape_model" : ['Grape Black_rot',
                              'Grape Esca_(Black_Measles)',
                              'Grape Leaf_blight_(Isariopsis_Leaf_Spot)',
                              'Grape healthy'],

        "StrawBerry_model" : ['Strawberry Leaf_scorch',
                                   'Strawberry healthy'],
        "Cherry_model" : ['Cherry_(including_sour) Powdery_mildew',
                               'Cherry_(including_sour) healthy']
        }

    """
    Load and preprocess the data,the main duty of this function is to convert the images into 3 channeled
    numerical data and rescale it by 1/255. and expands the dimension at axis 1
    thats because of the batch_size is the first dimension 
    structure is od dimesnion: (batch_size,width,height,channels)
    """

    def load_and_prep_data(self,path):
        img = tf.io.read_file(path)
        # decode the image into tensor
        tensor = tf.io.decode_image(img, channels=3)

        image = tf.image.resize(tensor, [256, 256])
        # normalize the image
        image = image / 255.

        # we need to expand the first axis beacuse of batch size
        image = tf.expand_dims(image, axis=0)
        # (1,256,256,3)
        return image

    '''
    Given the preprocessed image data and model for a specific class used to predict the patterns
    wand gives the probability of each classes
    '''

    def predict_and_visualize(self):
        pro_image = self.load_and_prep_data(self.filename)

        #Selecting a random model form the selected plant model from [model2.h5,model3.h5]
        #Because both the models performs good and so i decided to use bothnthe models

        random_model=np.random.choice([x for x in os.listdir(f"Tensorflow_Plant_disease_recognition_model/{self.selected_model}") if x.endswith('.h5')])
        model=keras.models.load_model (f"Tensorflow_Plant_disease_recognition_model/{self.selected_model}/{random_model}")
        pred= model.predict(pro_image)

        #In case of multi-class labels we use the condtion pred[0]>1
        if(len(pred[0])>1):
            index=tf.argmax(pred[0])
            return self.labels[self.selected_model][index]
        # if pred[0] == 1 then it is an binary classification problem
        else:
            index=int(np.round(pred[0][0]))
            return self.labels[self.selected_model][index]

