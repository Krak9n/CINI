My approach here is quite simple.  
Initial goal was too find the sum of ten biggest elements.  
  
To achieve this I just sorted the input Vector in decreasing order, removed everything besides 10 first elements, and summed what remained. Of course if the Vector is less than 10 elements we should just return its sum.  