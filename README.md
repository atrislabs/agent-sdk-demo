# Agent SDK Demo

[![GitHub stars](https://img.shields.io/github/stars/atrislabs/agent-sdk-demo?style=social)](https://github.com/atrislabs/agent-sdk-demo/stargazers)

A demonstration project showcasing the capabilities of the ATRIS Agent SDK. This project provides a foundation for building intelligent agents that can interact with various tools and APIs.

## Overview

This demo includes:
- Basic agent implementation with extensible architecture
- Example configurations and usage patterns
- Integration examples with common tools and services
- Development setup and testing utilities

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/atrislabs/agent-sdk-demo.git
cd agent-sdk-demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the demo agent:
```bash
python src/agent.py
```

## Project Structure

```
agent-sdk-demo/
├── README.md           # This file
├── requirements.txt    # Python dependencies
├── src/
│   └── agent.py       # Main agent implementation
└── atris/
    ├── MAP.md         # Codebase navigation
    ├── PERSONA.md     # Project conventions
    └── TODO.md        # Task tracking
```

## Usage

The demo agent can be customized and extended for various use cases:

```python
from src.agent import Agent

# Initialize agent
agent = Agent(config_path="config.json")

# Run agent
result = agent.run("Your task here")
print(result)
```

## Configuration

Agent behavior can be configured through:
- Environment variables
- Configuration files
- Runtime parameters

See `src/agent.py` for available configuration options.

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
This project follows PEP 8 conventions. Run formatting with:
```bash
black src/
flake8 src/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For questions and support, please visit the [ATRIS documentation](https://docs.atris.ai) or open an issue in this repository.

## Atris ecosystem

Demo for [atris](https://github.com/atrislabs/atris) · [member](https://github.com/atrislabs/member) · [clawhub-skills](https://github.com/atrislabs/clawhub-skills)