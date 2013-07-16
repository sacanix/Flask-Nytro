Flask Nytro
===========

Nytro is an extension to help the developers providing a set of useful tools
giving even more facility to development apps with Flask.

## Benefits

1. Create your blueprints with the *templates* folder and *static* folder assigned automatically like a app, but another place can be assigned if you want.    

2. Allows to attach *blueprins* on app automatically by convention or granularly through configuration.    

3. Brings a few (for now) helper functions to create: a slug, a random key and the intermediate table for many-to-many relationship for SQLAlchemy.

##Quick Tutorial


1. Create the bluepirnt **simple_bp.py** inside app folder, with the content like below:    

      
    ```python
    from flask import render_template as render
    from flask.ext.nytro import Blueprint        
            
    bp = Blueprint('my_bp', __name__, url_prefix='/my-bp')    
    
    @bp.route('/')
    def index():
        return render('index.html')    
    ```
2. On the same level of the blueprint file, create the *static* folder and *templates* folder.

3. In the *templates* folder that you just created, create the **index.html** file with any content, also create the **foo.txt** file with a some content in the *static* folder that you, too, just created. 


4. In the file that creates the flask app, import the nytro Blueprint and add  **Blueprint.attach_all(app)**. Something like this:
    ```python 
    from flask import Flask
    from flask.ext.nytro import Blueprint

    #Creates an app
    app = Flask(__name__)

    
    #Attaches all blueprints to app automatically by convention or configuration
    Blueprint.attach_all(app)    
    ```
    

5. In your **settings.py** file add the option **BLUEPRINTS** as tuple of import paths. Like below:
    ```python
    BLUEPRINTS = (
        'my_app.simple_bp',
        #or
        'simple_bp'
        #if the blueprint file is imediatally inside the app folder
    )
    ```
    In this way you can enable and disable blueprints through configuration, like django pluggable apps.
    
       **HINT:** You can put the BLUEPRINT option where you prefer, for example, inside the module that create the Flask app.
       
       By convention, you can load blueprints automatically. To do that, just create a ***blueprints*** folder inside the app folder and create them there. But, for this approach, is required to work the blueprint as package. For more information see the **sample**. Also you can change the folder that holds the blueprints that will be loaded automatically through option BLUEPRINTS_FOLDER.

6. Execute the aplication. 

7. Try access http://127.0.0.1:5000/my-bp/ to render the **index.html** template.

8. Try access http://127.0.0.1:5000/my-bp/static/foo.txt to show the content of **foo.txt**.


Please, see the **sample** for a better understand.

## Installation
```bash
$ pip install flask-nytro
```
or download/clone the package and

```bash
$ python setup.py install
```


Have fun.
