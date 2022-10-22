import pyrebase
firebaseConfig={
   'apiKey': "AIzaSyBDmHFnZdkZPuBVmQ6XZLXTqG_LzQiqPtM",
  'authDomain': "farmai-a9eb9.firebaseapp.com",
  'projectId': "farmai-a9eb9",
  'storageBucket': "farmai-a9eb9.appspot.com",
  'messagingSenderId': "661942268532",
  'appId': "1:661942268532:web:459765d66f3dfe5f001721",
  'measurementId': "G-F9M5Z0ZSZB"
}
class Cloudapi:

  def __init__(self,file,filename):
    self.firebase=pyrebase.initialize_app(firebaseConfig)
    self.storage=self.firebase.storage()
    self.file=file
    self.filename=filename

  def upload_img(self):

    self.storage.child(self.filename).put(self.file)

  def get_img_url(self):

    self.url=self.storage.child(self.filename).get_url()
    return self.url
