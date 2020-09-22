<!DOCTYPE html>
<html>
        <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
				<link href="https://gitcdn.github.io/bootstrap-toggle/2.2.2/css/bootstrap-toggle.min.css" rel="stylesheet">
			<script src="https://gitcdn.github.io/bootstrap-toggle/2.2.2/js/bootstrap-toggle.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.0.3/socket.io.js"></script>

                <script>





			$(document).ready(function(){
				var socket = io('http://10.0.0.07:8080/');

				var $growoff = $('#growoff');
				var $growon = $('#growon');

				$growon.hide();
				$growoff.hide();

				socket.on('lightChange', function (data) { //get button status from 
					let off = data === 1;
					if (off) {
						$growon.hide();
						$growoff.show();
					} else {
						$growoff.hide();
						$growon.show();
					}
				});


				$("#growLight").click(function(event){
					let checked = event.target.checked;
					socket.emit("updateLight", checked ? 0 : 1);
				});

				$growoff.click(function(){
					socket.emit("updateLight", 0);
					$growoff.hide();
					$growon.show();
				});

				$growon.click(function(){

					socket.emit("updateLight", 1);
					$growon.hide();
					$growoff.show();
				});

				$("#studioon").click(function(){
					$.get("studioon.php");
				});
				$("#studiooff").click(function(){
					$.get("studiooff.php");
				});
				$("#capture").click(function(){
					$.get("capture.php");
				});
				$("#starttl").click(function(){
					$.get("starttl.php");
				});
				$("#stoptl").click(function(){
					$.get("stoptl.php");
				});

				// function doStuff(){
				// 	$.get("test5.php", function(data, status){
				// 			console.log("Data: " + data + "\nStatus: " + status);
				// 	});
				// }

				//setInterval(doStuff, 1000); // does the funtion every second 
 
						});
						


			</script>

        </head>
<body>

<div class="container ">
			<div class="jumbotron bg-success text-white">
			<h1 class="text-center"> Plant Box<h1>
			</div>

				<div class="row">
				 
				</div>

				<br>
				
				<div class="col-sm-12">
					<button type="button" class="btn btn-dark btn-block " id="growoff">Grow Light OFF</button></div>
				<div class="col-sm-12">
					<button type="button" class="btn btn-success btn-block" id="growon">Grow Light ON</button></div>
				</div>

				


				<div class="row">
				<div class="col-sm-6">
				<h3 class="text-center">Studio Light</h3>
                        	</div>
				<div class="col-sm-3">
                                <button type="button" class="btn btn-block" id="studioon">ON</button></div>

                                <div class="col-sm-3">
                                <button type="button" class="btn btn-dark btn-block" id="studiooff">OFF</button></div>
                        	</div>

				<div class="row">
				<div class="col-sm-6">
				<h3 class="text-center">Capture Image</h3>
                        	</div>
				<div class="col-sm-6">
                                <button type="button" class="btn btn-primary btn-block" id="capture">Capture</button></div>


                        	</div>
				<div class="row">
				<div class="col-sm-6">
				<h3 class="text-center">Timelapse Program</h3>
                        	</div>
				<div class="col-sm-3">
                                <button type="button" class="btn btn-success btn-block" id="starttl">Start</button></div>

                                <div class="col-sm-3">
                                <button type="button" class="btn btn-danger btn-block" id="stoptl">Stop</button></div>
                        	</div>
						</div>
	</div>



</body>
</html>

