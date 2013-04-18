What is sillysignin?
--------------------

I used to spend a lot of time working with Google App Engine. One of my favorite GAE features is was that, when you run an app locally (dev_appserver.py), it includes a dead-simple, password-free, simulated login page. Enter any email address in the box, and suddenly you are logged into your app as a user with that email address. 

When you're GAE app is deployed, you get all the benefit of the full-fledged authentication page. If your app worked in the simulator, it should work in production as well.

'sillysignin' is basically that, for plain old Django apps. It provides a dead-simple, dead-standard login page (and authentication provider) that only requires usernames, and automatically creates non-existant accounts.

Needless to say, you shouldn't use this in production. It exists because I'm working on a reusable (I  hope) Django app, and being able to quickly log in as a new user, and not worry about account creation and passwords, is useful.

Make it go
-----------------------

It depends on django-class-based-auth-views, which made my work super easy. If you're writing your own authentication views, you should use it.

* Install it using your favorite method for doing such things(like "pip install django-sillysignon").
* Add sillysignin to your INSTALLED_APPS
* Set AUTHENTICATION_BACKENDS = ('sillysignin.backends.SillyAuthBackend',)
* Map the URL: url(r'^accounts/', include('sillysignin.urls')),

(If you don't want to use /accounts, be sure to configure LOGIN_URL and LOGOUT_URL appropriately)

What will the future bring?
------------------------

It might be fun if you could "decorate" another authentication app, such that it automatically uses the your "real" authentication system in production, but uses sillysignin while your developing (maybe on DEBUG=True?)

