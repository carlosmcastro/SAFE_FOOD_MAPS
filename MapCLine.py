import argparse
import string, json
from MapFuncs import generate_map

def clean_arg(arg):
	valid = f'{string.digits}(,.-)' 
	return "".join([c for c in arg if c in valid])

def convert_type(*args):
	origin, points, nodes= map(eval, map(clean_arg, args[:3]))
	name = args[3]
	options = json.loads(args[4].replace("\'", "\""))
	return origin, points, nodes, name, options


parser = argparse.ArgumentParser()

parser.add_argument("-g", "--generate", action='store', nargs=5, 
					help='Generate a HTML map for SafeFood visualization', 
					type=str, metavar= ('Origin', 'Points', 'Nodes', 'Name', 'Options'), 
					dest='generate_map')

args = parser.parse_args()
new_args = convert_type(*args.generate_map)
basic_parameters = new_args[:4]
options = new_args[4]

generate_map(*basic_parameters, **options)


