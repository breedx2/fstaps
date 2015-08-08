from flask import Flask, render_template, request, url_for, redirect
import datetime
import inflect
import yaml

DATAFILE='fstaps.yaml'

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
		d = datetime.datetime.strptime(self.date_tapped, "%Y-%m-%d")
		month_name = d.strftime("%b")
		return "%s %s" % (month_name, inflect.engine().ordinal(d.day))
	def to_dict(self):
		return { 'brewery': self.brewery, 'name': self.name, 'style': self.style, 'abv': self.abv, 'date_tapped': self.date_tapped }
	@staticmethod
	def from_dict(data):
		return Tap(brewery = data['brewery'], name = data['name'], style = data['style'], abv = data['abv'], date_tapped = data['date_tapped'])

def to_dicts(taps):
	return { k: map(lambda x: x.to_dict(), v) for k,v in taps.iteritems() }

def save(data, filename):
	stream = file(filename, 'w')
	yaml.safe_dump(data, stream)

def load(filename):
	stream = file(filename, 'r')
	return yaml.load(stream)

@app.route('/')
def tap_list():
	raw_data = load(DATAFILE) 
	bartaps= { k: map(lambda x: Tap.from_dict(x), v) for k, v in raw_data.iteritems() }
	return render_template('fstaps.html', bars=bartaps)

@app.route('/downstairs')
def downstairs():
	return single_bar_render('downstairs', 'downstairs')

@app.route('/kitchen')
def kitchen():
	return single_bar_render('downstairs', 'kitchen')

@app.route('/upstairs')
def upstairs():
	return single_bar_render('upstairs', 'upstairs')

@app.route('/sprucegoose')
def sprucegoose():
	return single_bar_render('upstairs', 'Spruce Goose')

@app.route('/tenforward')
def tenforward():
	return single_bar_render('upstairs', 'Ten Forward')

def single_bar_render(which_bar, alias):
	if not alias:
		alias = which_bar
	raw_data = load(DATAFILE) 
	bartaps= { k: map(lambda x: Tap.from_dict(x), v) for k, v in raw_data.iteritems() }
	return render_template('fstaps.html', bars={alias: bartaps[which_bar]})

@app.route('/edit', methods=['POST'])
def edit_tap():
	raw_data = load(DATAFILE)
	bartaps= { k: map(lambda x: Tap.from_dict(x), v) for k, v in raw_data.iteritems() }

	barname = request.form['barname']
	index = int(request.form['index']) - 1

	new_tap = new_tap_from_request()
	bartaps[barname][index] = new_tap

	print to_dicts(bartaps)
	save(to_dicts(bartaps), DATAFILE)

	return redirect('/')

def new_tap_from_request():
	name = request.form['name']
	brewery = request.form['brewery']
	style = request.form['style']
	abv = request.form['abv']
	date_tapped = request.form['date_tapped']
	return Tap(name=name, brewery=brewery, style=style, abv=abv, date_tapped=date_tapped)
	

if __name__ == '__main__':
	debug = True
	app.run(host='0.0.0.0', port = 5000, debug = debug)
