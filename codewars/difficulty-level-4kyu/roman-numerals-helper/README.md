## Roman Numerals Helper 

<p align="justify">
Create a <b>RomanNumerals class</b> that can <b>convert</b> a roman numeral to and from an integer value. <br/>
It should follow the API demonstrated in the  examples below. <br/>
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. <br/>
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range :  `1 <= n < 4000`

In this kata  `4`  should be represented as  `IV`, NOT as  `IIII`  (the "watchmaker's four").

### Examples

```ruby
RomanNumerals.to_roman(1000)  # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
```

### Help
```ruby
Symbol    Value 
   I        1
  IV        4
   V        5
   X       10
   L       50
   C      100
   D      500
   M     1000
   ```
<br/><br/>


## Test
To test the solution, type from the CLI:   
	
	> python tests.py  

</p>
