import folium, numpy as np


class MapSafeFood:
	ZOOM = 10
	TILES = 'Stamen Terrain'
	
	POINT_ICON = 'cloud'
	POINT_COLOR = 'red'
	ICON_CONFIG = {'icon': POINT_ICON,
				   'color': POINT_COLOR}
				   
	LINES_COLOR = 'darkblue'

	def __init__(self, location:tuple, zoom_start:int =ZOOM, tiles:str =TILES, **options) -> None:
		self.mapp = folium.Map(location=location, zoom_start=zoom_start, tiles=tiles, **options)
	
	def AddPoints(self, points:list , popup:str ='Non Data', tooltip:str ='Information',icon_config:dict =ICON_CONFIG, **options) -> None:
		for point in points:
			folium.Marker(point,
						  popup=popup,
						  tooltip=tooltip,
						  icon=folium.Icon(**icon_config),
						  **options).add_to(self.mapp)
	
	def AddLines(self, line:tuple, color:str =LINES_COLOR, **options) -> None:
		folium.PolyLine(line, color=color, **options).add_to(self.mapp)
			
	def AddArrows(self, line:tuple, n_arrows:int = 3, color = 'black', fill_color='red', 
				  number_of_sides=3, radius=10, rotation=180, **options) -> None:
		loc_arrows = zip(np.linspace(line[0][0], line[1][0], n_arrows+2)[1:n_arrows+1],
						 np.linspace(line[0][1], line[1][1], n_arrows+2)[1:n_arrows+1])

		for loc_arrow in loc_arrows:
			folium.RegularPolygonMarker(location=loc_arrow, color=color, fill_color=fill_color, number_of_sides=number_of_sides, 
				radius=radius, rotation=rotation, **options).add_to(self.mapp)		
	
	def AddArrowsLines(self, lines:tuple, **options) -> None:
		for line in lines:
			#self.AddLines(line, **options)
			self.AddLines(line, **options.get('line', {}))
			#self.AddArrows(line, **options)
			self.AddArrows(line, **options.get('arrow', {}))
		
	def save(self, name:str) -> None:
		self.mapp.save(f'{name}.html')

		
def generate_map(origin:tuple, points:tuple, nodes:tuple, arch_name, **options) -> None:
	map_base = MapSafeFood(location=origin, **options.get('opt_init', {}))
	map_base.AddPoints(points, **options.get('opt_points', {}))
	map_base.AddArrowsLines(nodes, **options.get('opt_arrow_lines', {}))
	map_base.save(arch_name)
	

#Caso de prueba.
if __name__ == '__main__':

#	a = MapSafeFood(location=(41.257160, -95.995102), **{})

#	puntos = ((41.257160, -95.995102), (41.357160, -95.895102), (41.157160, -95.795102))
#	a.AddPoints(puntos, popup='Data of BlockChain')

#	a.AddArrowsLines([puntos[:-1], puntos[1:]])

#	a.save('hola')

	
	puntos = ((41.257160, -95.995102), (41.357160, -95.895102), (41.157160, -95.795102))
	generate_map((41.257160, -95.995102), puntos, (puntos[:-1], puntos[1:]), 'hola', **{'opt_points': {'popup': 'Data of BlockChain'}})
	#a.AddPoints(puntos, popup='Data of BlockChain')







