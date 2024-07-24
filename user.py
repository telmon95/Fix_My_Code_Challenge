#!/usr/bin/python3
"""
User class
"""

class User:
    """Class representing a User with an email address."""

    def __init__(self):
        """Initialize the User with a private email attribute."""
        self.__email = None

    @property
    def email(self):
        """Getter for the email property."""
        return self.__email

    @email.setter
    def email(self, value):
        """Setter for the email property.

        Args:
            value (str): The email address to set.

        Raises:
            TypeError: If value is not a string.
        """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
