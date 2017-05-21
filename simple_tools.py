def circumference(radius):
	'''
	Takes a number, the radius of a circle.
	Returns the circumference of the corresponding circle.
	'''
	
 	circumference = (radius * 2) * math.pi
 	return circumference
 
 def area(radius):
 	'''
	Takes a number, the radius of a circle.
	Returns the area of the corresponding circle.
	'''
 	area = (radius ** 2) * math.pi
 	return area
 
 def convert2kilometers(miles):
	'''
	Takes a number, miles.
	Returns the converted value in kilometers.
	'''
 	kilometers = 1.6 * miles
 	return kilometers
 
 def total_seconds(years, days, hours, minutes, seconds):
	'''
	Takes 5 parameters: years, days, hours, minutes, and seconds.
	Returns the total number of seconds from that value.
	'''
 	total_seconds = (years * 24 *365 *3600) + (days * 24*3600) + (hours * 3600) + (minutes * 60) + seconds
 	return total_seconds
 
 def perimeter(height, width):
 	'''
	Takes the height and width of a rectangle.
	Returns the perimeter of the corresponding rectangle.
	'''
 	perimeter = 2*width + 2*height
 	return perimeter
 
 def area(height, width):
  	'''
	Takes the height and width of a rectangle.
	Returns the area of the corresponding rectangle.
	'''
 	area = width * height
	return area
