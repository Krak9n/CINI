Basically, you have to find the correct password.
To do this you could find the **default.js** file. There will be a lot of things but the most important ones are the variable **s3cr37**, the **AES_decrypt** function, and this line:
```js
AES_decrypt('U2FsdGVkX1/JEKDXgPl2RqtEgj0LMdp8/Q1FQelH7whIP49sq+WvNOeNjjXwmdrl', s3cr37) === password_field.value
```
Speaking in simple words, to find the flag one could just paste the decrypt function and just paste the s3cr37 value into input.  