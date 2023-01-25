# callback-test-server

Simple python server for debugging webhooks or other HTTP callbacks.

This server binds to a host and port that you specify (http://<host>:<port>).
It listens for any POST request sent to that address and simply prints the 
request to the console.

## Testing Local Services

Testing a local service or API which uses webhooks is straight forward.
For example, let's say you are using http://localhost:9000 as your test 
callback URL.

You can run:

```sh
python callback_server.py --port 9000
```

The server will listen for POST requests to that URL and print any requests to 
the console.

## Testing External/Public Services

Processing inbound webhooks from an external service can be difficult to do 
locally when the external service cannot reach your local machine. One 
solution is to set up a webhook proxy. UltraHook is a free webhook proxy 
service.

### Setting Up UltraHook

To use UltraHook:

- Go to http://www.ultrahook.com/register and register
- Copy your api key and development URL
- Store your key and install ultrahook by running:

```sh
      echo "api_key: [API_KEY]" > ~/.ultrahook
      gem install ultrahook
```

### Using UltraHook

Let's say our namespace is 'bob' and we want to set up a webhook proxy to 
http://localhost:9000. We could run the following:

```sh
      ultrahook example localhost:9000
```

This would forward all requests to https://bob-example.ultrahook.com to 
http://localhost:9000


With ultrahook running and forwarding requests we could configure the 
external service to use our ultrahook URL as the callback. In this example: 
https://bob-example.ultrahook.com

Then you could run the test server to print out the webhook requests:

```sh
python callback_server.py --port 9000
```

