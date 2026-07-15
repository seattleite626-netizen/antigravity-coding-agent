"""
Agent: A class representing the antigravity agent.
"""

import logging
from typing import Dict

class Agent:
    """
    Agent: A class representing the antigravity agent.

    Attributes:
        config (Dict): The agent's configuration
        model (object): The AI model used by the agent
    """

    def __init__(self, config: Dict):
        """
        Initialize the agent.

        Args:
            config (Dict): The agent's configuration
        """
        self.config = config
        self.model = None

    def set_model(self, model: object):
        """
        Set the AI model used by the agent.

        Args:
            model (object): The AI model to use
        """
        self.model = model

    def generate_code(self):
        """
        Generate code using the AI model.
        """
        if self.model:
            # Use the AI model to generate code
            code = self.model.generate_code()
            print(code)
        else:
            logging.error('No AI model selected')

    def review_code(self):
        """
        Review code using the AI model.
        """
        if self.model:
            # Use the AI model to review code
            review = self.model.review_code()
            print(review)
        else:
            logging.error('No AI model selected')

    def modify_code(self):
        """
        Modify code using the AI model.
        """
        if self.model:
            # Use the AI model to modify code
            modified_code = self.model.modify_code()
            print(modified_code)
        else:
            logging.error('No AI model selected')