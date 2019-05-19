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
#   ‖       /        ‖
#   ‖     /          ‖
#   ‖   (x,y)        ‖
#   ‖                ‖
# (0,0)            (w,0)
#
# legend:
#
# ‖ = rail
# \ = A arm
# / = B arm
# ↑↓ = each arm upper tip travels up and down rail
# a = A arm upper tip rides on rail at (0,a)
# b = B arm upper tip rides on rail at (w,b)
# (x,y) = resulting position of lower arm tip

class Delta2d:
	'kinematics for delta2d plotter'
	def __init__(self, a_len, b_len, b_tip_len, width):
		'''Create a Delta2d plotter kinematics object
		:param float a_len: length of A arm
		:param float b_len: length of B arm (includes b_tip_len)
		:param float b_tip_len: length from A,B hinge and lower B tip
		:param float width: width between rails'''
		pass
	def ab(self,x,y):
		'inverse kinematics: given a (x,y) position, calculated the required a and b positions'
		pass
	def xy(self,a,b):
		'forward kinematics: given a and b positions, calculated the resulting (x,y) position'
		pass

def main():
	print('creating delta2d object...')
	plotter = Delta2d(10,10,2,10)
	print('done.')

if __name__ == "__main__":
	main()

# notes:
# - sphinx syntax https://www.sphinx-doc.org for documentation