

class BinarySearch(list):
	def __init__(self, a_length, b_step):

		# get the list class initialised
		super(BinarySearch, self).__init__()

		# Create array with intervals of b_steps
		for element in range(1, a_length + 1):
			self.append(element * b_step)

		#length of list
		self.length = len(self)


	def search(self, value):
		first = 0
		last = len(self)-1
		index_value = 0
		found = False

		counter = 0

		# if value == self[first]:
		# 	index_value = first
		# 	found  = True

		# elif value == self[last]:
		# 	index_value = last
		# 	found = True

		# if value not in self:
		# 	found = False
		# 	index_value = -1


		while first <= last and not found:
			middle_value = (first + last)//2

			if self[middle_value] == value:
				found = True
				index_value = middle_value

			else:
				counter+=1 # Update counter when ther is an interation
				if value < middle_value:
					last -= 1
				else:
					first += 1
				print ("___%d ___ %d ___last %d") %(counter, middle_value, first)


		return {"count": counter,  "index":index_value}

b = BinarySearch(20, 1)
#print b
print(b.search(16))




