# PERSONA.md - Project Conventions

## Project Type
Python Agent SDK Demo - Demonstration project for building intelligent agents

## Code Style
- **Python**: PEP 8 compliant, type hints encouraged
- **Docstrings**: Google/NumPy style for classes and methods
- **Logging**: Structured logging with configurable levels
- **Error handling**: Explicit try/except blocks with meaningful messages
- **Configuration**: JSON files + environment variables + kwargs override pattern
- **Class design**: Single responsibility, clear interfaces, extensible architecture

## Workflow
### Development
```bash
# Setup
pip install -r requirements.txt

# Run demo
python src/agent.py

# Code quality
black src/
flake8 src/
mypy src/

# Testing
python -m pytest tests/
```

### Architecture Patterns
- **Agent class**: Central controller with tool registration
- **Tool system**: Plugin architecture for extensibility  
- **Context management**: Stateful conversation/task context
- **Configuration cascade**: File → env vars → runtime params
- **Logging hierarchy**: Agent.{name} namespace pattern

### Extension Points
- Override `_process_task()` for custom agent logic
- Register tools via `register_tool()` method  
- Custom configuration via JSON files or init params
- Context management for stateful operations