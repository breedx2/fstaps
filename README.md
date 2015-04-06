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

Docker Container
-----------

Get Container

```
$ docker pull alexwitherspoon/fstaps
```

Run Container

```
$ docker run -p 80:80 -p 222:22 alexwitherspoon/fstaps
```

Use Container

Browse to http://Container-IP:80/

or

SSH as user "root", using password "beer" on port 222.
```
$ ssh -p 222 -l root <Container-IP>
```

Toss Container

```
$ docker ps -a
$ docker stop <instance-id>
$ docker rm <instance-id>
$ docker rmi <image-id>
```

TODO
----
Would be nice to have:
* "Just tapped" sticker for taps within the last business day
* Hyperlinks for more info about a given beer
* [your feature here]
