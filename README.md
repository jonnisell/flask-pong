# flask-pong

A simple Flask example based on a tutorial:
https://medium.com/bhavaniravi/build-your-1st-python-web-app-with-flask-b039d11f101c

The app is set up by using the Application Factory pattern with imported settings if needed. I've followed the initial guidelines of the [tutorial of Flask](https://flask.palletsprojects.com/en/stable/tutorial/) and switching Flask for APIFlask project.
Next step involves looking at https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins for references and looking at involing Blueprints dynamically through decorators

## Starting the application

You start the application by setting environment variables and running `flask run` i.e.

`export FLASK_ENV=dev FLASK_APP=__init__.py flask run`
