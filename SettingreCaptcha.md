## Setting up reCaptcha ##

Vikuit uses reCapcha from google for ensure that the new users are human and not some kind of alien. For setup the reCapcha component you must follow the follow steps:

## Create a reCapcha key. ##

You must create the key on the google's web page. The steps are:

  1. Go to the webpage: https://www.google.com/recaptcha/admin/create

  1. Put your url. If you don't have a domain and you use appspot, use your appspot url. By example, http://yourvikuitname.appspot.com

  1. Note the public and private key

## Configure your vikuit installation for use reCaptcha ##

The next step is configure vikuit for keep it:

  1. Login as admin
  1. Go to Administration->Application Configuration
  1. Set the both keys
  1. After this steps you must see the reCaptcha box when you try to register a user, by example.