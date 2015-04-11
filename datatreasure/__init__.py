from flask import Flask, url_for
import os
import re

datatreasure = Flask(__name__)

# Determines the destination of the build. Only usefull if you're using Frozen-Flask
datatreasure.config['FREEZER_DESTINATION'] = os.path.dirname(os.path.abspath(__file__))+'/../build'

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
datatreasure.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)


###############################################################################################################
# Custom Filters

#Auto Subscript any sequence of digits
def subnumbers_filter(input):
	return re.sub("\d+", lambda val: "<sub>" + val.group(0) + "</sub>", input)

#Adding the filters to the environment
datatreasure.jinja_env.filters['subnumbers'] = subnumbers_filter
###############################################################################################################



from datatreasure import views
