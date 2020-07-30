### Project Overview

 The problem statement given was regarding an agency that needed help to decipher a message that they received from their intel using python. It had multiple text files that needed some reading which was possible by performing a few operations in python to get to othe final message.


### Learnings from the project

 After completing this project, I had a better understanding of solving logical problems using python. In this project, I applied the following concepts to accomplish the given target:

String operations (floor division)
Conditional statement and loops (if-elif-else statement)
File I/O (all the file operation - open(),write(),close())
Functions (user-defined and built-in)


### Approach taken to solve the problem

 I created various functions that helped me read files and perform functions on the strings within those files. The different operations performed within those functions were:
1) Floor division on the two parameters of the function and storing the quotient in string format
2) Use if-else statement to substitute the message of the file for a secret message
3) Access two different files to compare the two messages and take only those words that appear in first message but not in second message - used list comprehensions
4) Use Lambda and filter() function to extract only those words from the message in the file that are of even length.
5) Use the split() and join() function to combine all the message bits collected from the above functions into a single message and write it in a file.




