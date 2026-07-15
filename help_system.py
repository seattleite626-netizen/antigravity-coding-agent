"""
HelpSystem: A module containing a help system for the antigravity agent.
"""

import logging

class HelpSystem:
    """
    HelpSystem: A class providing a help system for the antigravity agent.
    """

    def __init__(self):
        """
        Initialize the help system.
        """
        logging.info('Initializing help system')

    def display_help(self):
        """
        Display help information.
        """
        # Display help information
        logging.info('Displaying help information')
        print('Available commands:')
        print('  help        Display this help message')
        print('  create      Create a new project')
        print('  edit        Edit an existing project')
        print('  read        Read an existing project')
        print('  generate    Generate code using an AI model')
        print('  review      Review code using an AI model')
        print('  modify      Modify code using an AI model')
        print('  exit        Exit the antigravity agent')