

class BinarySearch(list):
	def __init__(self, a_length, b_step):

		# get the list class initialised
		super(BinarySearch, self).__init__()

		# Create array with intervals of b_steps
		for element in range(1, a_length + 1):
			self.append(element * b_step)

		#length of list
		self.length = len(self)


	def search(self, search_value):
		first = 0
		last = len(self)-1
		index_value = 0
		found = False

		counter = 0

		if search_value == self[first]:
			index_value = first
			found  = True

		elif search_value == self[last]:
			index_value = last
			found = True

		if search_value not in self:
			found = True
			index_value = -1


		while first <= last and not found:
			middle_value = (first + last)//2

			if self[middle_value] == search_value:
				found = True
				index_value = middle_value

			else:
				counter+=1 # Update counter when ther is an interation

				if  self[middle_value] > search_value:
					last = middle_value - 1
				else:
					first = middle_value + 1


		return {"count": counter,  "index":index_value}




