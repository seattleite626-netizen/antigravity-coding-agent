"""
Antigravity Agent: A terminal-based coding agent for the antigravity platform.

Usage:
    python antigravity_agent.py [options]

Options:
    -h, --help        Show this help message and exit
    -c, --config      Specify a configuration file
    -p, --project     Specify a project directory
    -m, --model       Specify an AI model (OpenAI, Groq, etc.)
"""

import os
import sys
import logging
import argparse
from typing import Dict

# Import internal modules
from agent import Agent
from models import OpenAIModel, GroqModel
from plugins import PluginManager
from config import ConfigManager
from project import ProjectManager
from help_system import HelpSystem

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main entry point for the antigravity agent.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Antigravity Agent')
    parser.add_argument('-c', '--config', help='Specify a configuration file')
    parser.add_argument('-p', '--project', help='Specify a project directory')
    parser.add_argument('-m', '--model', help='Specify an AI model (OpenAI, Groq, etc.)')
    args = parser.parse_args()

    # Load configuration
    config_manager = ConfigManager(args.config)
    config = config_manager.load_config()

    # Initialize agent
    agent = Agent(config)

    # Initialize AI models
    models: Dict[str, object] = {
        'OpenAI': OpenAIModel(),
        'Groq': GroqModel()
    }
    if args.model:
        agent.set_model(models[args.model])

    # Initialize plugin manager
    plugin_manager = PluginManager()
    plugin_manager.load_plugins()

    # Initialize project manager
    project_manager = ProjectManager(args.project)

    # Initialize help system
    help_system = HelpSystem()

    # Start conversational interface
    while True:
        user_input = input('> ')
        if user_input.startswith('help'):
            help_system.display_help()
        elif user_input.startswith('create'):
            project_manager.create_project()
        elif user_input.startswith('edit'):
            project_manager.edit_project()
        elif user_input.startswith('read'):
            project_manager.read_project()
        elif user_input.startswith('generate'):
            agent.generate_code()
        elif user_input.startswith('review'):
            agent.review_code()
        elif user_input.startswith('modify'):
            agent.modify_code()
        elif user_input.startswith('exit'):
            break
        else:
            print('Unknown command. Type "help" for available commands.')

if __name__ == '__main__':
    main()