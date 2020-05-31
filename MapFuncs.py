from MapClasses import MapSafeFood

#From a few parameters, it generates an HTML map
def generate_map(origin:tuple, points:tuple, nodes:tuple, arch_name:str, **options) -> MapSafeFood.MAP_TYPE:
	
	map_base = MapSafeFood(location=origin, **options.get('opt_init', {}))
	map_base.add_points(points, **options.get('opt_points', {}))
	map_base.add_arrows_lines(nodes, **options.get('opt_arrow_lines', {}))
	map_base.save(arch_name)
	
	return map_base.get_map
