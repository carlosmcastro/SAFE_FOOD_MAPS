import argparse
import string, json
from MapCreator.MapFuncs import generate_map

#We clean up the data, to prevent improper executions
#For tuples
def clean_arg(arg:str) -> str:
	valid = f'{string.digits}(,.-)' 
	return "".join([c for c in arg if c in valid])

#We convert from tuple strings, and take advantage of the json module, to extract the dictionary.
def convert_type(*args) -> tuple:
	origin, points, nodes= map(eval, map(clean_arg, args[:3]))
	name = args[3]
	options = json.loads(args[4].replace("\'", "\""))
	return origin, points, nodes, name, options


parser = argparse.ArgumentParser()

#It takes 5 string parameters, and stores them in a list.
parser.add_argument("-g", "--generate", action='store', nargs=5, 
					help='Generate a HTML map for SafeFood visualization', 
					type=str, metavar= ('Origin', 'Points', 'Nodes', 'Name', 'Options'), 
					dest='generate_map')

args = parser.parse_args()
new_args = convert_type(*args.generate_map)

#Basic and optional parameters for the map design.
basic_parameters = new_args[:4]
options = new_args[4]

#Lo generamos.
generate_map(*basic_parameters, **options)

"""
Sample:

MapCline.py "(41.257160, -95.995102)" "((41.257160, -95.995102), (41.357160, -95.895102), (41.157160, -95.795102))" "(((41.257160, -95.995102), (41.357160, -95.895102)), ((41.357160, -95.895102), (41.157160, -95.795102)) )" "hola" "{'opt_points': {'popup': 'Data of BlockChain'}}"

"""
