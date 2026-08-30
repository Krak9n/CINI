In this challenge I had to implement a basic spider that would go over all links on the page and look for a flag inside of the h1 tags.   
  
Basically my spider just:
+ checks if a page contains an h1 header  
+ finds all of the links present on the page  
+ goes through the links  
+ checks if the current link has been already visited   
+ repeats from the start until no unvisited links left  
  
My approach sucks because I have to then search for any occurence of `flag{`.  