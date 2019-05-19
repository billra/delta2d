# delta2d plotter kinematics
# Bill Ola Rasmussen
# version 0.4

# diagram:
# 
#   ‖                ‖
#  ↑‖a               ‖
#  ↓‖\              b‖↑
#   ‖  \ A          /‖↓
#   ‖    \      B /  ‖
#   ‖      \    /    ‖
#   ‖        \/      ‖
#   ‖       /(ix,iy) ‖
#   ‖     /          ‖
#   ‖   (x,y)        ‖
#   ‖                ‖
# (0,0)            (w,0)
#
# legend:
#
# ‖ = rail
# w = width between rails
# \ = A arm
# / = B arm
# ↑↓ = each arm upper tip travels up and down rail
# (ix,iy) = hinge point where A arm lower tip contacts B arm
# a = A arm upper tip rides on rail at (0,a)
# b = B arm upper tip rides on rail at (w,b)
# (x,y) = resulting position of lower arm tip

import math

class Delta2d:
	'kinematics for delta2d plotter'
	def __init__(self, A_len, B_len, B_tip_len, width):
		'''Create a Delta2d plotter kinematics object
		:param float A_len: length of A arm
		:param float B_len: length of B arm (includes B_tip_len)
		:param float B_tip_len: length from A,B hinge and lower B tip
		:param float width: width between rails'''
		self.A_len = A_len
		self.B_len = B_len
		self.B_tip_amt = B_tip_len / B_len # amount of B length used for tip
		self.width = width

	def ab(self,x,y):
		'inverse kinematics: given a (x,y) position, calculated the required a and b positions'
		B_width = self.width - x # width of rectangle containing arm B
		B_height = math.sqrt(self.B_len ** 2 - B_width ** 2) # height of rectangle containing arm B, using Pythagorean theorem
		b = B_height + y # B arm upper tip at (w,b)
		ix = B_width * self.B_tip_amt + x # ix == A_width, width of rectangle containing arm A
		iy = B_height * self.B_tip_amt + y
		A_height = math.sqrt(self.A_len ** 2 - ix ** 2) # height of rectangle containing arm A, using Pythagorean theorem
		a = A_height + iy # A arm upper tip at (0,a)
		return a,b

	def xy(self,a,b):
		'forward kinematics: given a and b positions, calculated the resulting (x,y) position'
		pass

def main():
	print('creating delta2d object...')
	plotter = Delta2d(10,10,2,10)

	x,y=1,2 # desired x,y coordinates
	print("use ab{0} to get xy{1}".format(plotter.ab(x,y),(x,y)))

	x,y=1.5,2 # desired x,y coordinates
	print("use ab{0} to get xy{1}".format(plotter.ab(x,y),(x,y)))

	x,y=2,2 # desired x,y coordinates
	print("use ab{0} to get xy{1}".format(plotter.ab(x,y),(x,y)))

	print('done.')

if __name__ == "__main__":
	main()

# notes:
# - sphinx syntax https://www.sphinx-doc.org for documentation