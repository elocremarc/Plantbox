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

                <script>
	                        $(document).ready(function(){
                                $("#growon").click(function(){
                                         $.get("growon.php");
                                });
                                $("#growoff").click(function(){
                                        $.get("growoff.php");
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
				$("#starttl").click(function(){
					$.get("stoptl.php");
				});
                        });
			                </script>

        </head>
<body>

<div class="container ">
			<div class="jumbotron bg-success text-white">
			<h1 class="text-center"> Plant Box<h1>
			</div>
<!--
				<div class="row">
				<div class="col"> <img src="test1.jpg" class="img-fluid" alt="test photo" width"1920" height="1080" ></div> 
				</div>
-->
				<br>
				<div class="row">
				<div class="col-sm-6">
				<h3 class="text-center">Grow Light</h3>
				</div>

                                <div class="col-sm-3">
                                <button type="button" class="btn btn-block" id="growon">ON</button></div>

                                <div class="col-sm-3">
				<button type="button" class="btn btn-dark btn-block" id="growoff">OFF</button></div>
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
                                <button type="button" class="btn btn-primary btn-block" id"capture">Capture</button></div>


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




</body>
</html>

