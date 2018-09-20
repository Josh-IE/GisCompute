import csv
import math
import json
from shapely.geometry import Point
import pandas as pd


class GeoLogic:
	
	def __init__(self, dataset_path):
		"""
		argument dataset_path: path to the dataset csv
		"""
		self.dataset_path = dataset_path

	def nearest_n(self, params):
		"""
    	returns a list of n coordinates in ascending order of the distance between params['x','y'] coordinate and each coordinate in the dataset
		
		Args:
        params (dict): Dictionary containing x, y, n keys

		Returns:
        List: list of objects
    	"""
		x = float(params['x'])
		y = float(params['y'])
		n = int(params['n'])
		matrix = []
		response_list = []
		
		with open(self.dataset_path) as csvDataFile:
			csvReader = csv.reader(csvDataFile, delimiter=';',)
			next(csvReader) # skip header
			for row in csvReader:
				distance = self.distance( [x, y], [float(row[1]), float(row[2])] )
				matrix.append( [int(row[0]), float(row[1]), float(row[2]), distance] )

		matrix.sort(key=lambda m:m[3])		
		trimmed_matrix = matrix[0:n]

		for z in trimmed_matrix:
			response_list.append(
				{
					"id": z[0],
					"x": z[1],
					"y": z[2]
				}
			)
		return response_list

	def distance(self, coord_one, coord_two):
		"""
    	computes distance between 2 coordinates
    	"""
		distance = math.sqrt( ((coord_one[0]-coord_two[0])**2)+((coord_one[1]-coord_two[1])**2) )
		return distance


	def nearest_n_with_package(self,params):
		"""
    	returns a list of n coordinates in ascending order of the distance between params['x','y'] coordinate and each coordinate in the dataset
			using the pandas and shapely package
		Args:
        params (dict): Dictionary containing x, y, n keys

		Returns:
        List: list of objects
    	"""
		x = float(params['x'])
		y = float(params['y'])
		n = int(params['n'])
		
		request_point = Point(x, y)
		df = pd.read_csv(self.dataset_path, delimiter=';')
			
		def distance_calc(row):
			data_point = Point(float(row['x']), float(row['y']))
			return request_point.distance(data_point)

		df['distance'] = df.apply(distance_calc, axis=1)

		sorted_df = df.sort_values(by=['distance'])
		sorted_df = sorted_df.reset_index(drop=True)

		trimmed_df = sorted_df.drop('distance', axis=1).head(n)		
		json_string = trimmed_df.to_json(orient = "records")
		
		return json.loads(json_string)

	