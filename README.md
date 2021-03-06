Lights Out
==========

A Python implementation of the classic puzzle game 'Lights Out' using the Tkinter GUI package.

![Lights Out Screenshot](http://img585.imageshack.us/img585/9475/hqna.png)

'Lights Out' was originally released by Tiger Toys in 1995 as an electronic puzzle game. It features a 5-by-5 grid of buttons which can be in one of two states, lit or unlit. Pressing a button toggles the state of that button as well as the four buttons directly adjacent to it. The game begins with certain buttons lit and the player presses buttons with the goal of getting all the buttons into their unlit state, hence the name 'Lights Out'.

This game uses check-boxes as the buttons and includes 8 pre-arranged levels. From Level 9 onwards, the puzzles are generated by an algorithm and will be of varying difficulty. I created this project because I enjoyed 'Lights Out' as a child and wanted to see how easy it would be to create an implementation of it using the tools that I am familiar with. 

Dependencies
------------

* Python 2.7
* Tkinter

Usage
-----

If you have the required dependencies, to run the game all you have to do is download the file 'lights_out.py', and in your operating system's command line navigate to the dirctory where the file is located and do:

	python lights_out.py

The game should run on Windows, OSX and Linux.
