# FlashGiving
A website platform for running a charitable flashmob

To stay informed about developments, pls fill out [this form](http://goo.gl/forms/rQpKVNsWLH6ydXnk2).

Join the  [Hipchat Room](https://www.hipchat.com/gjl1uenL0) at: https://www.hipchat.com/gjl1uenL0

## Get up and running

Everything is setup using Docker.

    docker-compose up -d
    
Open locally with

    http://192.168.99.100:8000/
    
> note the ip may be different, check yours using `docker-machine ip`

### Testing with payment gateways

Payment gateways may not like redirceting to localhost. To get around this, add a domain in your `/etc/hosts`: 

```
127.0.0.1       stage.flashgiving.co.za
```

Where 127.0.0.1 is the IP you use to test locally.
Now you can test payment gatways e2e

## Running tests: 

**Running  continiously:**

```
docker-compose run --rm web sniffer
```

**Once off**
```
docker-compose run --rm python manage.py test
```

**Multi-environment:**

```
docker-compose run --rm tox
```