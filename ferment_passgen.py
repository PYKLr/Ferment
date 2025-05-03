#!/usr/bin/env python3

"""
Module that generates the password.

Procedure:
    - Defines password generator class.
    - Secure, random passwords.
    - Combines ASCII letters, numbers, and punctuation.
"""

__author__ = 'PYKLr'
__date__ = '5/2/2025'

from tkinter import messagebox
import secrets
import string

MINIMUM_LENGTH = 16


class Passgen():
    """
    A class that generates a random password to given length.

    Password consists of:
        - Uppercase ASCII Letters
        - Lowercase ASCII Letters
        - Punctuation
        - Numbers

    Attributes:
        length (int): Length of the password
    """

    def __init__(self, length=16):
        """
        Initialize the Passgen class.

        Args:
            length (int, optional): Length of the password. Defaults to 16.
        """
        self.length = length

    @property
    def length(self):
        """
        Return current length of password.

        Returns:
            int: Length of password
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Set length of generated password.

        Error Handeling:
            - Raises error when below minimum length

        Args:
            length (int): Length of password
        """
        if length >= MINIMUM_LENGTH:
            self._length = length
        else:
            messagebox.showwarning('Warning!', 'Password is too short! ')

    def gen_key(self):
        """
        Generate a random password with string and secrets library.

        Returns:
            str: A randomly generated password of X length
        """
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(secrets.choice(chars) for _ in range(self.length))
