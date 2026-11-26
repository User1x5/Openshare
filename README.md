## Openshare
-# We need more open source software!

Openshare is an open source file sharing software that runs on sockets and python
Since it is currently in development, it is not recommended to use it for production purposes. You can contribute by making a fork and making a PR! (This is highly appreciated please do it)
If theres an issue, please report it in the issues section of the repository.

## Installation
Its easy, clone the repository and run the following command in the root of the repository:
`git clone https://github.com/User1x5/Openshare.git`

Run it with python3
`python3 openshare.py`

## Documentation
Openshare works by opening a socket with a receiver, You can select both sending or receiving
It specially needs an ip address to connect to, and a port to listen on, Default port is set on the `tcp_port` variable (In case of making a fork then if you do not want openshare to communicate with your port in the case both protocols dont work please change it in the range of 2764-5000, also works in case an app is using the same port)

# Variables

Runtime = set during execution
Hard = Set in the start of the code

`tcp_port` - The port that openshare will listen on, default is 2763 - Hard
`name` - Name of protocol, default is Openshare - Hard
`version` - Version of protocol, default is 1.0 - Hard

`filename` - Name of the file to send or receive - Runtime - Appears in function send and receive
`client` - The client socket that connects to the server - Runtime - Appears in function send
`server` - The server socket that listens for connections - Runtime - Appears in function receive
`ipaddr` - The ip address of the receiver - Runtime - Appears in function send and is set by an input
`recvbytes` - The raw bytes received - Runtime - Appears in function receive
`recvstring` - The raw bytes received decoded into a string - Runtime - Appears in function receive and send
`rheader` - The header of the received data - Runtime - Appears in function receive
`total` - The total size of the file to receive - Runtime - Appears in function receive
`received` - The received data - Runtime - Appears in function receive

`chunk` - The chunk of data received - Runtime - Appears in function receive
`file` - The file object to write the received data - Runtime - Appears in function receive
`archive` - The zipfile object to extract the received data - Runtime - Appears in function receive
`newname` - The new name of the extracted folder - Runtime - Appears in function receive

-# There are more variabkles but they are not important for the user to know about, they are used internally by the functions

# Functions
`send()` - The function that sends the file to the receiver
`receive()` - The function that receives the file from the sender

## What can you do with Openshare?
i made this program as a classic weekend project, so it is not very useful, but you can use it to send files to your friends or family, or even to yourself if you want to transfer files between your devices, Its not too supported by android devices because you need to have a python interpreter, But you can build it, You can learn TCP from this, so i made it public for that

You can inspect the code and learn from it, or do a fork And do whatever your mind desires, Itd be happy to see what things you can do 

Renember, build what you want, have freedom, and learn from it.


## Notes
It is not guaranteed that a transfer will be secure or so, The protocol is not encrypted so anyone can read from it, But who is sending private info to their friends?
And renember, never send ANYTHING personal if you dont want some geek with some weird tech to read things over the network.
Openshare would not be receiving updates regularly as i mostly develop in a phone since my main tool to program is broken, But itd be happy to merge PRs

please do not leak your ip tho since it only works in the local network so you cant send things over 5 million kilometers away, but if you want to do that, you can use a vpn or something like that, but i dont recommend it since it is not secure and you can get hacked easily
