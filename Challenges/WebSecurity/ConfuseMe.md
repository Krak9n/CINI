The main vulnerability here is *Type Juggling*.
In the source we can see this comparison.  
```php
  ($user_input == substr(md5($user_input), 0, 24))  
```

The main problem here is that php in this context does **Loose comparison** which means: both variables have the same value. If the variables are of different types then php will try to convert them automatically.

We can use this magic number to exploit this vulnerability: `0e1137126905`. PHP would interpret this payload as a scientific number and the hash as a float.   
Read more [here](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md).