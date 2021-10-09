## Subarrays with an odd number of odd numbers

<p align="justify">

Implement a function which takes an array of non negative integers and returns  **the number of subarrays**  with an  **odd number of odd numbers**. <br/> 
Note, a subarray is a  _**contiguous subsequence**_.

### Example

Consider an input:
```ruby
[1, 2, 3, 4, 5]
```
The subarrays containing an odd number of odd numbers are the following:
```ruby
[1], [1, 2], [1, 2, 3, 4, 5], 
[2, 3], [2, 3, 4], 
[3], [3, 4], 
[4, 5], 
[5]
```
The expected output is therefore  `9`.

**Expected time complexity is O(n).**
<br/><br/>



## Test
To test the solution, type from the CLI:   
	
	> python tests.py  

</p>
