from flask import Flask, render_template

app = Flask(__name__)

class Tap(object):
	def __init__(self, brewery = '', name = '', style = None, abv = None, date_tapped = None):
		self.brewery = brewery
		self.name = name
		self.style = style
		self.abv = abv
		self.date_tapped = date_tapped
	def __repr__(self):
		return "%s %s (%s), %s abv, tapped on %s" % (self.brewery, self.name, self.style, self.abv, self.date_tapped)
	def get_index(self, max):
		return (hash(self.name) % max) + 1
	def get_color_index(self, max):
		return (hash("%s%s%s" %(self.name, self.brewery, self.abv)) % max) + 1

@app.route('/')
def tap_list():
	downstairs = [ 
		Tap('Deschutes', 'Mirror Pond', abv = '5', style = 'Pale Ale'), 
		Tap('Something', 'Face Melter', abv = '9.1', date_tapped = '2014-02-01'),
		Tap('Other', 'Another Brew', style = 'Amazeballs')
	]
	upstairs = [
		Tap('Donkey Pond', 'Hair Dog', abv = '7'), 
		Tap('Smarmy Beast', 'Sm00th Times', style = 'Yeti', abv = '5.3'),
		Tap('Oregone', 'Locals Only', abv = '5.2')
	]
	taps = { 'upstairs': upstairs, 'downstairs': downstairs }
	print taps
	return render_template('fstaps.html', **taps)

if __name__ == '__main__':
	debug = True
	app.run(debug = debug)
