from django.test import TestCase
from GeoLogic.GeoLogic import GeoLogic
from django.test import Client

class GeoLogicTests(TestCase):
	def test_missing_n_input_status_code(self):
		"""
		A test on response status code when n input is absent
		"""
		c = Client()
		response = c.post('/', {'x': 206880.9, 'y': 77203.13})
		self.assertEquals(response.status_code, 400)
	
	def test_invalid_input_type_status_code(self):
		"""
		A test on response status code when x input is invalid
		"""	
		c = Client()
		response = c.post('/', {'x': 'ninety eight', 'y': 77203.13, 'n': 10})
		self.assertEquals(response.status_code, 400)
	
	def test_point_distance_sort(self):
		"""
		A test on sorting logic, via the api request
		"""	
		c = Client()
		response = c.post('/', {'x': 206880.2, 'y': 77203.13, 'n': 15000})
		data_dict = response.json()['data']
				
		self.assertEquals(response.status_code, 200)
		self.assertEquals(len(data_dict), 15000)
		self.assertEquals(data_dict[0]['id'], 15212)
		self.assertEquals(data_dict[14500]['id'], 7671)
	