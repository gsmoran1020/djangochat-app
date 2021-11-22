# djangochat-app
 
## Overview
This project is a chat application built with HTML, Bootstrap, JavaScript, Python, Django, and Django Channels. It utilizes communication between javascript web sockets and asnychronous django channels in order to provide users with a real-time chat application where they can talk to each other. There are two pre-built chat rooms and an option for users to create their own chat rooms. You can create an account and give it a try here: https://djangochatnow.herokuapp.com/

## Features
The DjangoChat application features two primary chat rooms and the ability for users to create their own rooms. These chat rooms are unique and are destroyed, along with any messages in them, whenever all users in the chat room exit the room. 

This Project also features user authentication and password reset via email links.

## How It Works
Real-time chat between multiple users is achieved through a JavaScript WebSocket on the front end and a Django Channels consumer on the backend. 

First the WebSocket is created in the front end, communicating with the built in daphne server that Django Channels uses. Once the html element for sending messages is pressed, the web socket sends a message to the server which is picked up by the consumers channel layer. After receiving this message the consumer sends the message out to all other channel layers in the same group, in this case this would be other users that are in the same chat room. The message is then sent once more back to the javascript web socket where it checks the information provided in the message and updates the chat room front end accordingly.
