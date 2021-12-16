## Switch on the Gravity

Published by  [Joshua Señoron](https://edabit.com/user/PXAcsKkssS2yLyDv2) 

Given a 2D array of some suspended blocks (represented as hastags), return another 2D array which shows the _end result_ once gravity is switched on.

### Examples
``` ruby
switch_gravity_on([
  ["-", "#", "#", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"]
]) ➞ [
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "-", "-", "-"],
  ["-", "#", "#", "-"]
]

switch_gravity_on([
  ["-", "#", "#", "-"],
  ["-", "-", "#", "-"],
  ["-", "-", "-", "-"],
]) ➞ [
  ["-", "-", "-", "-"],
  ["-", "-", "#", "-"],
  ["-", "#", "#", "-"]
]

switch_gravity_on([
  ["-", "#", "#", "#", "#", "-"],
  ["#", "-", "-", "#", "#", "-"],
  ["-", "#", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-"]
]) ➞ [
  ["-", "-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-"],
  ["-", "#", "-", "#", "#", "-"],
  ["#", "#", "#", "#", "#", "-"]
]
```