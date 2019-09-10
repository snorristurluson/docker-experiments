This project is intended to demonstrate how to have two Docker containers
communicate to each other.

*Echo* is a simple echo server - it opens a listening socket and echoes back anything
sent to it. *Forward* is a variation on the echo server - rather than echoing its messages
right back, it connects to the echo server and forwards messages to it, then echoes back
the response from the echo server.

As far as networking goes, this is similar to a web server that talks to a database.
The web server handles connections coming in from the outside, and talks to the database
to get the necessary data. The database is not directly accessible from the outside world,
only the web server can talk to it.

