"""
Config: A module containing configuration management for the antigravity agent.
"""

import logging
import yaml
from typing import Dict

class ConfigManager:
    """
    ConfigManager: A class managing configuration for the antigravity agent.
    """

    def __init__(self, config_file: str):
        """
        Initialize the configuration manager.

        Args:
            config_file (str): The configuration file
        """
        self.config_file = config_file

    def load_config(self) -> Dict:
        """
        Load configuration from a file.

        Returns:
            Dict: The loaded configuration
        """
        # Load configuration from a YAML file
        with open(self.config_file, 'r') as f:
            config = yaml.safe_load(f)
        logging.info('Loaded configuration')
        return config