## Tower of Hanoi

There are **three towers**. 
The objective of the game is to move all the disks *(1 disc can be changed per move)* over to tower #3, but **you can't place a larger disk onto a smaller disk**. 

![Tower of Hanoi](https://edabit-challenges.s3.amazonaws.com/tower_of_hanoi.gif "Tower of Hanoi")

Create a function that takes a number `discs` *(always a positive integer)* as an argument and returns the **minimum amount** of **steps needed** to **complete the game**.

### Examples
``` ruby
towerHanoi(3) ➞ 7

towerHanoi(5) ➞ 31

towerHanoi(0) ➞ 0