```markdown
# Star Wars API Project

## Project Overview

The **0x06. Star Wars API** project is designed to help me interact with an external API to fetch and display information about Star Wars characters based on a provided movie ID. This project requires proficiency in various key web programming concepts, including API interaction and asynchronous programming in JavaScript.

## Key Concepts

### HTTP Requests in JavaScript
- Understanding how to make HTTP requests to external services using the `request` module or alternatives like `fetch` in Node.js.
- **Resources**:
  - [A Complete Guide to Making HTTP Requests in Node.js](#)
  - [HTTP Requests in JavaScript](#)

### Working with APIs
- Basics of RESTful APIs and how to interact with them.
- Parsing JSON data returned by APIs.
- **Resources**:
  - [Working with APIs in JavaScript](#)

### Asynchronous Programming
- Managing asynchronous operations with callbacks, promises, and `async/await` syntax.
- Handling API response data asynchronously.
- **Resources**:
  - [Asynchronous Programming in JavaScript](#)

### Command Line Arguments in Node.js
- Using the `process.argv` array to access command-line arguments passed to a Node.js script.
- **Resources**:
  - [How to Parse Command Line Arguments in Node.js](#)

### Array Manipulation and Iteration
- Iterating over arrays and manipulating data structures to format and display character names.
- **Resources**:
  - [JavaScript Array Methods](#)

## Project Requirements

- **Allowed editors**: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should be semistandard compliant. Rules of Standard + semicolons on top. Reference: [AirBnB style](#)
- All files must be executable
- The length of files will be tested using `wc`
- Use of `var` is not allowed

## Installation and Setup

### Install Node 10
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semistandard
```bash
$ sudo npm install semistandard --global
```

### Install request module and use it
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Tasks

### 0. Star Wars Characters
**Mandatory**

Write a script that prints all characters of a Star Wars movie:
- The first positional argument passed is the Movie ID - example: `3 = “Return of the Jedi”`
- Display one character name per line in the same order as the `characters` list in the `/films/` endpoint
- Use the Star Wars API
- Use the `request` module

Example Usage:
```bash
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$
```

## Repository
- **GitHub repository**: `alx-interview`
- **Directory**: `0x06-starwars_api`
- **File**: `0-starwars_characters.js`
```
sebsibe solomon
