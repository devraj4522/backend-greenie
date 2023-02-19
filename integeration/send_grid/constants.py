EMAIL_STYLE ="""
	<style>
		body {{
			background-color: #f2f2f2;
			font-family: Arial, sans-serif;
			font-size: 16px;
			line-height: 1.5;
			margin: 0;
			padding: 0;
			text-align: center;
			color: #333;
		}}
		.container {
			background-color: #fff;
			border-radius: 5px;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
			margin: 20px auto;
			max-width: 600px;
			padding: 20px;
		}
		h1 {
			color: #4caf50;
			font-size: 36px;
			font-weight: bold;
			margin: 0 0 20px;
			text-transform: uppercase;
		}
		p {
			font-size: 18px;
			line-height: 1.5;
			margin: 0 0 20px;
			text-align: left;
		}
		a {
			background-color: #4caf50;
			border-radius: 5px;
			color: #fff;
			display: inline-block;
			font-size: 18px;
			font-weight: bold;
			margin: 20px 0 0;
			padding: 10px 20px;
			text-decoration: none;
			text-transform: uppercase;
		}
		a:hover {
			background-color: #3e8e41;
		}
	</style>
"""

def get_tempate(name, amount, ):
    return  f"""
		<!DOCTYPE html>
		<html>
		<head>
			<title>Your Order Has Been Placed!</title>
			{EMAIL_STYLE}
		</head>
		<body>
			<div class="container">
				<h1>Your Order of Rs. {amount} Has Been Placed!</h1>
				<p>Hi {name},</p>
				<p>We are happy to let you know that your order with Greeny has been successfully placed. </p>
				<p>Thank you for shopping with us! </p>
				
			</div>
		</body>
		</html>
    	"""