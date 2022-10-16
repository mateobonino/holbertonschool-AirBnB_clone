# AirBnB Clone

![App Screenshot](https://imgs.search.brave.com/jTCrNgZ5d61CuMVlnPLxirGgtFhn5nmZigZMPxAfFIo/rs:fit:1200:1036:1/g:ce/aHR0cHM6Ly9pbWd1/ci5jb20vT2lsRXNY/Vi5wbmc)


The objective of this project is to implement a simple copy of the AirBnB website.
This project will be divided, each focused on different aspects and technologies.
This is the first part of the project which consists of building the console.

# What is a console?
 This works as a [Shell](https://github.com/Lautaro1387/holbertonschool-simple_shell).
It is implemented in the same way but with a specific use, that in this case, we want to be able to manage the objects of our project.

### How to install the console
Clone this repo:
```bash
$ git clone https://github.com/Lautaro1387/holbertonschool-AirBnB_clone
```

Run the file "console.py"
```bash
$ ./console.py
```

#### Interactive Mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all create  destroy help  quit show update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
#### Non-Interactive Mode
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Example
I will now show and explain some of the commands implemented on the console.

create --> Creates a new instance of BaseModel (in this case), saves it (in the JSON file) and prints the id
```bash
$ ./console.py
(hbnb) create BaseModel
6e9b2b2b-7fe4-4303-8a57-08ea8ff9dccb
(hbnb)
```

show --> Prints the string representation of an instance based on the class name and id.
```bash
./console.py
(hbnb) show BaseModel 6e9b2b2b-7fe4-4303-8a57-08ea8ff9dccb
[BaseModel] (6e9b2b2b-7fe4-4303-8a57-08ea8ff9dccb)     {'id': '6e9b2b2b-7fe4-4303-8a57-08ea8ff9dccb', 'created_at': datetime.datetime(2022, 10, 15, 17, 17, 38, 33901), 'updated_at':
datetime.datetime(2022, 10, 15, 17, 17, 38, 33913)}
(hbnb)
```

destroy --> Deletes an instance based on the class name and id (save the change into the JSON file).
```bash
./console.py
(hbnb) destroy BaseModel 6e9b2b2b-7fe4-4303-8a57-08ea8ff9dccb
(hbnb) show BaseModel 6e9b2b2b-7fe4-4303-8a57-08ea8ff9dccb
** no instance found **
(hbnb)
```

## Flowchart
Here you have a flowchart to understand you the program works

![Flowchart](https://i.ibb.co/6t35H9S/Diagrama-en-blanco.png)

## Authors

- [Lautaro Illa](https://github.com/Lautaro1387)
- [Mateo Bonino](https://github.com/mateobonino)
