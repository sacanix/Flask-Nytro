Flask Nytro
===========

Nytro is an extension to help developer providing a set of useful tools
giving even more facility to development apps with Flask.

## Benefits

1. Creates your blueprints with the *template* and *static* folders setted automatically like a app, but another place can be setted with you want.    

2. Allows to attch *blueprins* on app automaticaly by convention or granularity by configuration.    

3. Brings a few (for now) helper functions to create: a slug, a random key and the intermediate table for Many to Many relationship for SQLAlchemy.

##Usage


1. Create a bluepirnt like bellow:    

      
    ```python
    from flask import render_template as render
    from flask.ext.nytro import Blueprint        
            
    bp = Blueprint('my_bp', __name__, url_prefix='/my-bp')    
    
    @bp.route('/')
    def index():
        return render('index.html')    
    ```
2. On the same level of the blueprint file, create the *static* and *templates* folders.
3. In the *templates* folder that you created, create the *index.html* file with any content.
3. Execute the aplication. 
4.

## Instalation
```bash
$ pip install flask-nytro
```
or download/clone the package and

```bash
$ python setup.py install
```


Done, just create your apps and have fun.
