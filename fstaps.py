from flask import Flask, render_template

app = Flask(__name__)

class Tap(object):
	def __init__(self, brewery = '', name = '', abv = ''):
		self.brewery = brewery
		self.name = name
		self.abv = abv

@app.route('/')
def tap_list():
	downstairs = { 
		'left': Tap('Deschutes', 'Mirror Pond', '5'), 
		'middle': Tap('Something', 'Face Melter', '9.1'),
		'right': Tap('Other', 'Another Brew', '4.5')
	}
	upstairs = { 
		'left': Tap('Donkey Pond', 'Hair Dog', '7'), 
		'middle': Tap('Smarmy Beast', 'Sm00th Times', '5.3'),
		'right': Tap('Oregone', 'Locals Only', '5.2')
	}
	taps = { 'upstairs': upstairs, 'downstairs': downstairs }
	print taps
	return render_template('fstaps.html', **taps)

if __name__ == '__main__':
	debug = True
	app.run(debug = debug)
