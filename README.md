# Ferment Password Generator

Ferment is a simple password generator built with Python and Tkinter that allows you to generate secure, random passwords of specified lengths. It combines uppercase and lowercase letters, digits, and punctuation characters to create strong passwords. It also offers an intuitive GUI to easily generate and manage passwords.
## Features

- Generate Password: Generate a secure password of your desired length (minimum length of 16 characters).
- Show/Hide Password: Toggle between showing and hiding the generated password.
- Copy to Clipboard: Copy the generated password to the clipboard for easy pasting.
- GUI-Based: Easy-to-use graphical interface built with Tkinter.
- No password storage: The application does not store passwords anywhere—ideal for use with a password manager.

## Requirements

- Python 3.x
- Tkinter (comes with Python standard library)

## Installation
1. Clone the repository

You can clone this repository to your local machine using Git:

git clone https://github.com/your-username/ferment-password-generator.git

2. Install required packages

Ferment uses the secrets and string libraries, which are part of Python's standard library, so no additional dependencies need to be installed. However, make sure you have Python 3.x installed on your system.
Usage
1. Run the Program

Once you have cloned the repository, navigate to the directory where the project is located. Then, simply run the Python script to start the GUI:

python ferment_gui.py

This will open a window where you can:

    Generate a Password: Enter the desired length and click the "Generate" button.

    Show/Hide Password: Toggle visibility of the password by clicking the "Show" or "Hide" button.

    Copy Password: Copy the generated password to your clipboard using the "Copy" button.

    Exit the Program: Close the application by clicking the "Exit" button.

2. Customize Password Length

By default, the password length is set to 16 characters. You can specify a different length by entering a number in the "Length" field before clicking "Generate." If you enter a value less than 16, a warning will appear, and the password will default to 16 characters.
Code Overview
Password Generator Class (ferment_passgen.py)

The Passgen class is responsible for generating secure passwords. It:

    Uses Python's secrets module for cryptographically secure random numbers.

    Combines ASCII letters (uppercase and lowercase), digits, and punctuation to generate strong passwords.

GUI Class (ferment_gui.py)

The Ferment class creates the GUI for the application. It allows users to:

    Input a desired password length.

    Generate a password.

    Copy it to the clipboard.

    Show or hide the password.

Example

When you run the program, you will see a simple GUI where you can input the desired password length, generate the password, copy it to the clipboard, or toggle the visibility of the password.

Here’s an example of the output:

Password: X$s9oP&bZa2dC7m!
Length: 16

You can then click the "Copy" button to copy the password to your clipboard and use it for your accounts.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Contributing

Feel free to fork this repository and submit issues or pull requests if you have suggestions or improvements. If you would like to contribute, please follow the steps below:

    Fork the repository.

    Clone your fork to your local machine.

    Create a new branch for your feature or bug fix.

    Make your changes, and test them thoroughly.

    Commit your changes and push to your fork.

    Open a pull request describing your changes.

Contact

If you have any questions or suggestions, feel free to contact me:

    Author: PYKLr

    Email: pyklr@proton.me

    Signal: @PYKLr.43

    GitHub: https://github.com/PYKLr
