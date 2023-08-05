# DynamicBio
Set yourself a dynamic status in Scratch!

### RUS:
Run the program, close the program and open the config.ini file created in the program folder.
Configure the program through config.ini.

#### Config designations:
**BIOs** - enter text here for dynamic status. Example:
```
[BIOS]
bio1 = Hello! This field is constantly changing!
bio2 = Status: Online!
bio3 = *working on a project*
```
**User** - enter the username and password for your Scratch account here. Example:
```
[user]
name = CaT_cRuSh
password = pwdpwd123
```
**Options** - specify additional options here.

cooldown - time in seconds after which the text will change.
mode - operating mode. Has 2 meanings: bio and wiwo. bio - change the "About me" field. wiwo - change the field "what I'm working on"

Example:
```
[options]
cooldown = 10
mode = bio
```
