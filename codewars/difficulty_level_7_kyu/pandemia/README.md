## Pandemia π‘οΈ
<p align="justify">
β οΈ The world is in quarantine! There is a new pandemia that struggles mankind. Each continent is isolated from each other but infected people have spread before the warning. β οΈ
<br/><br/>
 
πΊοΈ You would be given a map of the world in a type of string:

``` ruby
string s = "01000000X000X011X0X"
'0' : uninfected
'1' : infected
'X' : ocean
```
 
β« The virus can't spread in the other side of the ocean.

β« If one person is infected every person in this continent gets infected too.

β« Your task is to find the percentage of human population that got infected in the end.

βοΈ Return the percentage % of the total population that got infected.

ββ The first and the last continent are not connected!
<br/><br/>
 
π‘ Example:
``` ruby
 start: map1 = "01000000X000X011X0X"
 end:   map1 = "11111111X000X111X0X"
 total = 15
 infected = 11
 percentage = 100*11/15 = 73.33333333333333
```
β For maps without oceans "X" the whole world is connected.

β For maps without "0" and "1" return 0 as there is no population.

<br/><br/>
To test the solution, type from the CLI: 
<br/><br/>

    > python tests.py

</p>
