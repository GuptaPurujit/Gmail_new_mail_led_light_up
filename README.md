# Gmail_new_mail_led_light_up
This program automatically logs onto gmail by the user just providing their Email Id and Password and then checks for a new e-mail after every 30 secs.
If there is a new mail then it is accompanied by a blink of an led on the arduino uno otherwise a false is registered on the terminal.

## Getting Started
All the libraries and stuff that has to be installed through `pip install` are listed in the `requirements_gmail.txt` file.

You can directly add them to the directory using the command `pip install -r requirements_gmail.txt`.  

In the main file is `app.py`, there are two field where one has to enter their own data, they are username and password fields.

## Prerequesites
To understand this project, there is need of understanding of the framework **Selenium**, for that refer to the official docs [here](https://selenium-python.readthedocs.io/).

Also for the arduino and python interfacing another library namely **pyfirmata** has been used, whose documentation can be referred to [here](https://hub.packtpub.com/prototyping-arduino-projects-using-python/).

Also time library has been introduced to get a time delay and the use of `sleep()` has been made.

## Contributions
Feel free to give any suggestions or report any issues.
