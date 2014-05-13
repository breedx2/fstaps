from flask import Flask, render_template

app = Flask(__name__)

class Tap(object):
	def __init__(self, brewery = '', name = '', abv = ''):
		self.brewery = brewery
		self.name = name
		self.abv = abv
	def get_index(self, max):
		return (hash(self.name) % max) + 1
	def get_color_index(self, max):
		return (hash(self.name + self.brewery + self.abv) % max) + 1

@app.route('/')
def tap_list():
	downstairs = [ 
		Tap('Deschutes', 'Mirror Pond', '5'), 
		Tap('Something', 'Face Melter', '9.1'),
		Tap('Other', 'Another Brew', '4.5')
	]
	upstairs = [
		Tap('Donkey Pond', 'Hair Dog', '7'), 
		Tap('Smarmy Beast', 'Sm00th Times', '5.3'),
		Tap('Oregone', 'Locals Only', '5.2')
	]
	taps = { 'upstairs': upstairs, 'downstairs': downstairs }
	print taps
	return render_template('fstaps.html', **taps)

if __name__ == '__main__':
	debug = True
	app.run(debug = debug)
