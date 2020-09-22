
var http = require('http').createServer(handler); //require http server, and create server with function handler()
var fs = require('fs'); //require filesystem module
var io = require('socket.io')(http) //require socket.io module and pass the http object (server)
var Gpio = require('onoff').Gpio; //include onoff to interact with the GPIO
var GROW = new Gpio(20, 'out', 'falling'); //use GPIO pin 20 as output


http.listen(8080); //listen to port 8080

function handler (req, res) { //create server
  fs.readFile(__dirname + '/public/index.html', function(err, data) { //read file index.html in public folder
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'}); //display 404 on error
      return res.end("404 Not Found");
    }
    res.writeHead(200, {'Content-Type': 'text/html'}); //write HTML
    res.write(data); //write data from index.html
    return res.end();
  });
}

let growValue = 0;

let sockets = [];

io.sockets.on('connection', function (socket) {// WebSocket Connection
  sockets.push(socket);
  GROW.read().then(response => {
    console.log(response);
    socket.emit('lightChange', response);
  });



  
  socket.on('updateLight', function(data) { //get light switch status from client
    growValue = data;
    if (growValue != GROW.readSync()) { //only change LED if status has changed
      GROW.writeSync(growValue); //turn LED on or off
    }
      sockets.forEach(clientSocket => {
        try {
          clientSocket.emit('lightChange', growValue);
        } catch (error) {
          console.log(error);
        }
      });

  });
});



process.on('SIGINT', function () { //on ctrl+c
  GROW.writeSync(0); // Turn LED off
  GROW.unexport(); // Unexport LED GPIO to free resources
  process.exit(); //exit completely
});
