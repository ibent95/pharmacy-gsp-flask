# pharmacy-gsp-flask
Implementation of Generalized Sequential Pattern (GSP) on Pharmacy App in Flask framework

Pre-action :
1. Create virtual environtment
	- macOS/Linux => "python3 -m venv venv"
	- Windows => "py -3 -m venv venv"
2. Activate the virtual environtment
	- macOS/Linux => ". venv/bin/activate"
	- Windows => "venv\Scripts\activate"

Please install these python library:

 1. pip install Flask
 2. pip install Flask-WTF
 3. pip install python-dotenv
 4. pip install python-webpack-boilerplate
 5. pip install PyMySQL
 6. pip install Flask-SQLAlchemy
 7. pip install marshmallow
 8. pip install fpdf

[Opsional]
 9. pip install sqlalchemy-querybuilder
10. pip install autopep8

Don't forget to run MySQL Server and make database `pharmacy_gsp_app`.

Then run 'flask database_init' and 'flask run' in terminal or command prompt.

The app will serve on http://localhost:5000