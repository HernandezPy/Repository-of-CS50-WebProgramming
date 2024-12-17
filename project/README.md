# Project Title: "GOING TO THE DENTIST"
#### Video Demo: <https://youtu.be/uWReoSUOjTw>
#### Description:
My project is based on a data table which has options of services that a dentist offers to his patients.
Then each service has its own cost, and according to the client's selection it will receive a 50% discount.
If the client decides to pay immediately the discount will be applied and if decides not to pay, the full service will be applied.
My code consist of the main function where I created a dictionary with a variable called data, where the "options", "services" and "the cost"
are placed, then with the tabulate library it defines the table_of_information function to give a more attractive appearance to the output.
Then it defines the job_cost function which asks the client to select one of the services and according to the input it
will receive the information of its selection, and finally  defines the discount_in_advance function which has the function
of printing a message telling the client that if it pays in advance it will receive a 50% discount. It also receives an input
if wishes to pay [yes/no] if the client decides to pay in advance the discount will be applied and if not it will pay
the full amount.
Well my code is based on a book, which is Python for beginners and shows code and examples, but it seems to be a little outdated,
so it shows some exercises and projects, but they are different from everything I have been learning with CS50 which is more updated
using functions and libraries that help a lot to make the code easier to run. In short, I took a project from this book or rather
the idea, and then I modified it with everything I have been learning in CS50 and I can create a few functions which in the previous
code I did not use any function, only conditions, declarations, a very long code in the book with a lot of lack of complexity,
but it still works but when you see all the projects in this course nothing resembles the book, but to learn the basics it is fine.
Then you can improve with this course and update the code in your own way to make it work in an easier way and also,
so that it is not difficult to read it.
When testing with pytest I had a lot of problems because I didn't know how to test each function since two of the functions ask
for an input and pytest couldn't do the tests because the answers depended on the user and couldn't be verified just like that,
so with a little help on the internet and research I found a way to assimilate the output and do the tests with pytest.
For that I had to use monkeypatch.setattr which I had never seen in previous courses but, you always learn something new along the way,
I also used capsys in python which captures the output of print and using these two articles provided by the pytest libraries
I was finally able to get the tests to pass.
