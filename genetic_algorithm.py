import random 
import math
from operator import *

def find_fitness(binary_number):
	fitness = math.pow(binary_number,2)
	return fitness

def generate_number (bounds):
	binary_string = ""
	rand = bool(random.getrandbits(1))

	for i in range(bounds):
		if rand == True:
			binary_string+='1'
		else:
			binary_string+='0'
		rand = bool(random.getrandbits(1))

	return binary_string

def generate_list (number_bounds, list_bounds):
	number_list = []
	for i in range(list_bounds):
		number_list.append(generate_number(number_bounds))
	return number_list

def return_integer (binary_string):
	count = len(binary_string) - 1
	integer_number = 0
	for bit in binary_string:
	    if bit == '1':
	    	integer_number += math.pow(2,count)
	    count-=1
	return find_fitness(integer_number)

def generate_tuples (binary_string_list):
	tuple_array = []
	for i in binary_string_list:
		tuple_array.append((i,return_integer(i)))
	return tuple_array

def mutate (binary_string):
	binary_string = list(binary_string)
	if (binary_string[-1] == '0'):
		binary_string[-1] = '1'
	else:
		binary_string[-1] = '0'
	return "".join(binary_string)

def cross (parent1, parent2):
	cross = random.randint(1,3)
	return parent1[0:cross] + parent2[cross:]


number_list = generate_list(5,20)
number_list = number_list.sort(key = return_integer)
print (number_list)
# tuple_list = generate_tuples(number_list)
# sort tuple list by integer value in descending order
# tuple_list.sort(key=itemgetter(1), reverse=True)
#split the tuple list in half to get the optimal half
# tuple_list = tuple_list[0:int(len(tuple_list)/2)]



