# Plant-Disease-Recognition-TensorFlow
This project uses DeepLearning using TensorFlow to recognize disease patterns on various plants<br>

<h3>Click here:</h3><a href="https://farmai-trial.herokuapp.com/">Deployment Link</a>
<h2>Technology Stack</h2>

<h4>Languages used:</h4>
<ul>
  <li>Python~=3.9.13<a href="https://www.python.org" rel="nofollow"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40" style="max-width: 100%;"> </a></li>
 </ul>
  
<h4>Libraries used:</h4>
    <ul>
  <li> TensorFlow<a href="https://www.tensorflow.org" rel="nofollow"> <img src="https://camo.githubusercontent.com/b861b92581ad5a7b81147073d729eda727f71985d72f3dd198e0afd792a6f9de/68747470733a2f2f7777772e766563746f726c6f676f2e7a6f6e652f6c6f676f732f74656e736f72666c6f772f74656e736f72666c6f772d69636f6e2e737667" alt="tensorflow" width="40" height="40" data-canonical-src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" style="max-width: 100%;"> </a></li>
      
  <li>pyrebase<a href="https://firebase.google.com/" rel="nofollow"> <img src="https://camo.githubusercontent.com/dd4b2422ed3bfc9da88c43d18550375c66f9584327dff7ecc19315ce50b96f07/68747470733a2f2f7777772e766563746f726c6f676f2e7a6f6e652f6c6f676f732f66697265626173652f66697265626173652d69636f6e2e737667" alt="firebase" width="40" height="40" data-canonical-src="https://www.vectorlogo.zone/logos/firebase/firebase-icon.svg" style="max-width: 100%;"> </a></li>
 
  <li>BeutifulSoup4</li>
  
  <li>Keras</li>
 </ul>
 <h4>Frameworks used:</h4>
 <ul>
  <li>Flask<a href="https://flask.palletsprojects.com/" rel="nofollow"> <img src="https://camo.githubusercontent.com/cb2324a4c0e1910089f481d56e1f887d6e96114101987dfbb6ef6f9df1e0bf08/68747470733a2f2f7777772e766563746f726c6f676f2e7a6f6e652f6c6f676f732f706f636f6f5f666c61736b2f706f636f6f5f666c61736b2d69636f6e2e737667" alt="flask" width="40" height="40" data-canonical-src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" style="max-width: 100%;"> </a></li>
  </li>
  <li>BootStrap<a href="https://getbootstrap.com" rel="nofollow"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40" style="max-width: 100%;"> </a></li>
</ul>
<h4>Scripts and markup languages used:</h4>
<ul>
  <li>HTML</li>
  <li>CSS</li>
</ul>

 <h4>Containers used:</h4>
 <ul>
  <li>Docker<a href="https://www.docker.com/" rel="nofollow"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40" style="max-width: 100%;"> </a></li>
</ul>

<h4>Deployment and repo platforms used:</h4>
<ul>
  <li>Heroku <a href="https://heroku.com" rel="nofollow"> <img src="https://camo.githubusercontent.com/df12cb598044a3f38efc1f45e3580558c324cf8789b79487125044eeebcc4dee/68747470733a2f2f7777772e766563746f726c6f676f2e7a6f6e652f6c6f676f732f6865726f6b752f6865726f6b752d69636f6e2e737667" alt="heroku" width="40" height="40" data-canonical-src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" style="max-width: 100%;"> </a>
  </li>
  <li>Git <a href="https://git-scm.com/" rel="nofollow"> <img src="https://camo.githubusercontent.com/fbfcb9e3dc648adc93bef37c718db16c52f617ad055a26de6dc3c21865c3321d/68747470733a2f2f7777772e766563746f726c6f676f2e7a6f6e652f6c6f676f732f6769742d73636d2f6769742d73636d2d69636f6e2e737667" alt="git" width="40" height="40" data-canonical-src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" style="max-width: 100%;"> </a></li>
  
</ul>
<h4>Pipeline used:</h4>
<ul>
  <li>CI/CD pipeline using Git Actions</li>
  </ul>

This below image is the projects home page where we can upload the image of a plant's leaf and selected a model to predict.
![Home page](https://user-images.githubusercontent.com/75308799/197596201-07c0a886-455d-4bdb-8e11-44f7d16eae3a.png)

Selecting a model based on thr plant type
![Select model](https://user-images.githubusercontent.com/75308799/197596322-ce926a4c-14a2-4fe5-afa6-94cb95919c6a.png)

The results of our predictions and the scraped content about the disease of the plant is displayed on the result page.
Scraping happens only if the provided leaf imageis not healthy and the result is displayed in red and green in case of healhy leaf.
![result](https://user-images.githubusercontent.com/75308799/197596497-088a6f83-5ba4-4182-8912-9eadf46879c3.png)
