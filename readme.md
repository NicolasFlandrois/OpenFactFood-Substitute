# Products manager and substitutes.

## (Python, MySQL, API - OC Project 5 - OpenFoodFacts)


**Date**:Thu 23 May 2019 17:07:10 CEST 

**Author**: Nicolas Flandrois

-------------------------------------------------------------

**Description**:
This program will display a product management system, running from terminal, without GUI.

Through a menu, the user will select a product from the MySQL database set.
The program will display the product's sheet, along with the name of its substitute, and whether it's been substituted already.
Then the user will be presented with a choice, whether to apply a substitution, or not.

From the main menu, the user can also choose to display all curently substituted products (Not in use at the time), along with corresponding substitution in use. The display is a list of items, readable in one page.

At any time, when the program offers a choice menu, the user can either return to the previous menu, or quit the program.

*NB*: All changes in substitution, will be registered in the MySQL database. This persistence allow the user to manage updated system over time.

***How to run this script***:
After updating (or installing) MySQL, and all required dependencies,
Launch the program in python, with the file control.py

	python3.7 control.py

-------------------------------------------------------------

***Setup recommendations***:
- MySQL (or MariaDB)
- Python 3.x

	cf: requirements.txt for python dependencies required installs

	run in terminal:
	
		pip3 install -r [path-to-file]/requirements.txt

**Setup**:

1. Change your database (MySQL/MariaDB) credential in the config.json file. Update info with your personnal :
	1. Username
	2. Password
	3. Host name (MySQL/MariaDB by default should remain 'localhost')
	4. Port (MySQL/MariaDB by default should remain '3306')
2. Run the 'setup.py' file, to create, and populate your database with relevent data set.