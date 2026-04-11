### Assessment Overview
4 x multiple choice tests (2.5% each) - 10%
Programming Challenge: Submit own code to the given specification - 50%
Group project: assessing a given code base and reporting back via a group presentation - 40%

# Module 1
### The history of coding & progranning
abacus - first automation
![[Pasted image 20260212115508.png|300]]

binary

Age of enlightenment
1642 - Blaise Pascal
		the first mechanical machine able to do calculations - mechanical abacus
1671 - Gorrdeiws Leibniz
1837 - Charles Babbage
		assemble a mother computer called the **analytical engine** - the first?
		running more advanced mathematics
		conditionals and loops
		using punch cards in this prototype
1843 - Ada Lovelace
		first programmer of the world
1930 - Alan Turing
		second world world - encryption
		the turing machine (turing complete)
		enigma
		the turing test - determine whether a machine can exhibit human intelligence
1945 - John von Neumann
		design of the first ever electronic computers
1944 - Harvard MK1
		First programmable machine
		fast computations
1945 - ENIAC
		first programmable computer
1947 - Manchester Baby
		Tom Kilburn
		first reprogrammable computer
		significantly smaller
		Ferranti Mach one - alan turing wrote a chess game algorithm
		Kilburns have these replicas
1959 - Grace Hopper
		The first programming language - COBOL
			still used in 43% of banking and financial companies
		inventor of the compiler:
			what takes the written code, such as python, and transform into something that machines can understand
1963 - Graphical User Interface - GUI
		Ivan Sutherland
		developed the first ever GUI - Sketchpad
		first person conceptualized VR headset
1980 - Steve Furber
		ARM Processor
		BBC Micro - making programming more accessible
		SpiNNaker
1981 - IBM personal computer MS-DOS
1985 - Microsoft windows 1.0
1989 - Tim Berners-Lee
		The World Wide Web (WWW)
1999 - NVIDIA 256 - released their first graphical processing unit (2^8)


### What do Programmers Do?
Software engineering
**frontend team**
	interactive components
	everything in the page make sense
	interact with users
	HTML - structure
	layout of the websites
	CSS - cascading style sheets - aesthetics
	Javascript - dynamics
	
**backend team**
		
	java
	php
	python
	javascript
support the frontend teams with the functionality they need to populate the frontend of the project
![[Pasted image 20260212124152.png]]
**user experience departments**
operations
devops team
quality analysts
project managers
tech leads

Artificial Intelligence
	machine learning engineer
		cognitive robotics, computer visions, data science

natural language processing
	making machines seemingly talk like humans
	autocomplete sentences
	certain semantic properties in quantities
	sentiment

**Computer vision**
	models inspired by human perception

**Computer graphics**
	graphical artists jobs

### Problem Solving
What is a program?
	a set of instructions which performs a specific task

What is programming
	the process of designing and building a program

The wason selection task (1966)
 E3![[Pasted image 20260212130550.png]]

**Key steps of programming**
 define the output & data flows -> develop the logic to get that output -> write the program

**State & Type**

**5 Fundamendals**
- input
- output
- arithmetic
- conditional
- repetition

**States**
binary state: 0 / 1 or Off / On
dice

Variables - storing data
- ubt
- char
- string

# Module 2
### How do we program?
Triads of fundamentals
- **Sequences**
	morning routine?
	number/ values have to be store somewhere inside a sequence - variables
	equal sign = in programming -> called assignment
- **Selections**
	if x == 2: -> comparison operator
- **Loops**
	if the loop is neverending - computer crash
	need to have end condition
	![[Pasted image 20260227090139.png]]

psudocode

### Text Editors vs IDEs
The terminal
再看一眼


indentation- tab - very useful in the loops/conditions


![[Pasted image 20260313113639.png]]![[Pasted image 20260313113701.png]]

### Text Editors vs IDEs

ctrl + D - change same variable names

Integrated Development Environments IDEs
debugging - grace hopper

VS Code is not Visual Studio!!

#### Selection & Iteration 

allow customization and decision making
![[Pasted image 20260407160658.png|394]]

selection:
syntax
indentations
![[Pasted image 20260407160754.png|381]]

else if - can have many of them
![[Pasted image 20260407160903.png]]

statement execute one after the other, until you say otherwise

Block and statement boundaries are detected automatically

Compound statements = header + ":" + indented statements

Blank lines, spaces, and comments, are usually ignored


nesting - put one block into another - if under another if statement
Block delimiter: Indentation rules
![[Pasted image 20260407161416.png]]

![[Pasted image 20260407161657.png]]

#### Iteration or Looping

Infinite Loops
- repeat forever

Count-Controlled Loops
- repeat # Times

Conditioned-Controlled Loops
- repeat until condition met

while - when true then carry on
for - fixed number of times

