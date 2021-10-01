## Volleyball Positions 🏐  

<p align="justify">  
You are watching a volleyball tournament, but you missed the beginning of the very first game of your favorite team. Now you're curious about how the coach arranged the players on the field at the start of the game. <br/><br/>
The team you favor plays in the following formation:

``` ruby
0 3 0        
4 0 2
0 6 0
5 0 1
```
<p align="justify"> 
where positive numbers represent positions occupied by players. After the team gains the serve, its members rotate one position in a clockwise direction, so the player in position 2 moves to position 1, the player in position 3 moves to position 2, and so on, with the player in position 1 moving to position 6.
<br/><br/>
Here's how the players change their positions:

![image](https://user-images.githubusercontent.com/74595044/135637046-8f38f8f7-b41b-4533-bd01-82f429b56e68.png)
	
Given the current  `formation`  of the team and the number of times  `k`  it gained the serve, find the  `initial position`  of each player in it. <br/><br/>

### Example

For
``` ruby
formation = [["empty",   "Player5", "empty"],
             ["Player4", "empty",   "Player2"],
             ["empty",   "Player3", "empty"],
             ["Player6", "empty",   "Player1"]]
and k = 2
```
the output should be

``` ruby
[
    ["empty",   "Player1", "empty"],
    ["Player2", "empty",   "Player3"],
    ["empty",   "Player4", "empty"],
    ["Player5", "empty",   "Player6"]
]
```

For
``` ruby
formation = [["empty", "Alice", "empty"],
             ["Bob",   "empty", "Charlie"],
             ["empty", "Dave",  "empty"],
             ["Eve",   "empty", "Frank"]]
and k = 6
```

the output should be

``` ruby
  [
    ["empty", "Alice", "empty"],
    ["Bob",   "empty", "Charlie"],
    ["empty", "Dave",  "empty"],
    ["Eve",   "empty", "Frank"]
]
```
<br/><br/>
### Input

-   2D string array  `formation`
    
    A  `4 × 3`  array of strings representing names of the players in the positions corresponding to those in the schema above.
    
    It is guaranteed that for each empty position the corresponding element of formation is "empty".
    
    It is also guaranteed that there is no player called "empty" in the team.
    
-   Integer  `k`
    
    The number of times the team gained the serve.
    
    Constraints:  `0 ≤ k ≤ 1000000000.`
    
<br/>
	
### Output

-   2D string array
    
    Team arrangement at the start of the game.

<br/><br/>



## Test
To test the solution, type from the CLI:   
	
	> python tests.py  

</p>
