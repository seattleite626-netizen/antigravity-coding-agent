#!/usr/bin/env python3
# Package installation setup for antigravity coding agent
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="antigrav",
    version="1.0.0",
    author="Antigravity Platform",
    author_email="contact@antigravity.dev",
    description="A terminal-based coding agent extension for the antigravity platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seattleite626-netizen/antigravity-coding-agent",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Code Generators",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
        "requests>=2.28.0",
        "pyyaml>=6.0",
        "click>=8.0.0",
        "colorama>=0.4.4",
        "rich>=12.0.0",
        "composio-core>=0.4.0",
    ],
    entry_points={
        "console_scripts": [
            "antigrav=antigravity_agent:main",
        ],
    },
)