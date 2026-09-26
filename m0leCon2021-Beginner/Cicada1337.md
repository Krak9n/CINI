First step was to decode the original image with xxd. After digging into decoded hex we get this url: [https://postimg.cc/WdNhTrMR](https://postimg.cc/WdNhTrMR) which leads us to another image, **pidgey**.

---

Inside pidgey we find a link to another image [https://postimg.cc/7bz4c6Jg](https://postimg.cc/7bz4c6Jg), **congratulations**.

---

Examine congratulations.jpg with exiftool. There will be these next fields.
```
Image Width                     : 641
Image Height                    : 587
...
Image Description               : 1033
```  

After multiplying these 3 prime number you get the name of the subreddit: **r/388683811**.

---

```py
k = """{A KOAN}
A MAN DECIDED TO GO AND STUDY WITH A MASTER
HE WENT TO THE DOOR OF THE MASTER
"WHO ARE YOU WHO WISHES TO STUDY HERE" ASKED THE MASTER
THE STUDENT TOLD THE MASTER HIS NAME
"THAT IS NOT WHO YOU ARE, THAT IS ONLY WHAT YOU ARE CALLED
WHO ARE YOU WHO WISHES TO STUDY HERE" HE ASKED AGAIN
THE MAN THOUGHT FOR A MOMENT, AND REPLIED "I AMA PROFESSOR"
"THAT IS WHAT YOU DO, NOT WHO YOU ARE," REPLIED THE MASTER
"WHO ARE YOU WHO WISHES TO STUDY HERE"
CONFUSED, THE MAN THOUGHT SOME MORE
FINALLY, HE ANSWERED, "I AM A HUMAN BEING"
"THAT IS ONLY YOUR SPECIES, NOT WHO YOU ARE
WHO ARE YOU WHO WISHES TO STUDY HERE", ASKED THE MASTER AGAIN
AFTER A MOMENT OF THOUGHT, THE PROFESSOR REPLIED "I AM A CONSCIOUSNESS INHABITING AN ARBITRARY BODY"
"THAT IS MERELY WHAT YOU ARE, NOT WHO YOU ARE
WHO ARE YOU WHO WISHES TO STUDY HERE"
THE MAN WAS GETTING IRRITATED
"I AM," HE STARTED, BUT HE COULD NOT THINK OF ANYTHING ELSE TO SAY, SO HE TRAILED OFF
AFTER A LONG PAUSE THE MASTER REPLIED, "THEN YOU ARE WELCOME TO COME STUDY" """
first = [9, 19, 5, 1, 14, 19, 12, 7, 5, 20, 6, 16, 20, 8, 17, 2, 9, 20, 19, 15, 8, 16, 18, 1]
second = [43, 50, 35, 1, 41, 10, 11, 44, 23, 11, 58, 22, 63, 12, 27, 34, 4, 34, 57, 35, 44, 80, 29, 8]
for i in range(len(first)):
	print(k[first[i]:second[i]])
```