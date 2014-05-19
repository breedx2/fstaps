FlightStats taps
================

This project is a simple HTML display board for the taps at FlightStats.
It adopts the ubiquitous chalkboard model, including some chalk-fonts
and blinding pastels.

It's written in python + flask with a little hand-rolled html + jquery.
Data is persisted in a yaml file.

There is no security -- any user can edit the tap list.  
It should go without saying that the yaml file checked into github is strictly
for development and does not reflect the current tap list (in fact, it's fake!)

Please fork this project and make moar awesomer!  Thanks!

Install/Run
-----------

```
$ virtualenv --no-site-packages env
$ source env/bin/activate
$ easy_install flask PyYAML inflect 
$ python fstaps.py
```