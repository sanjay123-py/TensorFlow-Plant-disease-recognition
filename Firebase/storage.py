import pyrebase
import time

#Configuration for the api creation
firebaseConfig={
   'apiKey': "AIzaSyBDmHFnZdkZPuBVmQ6XZLXTqG_LzQiqPtM",
  'authDomain': "farmai-a9eb9.firebaseapp.com",
  'projectId': "farmai-a9eb9",
  'storageBucket': "farmai-a9eb9.appspot.com",
  "databaseURL" : "",
  'messagingSenderId': "661942268532",
  'appId': "1:661942268532:web:459765d66f3dfe5f001721",
  'measurementId': "G-F9M5Z0ZSZB"
}

class Cloudapi:

  def __init__(self,file,filename1):
    self.firebase=pyrebase.initialize_app(firebaseConfig)
    #initialize the instance of pyrebase with the defined configuration that links my project in firebase
    self.storage=self.firebase.storage()
    self.file=file
    self.filename1=filename1
    #upload the images to the firebase bucket
    self.storage.child(self.filename1).put(self.file)
    time.sleep(1)
    #get the link of the uploaded image
    self.url=self.storage.child(self.filename1).get_url(None)
