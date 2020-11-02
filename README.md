Create a REST endpoint that return the sum of a list of numbers e.g. [1,2,3] => 1+2+3 = 6

The list of numbers is expected to arrive from a backend service and for this test you can
hard code the list using the following line.

numbers_to_add = list(range(10000001))

The url of the endpoint and the sample response is as follows:
Request: http://localhost:5000/total
Response:
{
" total " : 6
}
Please provide the source code, tests, documentations and any assumptions you have
made.

--------------------------------------------
The code has a requirements.txt based on which you can install packages required, in this case just flask. I added a tests folder, just use pytest in the CLI to check them.

To run the application run in your terminal export FLASK_APP=app.py, go into the source code folder and type flask run.

I have set the DEBUG and TESTING options for flask to True such that the app reloads on code updates. In a production environment, the development config class from config.py would set these to false rather than have a "pass" as a command.

The get_total should still return the sum of a list, but I override its result in the view.

The view accepts only GET method.
