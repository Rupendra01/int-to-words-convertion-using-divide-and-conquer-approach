# int-to-words-convertion-using-divide-and-conquer-approach
in this project we are converting integers to english words using divide and conquer approach in python 3.
* iam constructing both indian and international number system
* i have done this project using gui(Pyqt5) and normal python code.
* i have used digital cheque book as gui.

# Divide and Conquer approach
Let’s simplify the problem by representing it as a set of simple sub-problems. One could split the initial integer 1234567890 on the groups containing not more than three digits 1.234.567.890. That results in representation 1 Billion 234 Million 567 Thousand 890 and reduces the initial problem to how to convert 3-digit integer to English word. One could split further 234 -> 2 Hundred 34 into two sub-problems : convert 1-digit integer and convert 2-digit integer. The first one is trivial. The second one could be reduced to the first one for all 2-digit integers but the ones from 10 to 19 which should be considered separately.

![daa project](https://user-images.githubusercontent.com/62048538/131243668-7bb22755-fc75-4f4f-bc1f-ad95fdd39fac.png)

