sa-nginx
========

[![Build Status](https://travis-ci.org/softasap/sa-nginx.svg?branch=master)](https://travis-ci.org/softasap/sa-nginx)


Basic role for nginx based deployments (like MEAN stack)

Adjusts folder structure to be apache style (i.e. sites-available, sites-enabled)

Adjusts hashbucketsize for longer domains.


Example of usage:

```YAML

     - {
         role: "sa-nginx"
       }


```


Usage with ansible galaxy workflow
----------------------------------

If you installed the `sa-nginx` role using the command


`
   ansible-galaxy install softasap.sa-nginx
`

the role will be available in the folder `library/softasap.sa-nginx`
Please adjust the path accordingly.

```YAML

     - {
         role: "softasap.sa-nginx"
       }

```




Copyright and license
---------------------

Code is dual licensed under the [BSD 3 clause] (https://opensource.org/licenses/BSD-3-Clause) and the [MIT License] (http://opensource.org/licenses/MIT). Choose the one that suits you best.

Subscribe for roles updates at [FB] (https://www.facebook.com/SoftAsap/)