![[Pasted image 20260407162106.png]]
continue - if something happened, you can go back to the beginiing of loop and start again

pass - want some loop to run but not do anything

else - not so common to add in loop
- run only when loop runs successfully

![[Pasted image 20260407162542.png]]


### Flowcharts

represents an:
- algorithm
- workflow
- process

Used for:
- Analysing
- Designing
- Documenting

![[Pasted image 20260407203241.png]]
![[Pasted image 20260407203322.png]]
![[Pasted image 20260407203436.png]]
![[Pasted image 20260407203543.png]]

## Module 3：

#### GUI & UX
spotify.design
ww.art.yale.edu

prof. simon harper - university of manchester

User Experience
Human-Computer Interaction

making system more appealing and humane

User Tailorability

causality in technological ecosystem

defining UX?


Mother of All Demos
the mouse
- word processing & document editing

Xerox PARC 

Xerox Star Interface
![[Pasted image 20260407205631.png]]

Skeuomorphism
understand the causal interface from day to day lives
![[Pasted image 20260407205815.png]]

WYSIWYG - what you see is what you get
Flip Wilson

the magical number 7 (+-2)
reduce cognitive load - attention is selective

Progressive Disclosure

engaging - gamification
- badges
- achievements

flow theory
![[Pasted image 20260407210651.png]]

User Centred Design (UCD)

Digital Phenotyping
tracking users activity
data of what user is tapping, etc on the device

very effective tool to study user behaviour


### Programming Paradigms & Styles
style of programming

![[Pasted image 20260409114453.png]]
higher level (compile language)
mid-level languages (C, C++)
assemply languages - mnemonics
electrical signals

compile

compile a java file
filename.class
![[Pasted image 20260409102614.png]]

Interpreted

python




![[Pasted image 20260407211454.png]]

Imperative - you tell machine what to do and exactly how to achieve it
- procedural 
	go through codes line by line, not much code usability
	most languages support 
	even EmojiLang
	![[Pasted image 20260407211609.png|407]]
declarative - tell the machine what you want, compiler figure out a way to provide you


what we are doing up until now - procedural coding


Object-Oriented Programming(OOP)
![[Pasted image 20260407211755.png]]

children will inherent all the attribute from the old class
but also have independent attribute

- inheritance

![[Pasted image 20260409103132.png]]



access modifiers in front of them (public & private)
![[Pasted image 20260407211858.png]]
construct an object

extends vehicle - inherent all attributes from truck class

![[Pasted image 20260407211949.png]]

![[Pasted image 20260409103550.png]]

Python is a object oriented language

Scripting languages
languages support quite fast interactions that are broken down into smaller chunks of code and tell what the software what to do

jupyter notebook - python is also scripting language - allow fast executing script that do not need to be compiled
r


declarative

imperative vs declarative
![[Pasted image 20260409104207.png|413]]

#### functional programming

everything is a function
functional programming has its basis in computational mathematics

functional programming requires a intimate knowledge of the programming language and mathematical concepts

python supports functional program as well

very versatile!

#### logical programming
software verifications
computational proofs
![[Pasted image 20260409104459.png|413]]

#### Relational Languages

Structured Query Language (SQL)
![[Pasted image 20260409104527.png]]extract information based on certain properties


## File Handling

Triad
selection
if
conditional
looping

how to read from external files
![[Pasted image 20260409104755.png]]
dictionaries - unordered lists

access through key
![[Pasted image 20260409104925.png]]
![[Pasted image 20260409104936.png]]
![[Pasted image 20260409105156.png]]

create - create eg: python file
read - access in read only mode
delete - delete the while file

open()
- filename
- mode
![[Pasted image 20260409105456.png]]
![[Pasted image 20260409105526.png]]
default, dont need to specify

basic syntax

to open a file it is enough to just specify the name of the file:
file = open("demoFile.txt")

both of the code samples are equivalent because "r" and "t" are default values.

file = open("demoFile.txt", "rt")

Reading a File

file = open("demoFile.txt", "r")
print(file.read())
file.close()

##### Writing to a File
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
- adds the text at the bottom of the file

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
- it overwrites the while file

##### Deleting a File
to remove a file you need to use the OS module

import os
os.remove("demofile.txt")
- once its gone you cannot retrieve it back


## Pseudocode
simpler version of a programming language written in plain english
this happens before we implement it in a specific language

A Guide to pseudocode
- capitalise key commands (IF, ELSE, WHILE)
- one statement per line
- use indentations
- be specific
- keep it simple


![[Pasted image 20260409111518.png]]
![[Pasted image 20260409112432.png]]
N = (value)
sum = 0
counter = 1

while counter <= N:
	sum += counter
	counter += 1

是不是就是

for counter in range (1, N+1):
	sum += counter