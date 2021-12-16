## Password Check 🔐 Binary to String

<p align="justify">  
A wealthy client has forgotten the password to his business website, but he has a list of possible passwords. <br/>
His previous developer has left a file on the server with the name password.txt. You open the file and realize it's in binary format. <br/><br/>

Write a script that takes a list of possible passwords and a string of binary representing the possible password. <br/>
Convert the binary to a string and compare to the password array. <br/>
If the password is found, return the password string, else return false.

	
### Example:
```ruby
decode_pass(['password123', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011');    => 'password123'
decode_pass(['password321', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011');    => False
decode_pass(['password456', 'pass1', 'test12'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011');    => False
```
<br/><br/>


## Test
To test the solution, type from the CLI:   
	
	> python tests.py  

</p>
