# Reservoir Manager Tool
Developed by Riley Hales at the Brigham Young University Hydroinformatics Lab 2019. Built on capstone projects completed by Riley Hales, Benjamin Gray, Bri Ihrke, Kate

## Installation Instructions
In addition to the packages installed automatically, you will need to install google-api tools using the following commands.
~~~~
pip install google-auth-oauthlib
pip install --upgrade google-api-python-client
~~~~

## Custom Settings


## Required Data
This app needs:
* A GeoJSON file containing the point locations of each of the reservoirs to be tracked with the property "NAME" containing the full name of the reservoir.
* An excel formatted sheet called bathymetry.xlsx that contains columns named reservoirname_elev and reservoirname_vol for each reservoir.
* An excel sheet called elevations where the daily recorded elevation data are saved.
* a JSON file called sheetscredentials.json containing the api key to the google account where your google sheet is located online
