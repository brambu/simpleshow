simpleshow
------------

a simple flask slideshow

  1. edit config (config/config.yaml) 

  2. bootstrap app
  ~~~
  bash app_bootstrap.sh
  ~~~

  3. run
  ~~~
  python run-app.py
  ~~~


or if you want to uwsgi here is an example:
(after bootstrap)

~~~
uwsgi --ini /path/to/simpleshow/simpleshow-uwsgi.ini
~~~

example of a nginx vhost:
~~~
upstream simpleshow {
  server unix:///tmp/simpleshow_uwsgi.sock;
  }
server {
  listen 8000;
  server_name simpleshow.example.com;
  charset utf-8;
  location /static {
    alias /path/to/simpleshow/app/static;
  }
  location / { 
  uwsgi_pass simpleshow;
  include /etc/nginx/uwsgi_params;
  }
}

~~~
