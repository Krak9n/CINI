In this challenge I had to work with CSRF tokens.
  
Basically, everything started from passing json with **admin** credentials to **/login** page and then I was having the first CSRF token with which I could proceed with completing the challenge.

The logic here is to do a GET request to **/flag_piece** 4 times with each retrieving a piece of a flag. Each of these GETs should contain this query:
```
		/flag_piece?csrf=<CSRF token>&index=<Index of a piece>
```  
  
After everything was successfully ran I had the flag.  