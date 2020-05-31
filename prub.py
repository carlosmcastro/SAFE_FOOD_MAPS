import folium, numpy as np


class MapSafeFood:
	ZOOM = 10
	TILES = 'Stamen Terrain'
	
	POINT_ICON = 'cloud'
	POINT_COLOR = 'red'
	ICON_CONFIG = {'icon': POINT_ICON,
				   'color': POINT_COLOR}
				   
	LINES_COLOR = 'darkblue'

	def __init__(self, location, zoom_start=ZOOM, tiles=TILES, **kwargs):
		self.mapp = folium.Map(location=location, zoom_start=zoom_start, tiles=tiles, **kwargs)
	
	def AddPoints(self, points, popup='Non Data', tooltip='Information',icon_config=ICON_CONFIG, **kwargs):
		for point in points:
			folium.Marker(point,
						  popup=popup,
						  tooltip=tooltip,
						  icon=folium.Icon(**icon_config),
						  **kwargs).add_to(self.mapp)
	
	def AddLines(self, line, color=LINES_COLOR, **kwargs):
		folium.PolyLine(line, color=color, **kwargs).add_to(self.mapp)
			
	def AddArrows(self, line, n_arrows= 3, **kwargs):
		loc_arrows = zip(np.linspace(line[0][0], line[1][0], n_arrows+2)[1:n_arrows+1],
						 np.linspace(line[0][1], line[1][1], n_arrows+2)[1:n_arrows+1])

		for loc_arrow in loc_arrows:
			folium.RegularPolygonMarker(location=loc_arrow, color='black', fill_color='red', number_of_sides=3, 
				radius=10, rotation=180).add_to(self.mapp)		
	
	def AddArrowsLines(self, lines, **kwargs):
		for line in lines:
			self.AddLines(line, **kwargs)
			self.AddArrows(line, **kwargs)
		
	def save(self):
		self.mapp.save('hola.html')

#Caso de prueba.
if __name__ == '__main__':	
	a = MapSafeFood(location=[41.257160, -95.995102])

	puntos = ((41.257160, -95.995102), (41.357160, -95.895102), (41.157160, -95.795102))
	a.AddPoints(puntos, popup='Data of BlockChain')

	a.AddArrowsLines([puntos[:-1], puntos[1:]])

	a.save()







