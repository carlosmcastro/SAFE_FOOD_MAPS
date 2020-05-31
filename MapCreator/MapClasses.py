import folium, numpy as np

class MapSafeFood:
	MAP_TYPE = folium.Map
	
	ZOOM = 10
	TILES = 'Stamen Terrain'
	
	POINT_ICON = 'cloud'
	POINT_COLOR = 'red'
	ICON_CONFIG = {'icon': POINT_ICON,
				   'color': POINT_COLOR}
				   
	POPUP_TEXT = 'Non Data'
	TOOLTIP_TEXT = 'Information'
				   
	LINES_COLOR = 'darkblue'
	
	N_ARROWS = 3
	ARROWS_COLOR = 'black'
	ARROWS_FILL_COLOR = 'darkred'
	ARROWS_SIDES = 3
	ARROWS_SIZE = 10

	def __init__(self, location:tuple, zoom_start:int = ZOOM, tiles:str =TILES, **options) -> None:
		#We locate the map, and give them an initial design and zoom.
		self.__mapp = folium.Map(location=location, zoom_start=zoom_start, tiles=tiles, **options)
	
	def add_points(self, points:list , popup:str = POPUP_TEXT, tooltip:str = TOOLTIP_TEXT, 
				   icon_config:dict = ICON_CONFIG, **options) -> None:
		#Points, icon, message on mouse over, and click.
		for point in points:
			folium.Marker(point,
						  popup=popup,
						  tooltip=tooltip,
						  icon=folium.Icon(**icon_config),
						  **options).add_to(self.__mapp)
	
	def add_lines(self, line:tuple, color:str =LINES_COLOR, **options) -> None:
		folium.PolyLine(line, color=color, **options).add_to(self.__mapp)
			
	#Ajustar la rotación.
	def add_arrows(self, line:tuple, n_arrows:int = N_ARROWS, color:str = ARROWS_COLOR, 
			fill_color:str = ARROWS_FILL_COLOR, number_of_sides:int =ARROWS_SIDES, 
			radius:int =ARROWS_SIZE, **options) -> None:
		
		#n number of halfway arrows, (x, y)
		loc_arrows = zip(np.linspace(line[0][0], line[1][0], n_arrows+2)[1:n_arrows+1],
						 np.linspace(line[0][1], line[1][1], n_arrows+2)[1:n_arrows+1])
						 
		#The rotated arrow following the direction of the origin line.
		rotation = self.concordant_rotation(line[0], line[1]) - 90

		#We plot the triangles/arrows
		for loc_arrow in loc_arrows:
			folium.RegularPolygonMarker(location=loc_arrow, color=color, fill_color=fill_color, 
				number_of_sides=number_of_sides, radius=radius, rotation=rotation, **options
				).add_to(self.__mapp)		
	
	#The options in this case is a dictionary with the options of lines and arrows
	def add_arrows_lines(self, lines:tuple, **options) -> None:
		for line in lines:
			self.add_lines(line, **options.get('line', {}))
			self.add_arrows(line, **options.get('arrow', {}))
		
	#We saved the map in HTML format
	def save(self, name:str) -> None:
		self.__mapp.save(f'{name}.html')
	
	#Getter of the map.
	@property
	def get_map(self) -> folium.Map:
		return self.__mapp
		
	@staticmethod
	def concordant_rotation(p1, p2):
	#Based on https://gist.github.com/jeromer/2005586
	
		long_diff = np.radians(p2[1] - p1[1])
		
		lat1 = np.radians(p1[0])
		lat2 = np.radians(p2[0])
		
		x = np.sin(long_diff) * np.cos(lat2)
		y = (np.cos(lat1) * np.sin(lat2) 
			- (np.sin(lat1) * np.cos(lat2) 
			* np.cos(long_diff)))
		bearing = np.degrees(np.arctan2(x, y))
		
		#Adjusting for compass bearing	
		if bearing < 0:
			return bearing + 360
		return bearing

	
"""
#Samples Cases.
if __name__ == '__main__':

#	a = MapSafeFood(location=(41.257160, -95.995102), **{})

#	puntos = ((41.257160, -95.995102), (41.357160, -95.895102), (41.157160, -95.795102))
#	a.AddPoints(puntos, popup='Data of BlockChain')

#	a.AddArrowsLines([puntos[:-1], puntos[1:]])

#	a.save('Case1')

	
	puntos = ((41.257160, -95.995102), (41.357160, -95.895102), (41.157160, -95.795102))
	mapa = generate_map((41.257160, -95.995102), puntos, (puntos[:-1], puntos[1:]), 'Case2', 
				 **{'opt_points': {'popup': 'Data of BlockChain'}})

	print(mapa, type(mapa))
"""
