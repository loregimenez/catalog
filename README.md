---------------
 Music Catalog
---------------

This project is about a catalog of music clasified by genre, stored in a database using SQLAlchemy.

It is needed a basic knowledge of Vagrant, Python, Flask and SQLAlchemy to run this project.

To be installed:
- Python v 2.7. Download: https://www.python.org/downloads/
- Vagrant. Download: https://www.vagrantup.com/downloads.html
- VirtualBox. Download: https://www.virtualbox.org/

To run the App:

1. Unzip de file in vagrant file
2. Open the terminal
3. Go to Vagrant directory: cd vagrant
4. Run the vagrant up command
5. Run the vagrant ssh command
6. Go to the project directory (cd catalog-master)
7. To set up the database: python database_setup.py
8. To populate de database: python music.py
9. To test the program: python application.py
10. Open a web browser to see the app on http://localhost:8080
