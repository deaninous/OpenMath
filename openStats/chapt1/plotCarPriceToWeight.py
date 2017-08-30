from matplotlib import pyplot as plt 
weight = []
price = []
i = 0
car_link = '../Data from openintro.org/cars.txt'
with open(car_link) as cars:
	clean_cars = cars.readlines()[1:]
	for car in clean_cars:
		c = car.split("\t")
		weight.append(float(c[5].replace('\n', "")))
		price.append(float(c[1]))
plt.scatter(weight, price)
plt.show()
