"""
EB-DOCKER-FLASK-MSSQL
by Jeric Macalintal 

A Flask Application for deployment in AWS Elastic Beanstalk Preconfigured with Docker

July 23, 2017
"""

#region Imports
import os
import logging
import sys
import json
import flask
from flask import request, Response,make_response,render_template
import pyodbc
from flask_basicauth import BasicAuth

#endregion

# Create the Flask app
application = flask.Flask(__name__)

#region Environment Variables
# Default config vals
THEME = 'default' if os.environ.get('THEME') is None else os.environ.get('THEME')
FLASK_DEBUG = 'false' if os.environ.get('FLASK_DEBUG') is None else os.environ.get('FLASK_DEBUG')
BASIC_AUTH_USERNAME = '' if os.environ.get('BASIC_AUTH_USERNAME') is None else os.environ.get('BASIC_AUTH_USERNAME')
BASIC_AUTH_PASSWORD = '' if os.environ.get('BASIC_AUTH_PASSWORD') is None else os.environ.get('BASIC_AUTH_PASSWORD')
CONNECTION_STRING = '' if os.environ.get('CONNECTION_STRING') is None else os.environ.get('CONNECTION_STRING')

application.config.from_object(__name__)
application.config.from_envvar('APP_CONFIG', silent=True)
application.config['BASIC_AUTH_USERNAME'] = BASIC_AUTH_USERNAME
application.config['BASIC_AUTH_PASSWORD'] = BASIC_AUTH_PASSWORD
# application.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(application)
#endregion

#region Application Functions

# SQL Query Function
def sql_query(sql,arguments):
    """
        Args:
            sql         (str): SQL Statement.
            arguments   (list of str): List of arguments for the sql Statement.

        Returns:
            results     List of Dictionaries.
    """
    cnxn = pyodbc.connect(CONNECTION_STRING)

    cursor = cnxn.cursor()
    _sqlString = sql
    cursor.execute(_sqlString,arguments)

    columns = [column[0] for column in cursor.description]
    results = []

    for row in cursor:
        results.append(dict(zip(columns, row)))
    cursor.close()
    del cursor

    return results

#endregion

#region Main Web Pages
#Homepage
@application.route('/')
def welcome():
    return render_template("home.html")

#endregion

#region Error Logging

@application.before_first_request
def setup_logging():
        if not application.debug:
            application.logger.addHandler(logging.StreamHandler())
            application.logger.setLevel(logging.INFO)
#endregion

if __name__ == '__main__':
    application.run(host='0.0.0.0')
    application.debug = True
    application.run()
