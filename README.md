# STIBC
 the Simple TI-BASIC Compiler is a command line utility that compiles and decompiles TI-BASIC programs.
 
 STIBC was created by James Dumas and is licensed under the GNU General Public License v3.0

##Installation
Run `python setup.py install` from the directory containing this file

##Usage
`stibc {compile | decompile} inputfile outputfile`

##Format
to successfully compile a program the input file must be formatted in a certain way. 
The first four lines of your script must contain the following:

```
#name: {program name}
#info: {comment}
#archived: {true | false}
{an empy line}
```
{program name} is what the program will be named when viewed on the calculator

{comment} is a comment containing 42 characters (check format.md for more about this)

archived {true | false} is whether or not the program is archived, obviously

Also, STIBC is not as picky about code formatting as the actualy TI-Connect editor.  Leading and trailing whitespace is ignored, and all tokens can be typed with a standard english keyboard. for example, instead of having to copy-paste a greek pi every time you want to use it, you just type `pi;`. Open stibc-tokens.json in the src folder to look at and change how all of the tokens are written.

##More Info
Check format.md for info on the 8xp program file format.  Most of the info needed for this project came from http://merthsoft.com/ and http://tibasicdev.wikidot.com/ so check those out too, they're pretty cool sites.
