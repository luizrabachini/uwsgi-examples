Cheaper
=======

Basic config to test applications running using auto scalling provided by [uWSGI Cheaper Subsystem](http://uwsgi-docs.readthedocs.io/en/latest/Cheaper.html).


Tests
-----

Using [ab](https://httpd.apache.org/docs/2.4/programs/ab.html), was performed 5 concurrent requests with a total of 100 requests.


Results
-------

Using two static workers:

```
Requests per second:    1.00 [#/sec] (mean)
Time per request:       5011.098 [ms] (mean)
Time per request:       1002.220 [ms] (mean, across all concurrent requests)
```

Using initially two workers and scale up by 1 to maximum of 10 workers:

```
Requests per second:    2.19 [#/sec] (mean)
Time per request:       2287.894 [ms] (mean)
Time per request:       457.579 [ms] (mean, across all concurrent requests)
```
