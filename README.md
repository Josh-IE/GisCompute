# README #

A Django app that implements an API to obtain from a set of geographical points the first N elements ordered by distance from a given pairs of coordinates in a csv file.

There are 2 methods in the GeoLogic Class that computes the distance and performs sorting

* nearest_n (Default): uses custom code 
* nearest_n_with_package: uses Pandas and Shapely 3rd party tools

The API endpoint input (Content-Type: application/json) are:
* <x:float> X coordinate
* <y:float> Y coordinate
* <n:int> number of points to be returned

A success response format (Content-Type: application/json):
* <error:boolean> false
* <data:list> List of json object datapoints

A failed response format (Content-Type: application/json):
* <error:boolean> true
* <errors:dict> input keys with their respective errors


### Requirements ###

* Django==2.1.1
* djangorestframework==3.8.2
* pandas==0.23.4
* Shapely==1.6.4.post1

### Set up ###

* Clone the repository into a folder on your computer.
* cd into the project folder
* Install requirements. pip install requirements.txt
* cd into the src folder
* Run the command 'python manage.py runserver' in a command line/terminal.
* make a post request to http://localhost:[port]/ or http://127.0.0.1:[port]/, passing the input parameters.

### Tests ###

* cd into the src folder
* Run the command 'python manage.py test' in a command line/terminal.

### Assumptions ###

* The data object in response is ordered in ascending order of distance between input datapoint and datapoints in dataset
