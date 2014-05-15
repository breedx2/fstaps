from flask import Flask, render_template
import yaml

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
	def nice_tap_date(self):
		if self.date_tapped is None:
			return None
		return "Mar. 23rd"
	def to_dict(self):
		return { 'brewery': self.brewery, 'name': self.name, 'style': self.style, 'abv': self.abv, 'date_tapped': self.date_tapped }
	@staticmethod
	def from_dict(data):
		return Tap(brewery = data['brewery'], name = data['name'], style = data['style'], abv = data['abv'], date_tapped = data['date_tapped'])

def to_dicts(taps):
	return { k: map(lambda x: x.to_dict(), v) for k,v in taps.iteritems() }

def save(data, filename):
	stream = file(filename, 'w')
	yaml.dump(data, stream)

def load(filename):
	stream = file(filename, 'r')
	return yaml.load(stream)

@app.route('/')
def tap_list():
	raw_data = load('fstaps.yaml')
	taps = { k: map(lambda x: Tap.from_dict(x), v) for k, v in raw_data.iteritems() }
	return render_template('fstaps.html', **taps)

if __name__ == '__main__':
	debug = True
	app.run(debug = debug)
