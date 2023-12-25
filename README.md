# Parallel BFS - Network Programming Project @ FMI 2023

## Table of Contents

1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Setup and Installation](#setup-and-installation)
4. [Client Server Communication](#client-server-communication)
5. [Architecture](#architecture)
6. [Running the Application](#running-the-application)
7. [Testing](#testing)

## Introduction

This project implements a simple client-server system that performs a parallel Breadth-First Search (BFS) operation on a graph. The graph information is sent by the client to the server which performs the BFS operation in a parallelized manner using Python's multiprocessing capabilities.

## System Requirements

- Python 3.6 or higher
- Networking permissions for the Python interpreter to open sockets

## Setup and Installation

1. Clone this repository or download the project zip.
2. Extract the files to your desired location.
3. Run the Python scripts as described in the "Running the Application" section.

## Client Server Communication

The client prompts the user to enter a graph and sends this to the server. The server performs a parallel BFS on the received graph and returns the order of visited nodes back to the client.

## Architecture

The application consists of two main Python scripts:

- `client.py`: Sends the graph data as a JSON object to the server using a socket.

- `server.py`: Receives the graph data, performs a parallel BFS using Python's multiprocessing module and returns the list of visited nodes back to the client.

## Running the Application

### Server

To run the server, ensure that `server.py` is in your current directory and run the following command in your terminal:

```
python3 server.py
```

### Client

To run the client, ensure that `client.py` is in your current directory and run the following command in your terminal:

```
python3 client.py
```

When prompted, enter the graph information in the following format:
```
{'1': ['2', '3'], '2': ['4', '5'], '3': [], '4': [], '5': [], 'start': '1'}
```

## Testing

Unit tests are included in the `tests.py` file. 

To run the tests, navigate to the directory containing `tests.py` in your terminal/command prompt and use the command:

```bash
python3 -m unittest tests.py
```

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details. 

----
This project was created as part of the "Network Programming" course at the Faculty of Mathematics and Informatics (FMI), Sofia University, 2023.

----

## Contact

For queries or assistance, please feel free to reach out.