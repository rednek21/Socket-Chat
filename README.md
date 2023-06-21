# Socket-Chat
Simple socket-chat using python

This app is a university lab work on the discipline of "Internet technology" to study sockets using client-server architecture wtih multithreading.

The application works as follows: when starting the client, you are asked to enter the ip-address and port of the server you want to connect(default data are stored in "config.json". Server uses same data to run).
Next you are asked to enter the nickname you want to use in the chat.
if all past without errors then you will be connected to the server with your nickname and will see the last 10 messages that were sent by users.
To disconnect type "bye".

Otherwise, for correct work of the app you must use the same network with your friends.

To run the app:
1. python3 server.py
2. python3 client.py

Enjoy chating with your friends)

P.S. To communicate full-remotely have to upload the application to the real server.
