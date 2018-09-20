from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .serializers import GeoSerializer
from GeoLogic.GeoLogic import GeoLogic

# Create your views here.
class NearestPoints(APIView):
	"""
	View that makes decisions based on the board state and returns a new board state in text.

	* Requires no authentication.
	* Requires no permission.
	"""
	renderer_classes = (JSONRenderer, )  

	def post(self, request, format=None):

		serializer = GeoSerializer(data=request.data)
		if serializer.is_valid():
			geo_logic = GeoLogic('points.csv')

			#method to run with my code
			nearest_n = geo_logic.nearest_n(serializer.data)

			#method to run with 3rd party tools
			#nearest_n = geo_logic.nearest_n_with_package(serializer.data)
			
			return Response({'error': False,'data':nearest_n}, status=status.HTTP_200_OK)
		else:
			return Response({'error': True, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


	
