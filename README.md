# flask-sse-demo
A demo using SSE to create an event stream from a flask application

To get started, run pip install

```sh
pip install -r requirements.txt
```

And start an instance of Redis. If you have Docker installed, you can start a local Redis server with:

``` sh
docker run --name redis-sse -p 6379:6379 -d redis
```

Next, start up the main web server:

```sh
gunicorn app:app --worker-class gevent --bind 127.0.0.1:5000
```

In two new terminal windows start the event emitter and the listener.

```sh
python events.py
```

```sh
python listen.py
```
