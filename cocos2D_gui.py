#!/usr/bin/env python3

# try to import the cocos module and import to our namespace the .actions from the cocos module
try:
	import cocos
	from cocos.actions import *
except:
	print('Cannot import cocos. Did you run \'pip install cocos2d\' ?')

# define a simple HelloWorld() class that inherits from cocos.layer.ColorLayer (making it a sub-class of it)
# Difference between .Layer and .ColorLayer is, well, you can Colorize
class HelloWorld(cocos.layer.ColorLayer):
	# __init__ is run every time you instantiate the class
	def __init__(self):
		# Always call super in the constructor, we taint the layer with r:64 g:64 b:224 alpha:255
		super(HelloWorld, self).__init__(64,64,224,255)
		# label will become an object with all the necessary to display a text, with font TimesNewRoman and it will be center-anchored
		# Note: .Label is a subclass of CocosNode
		label = cocos.text.Label('Hello, world', font_name='Times New Roman', font_size=32, anchor_x='center', anchor_y='center')
		# set the position of our text to x:320 y:240
		label.position = (320, 240)
		# add our label as a child. It is a CocosNode object, which know how to render themselves.
		self.add(label)
		# sprite becomes a .Sprite object with our molecule picture
		sprite = cocos.sprite.Sprite('sprites/molecule.png')
		# set the position of our sprite to x:320 y;240 the default position is x:0 y:0
		sprite.position = (320,240)
		# scale the sprite 2x
		sprite.scale = 2
		# add our sprite as a child and make sure it is on top by defining the z-axis, default is z: 0
		self.add(sprite, z=1)
		# create a ScaleBy action object that scales our sprite 3x during 2 seconds
		scale = ScaleBy(3, duration=2)
		# Repeat the scale action plus the revers of the scale action to our label
		label.do(Repeat(scale + Reverse(scale)))
		# Repeat the reverse of our scale action plus the scale action to our sprite
		sprite.do(Repeat(Reverse(scale) + scale))
		self.add_label()

	def add_label(self):
		label = cocos.text.Label('gigi', font_name='Times New Roman', font_size=32, anchor_x='center', anchor_y='center')
		# set the position of our text to x:320 y:240
		label.position = (20, 20)
		# add our label as a child. It is a CocosNode object, which know how to render themselves.
		self.add(label)


# our main function
def main():
	# We initialize the director, that takes care of our main window
	cocos.director.director.init()
	# We instantiate hello_layer with our HelloWorld() class
	hello_layer = HelloWorld()
	# All CocosNode objects can execute actions, so we can execute ONE rotate action on ALL of our layers. 360deg-turn in 10 seconds
	hello_layer.do(RotateBy(360, duration=10))
	# Now we create a .Scene and pass our HelloWorld() object stored in hello_layer, as a child
	main_scene = cocos.scene.Scene(hello_layer)
	# All setup now. Let's run our main_scene
	cocos.director.director.run(main_scene)
	# The above could have been compacted to:
	# cocos.director.director.run(cocos.scene.Scene(HelloWorld()))

if __name__ == '__main__': main()