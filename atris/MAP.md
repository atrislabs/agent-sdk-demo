# MAP.md - Codebase Navigation

## Quick Reference
- grep-friendly index of key files

## By Feature
### Agent Core
- `src/agent.py` ⭐ - Main agent implementation class
- `README.md` - Project documentation and setup

### Configuration
- `requirements.txt` - Python dependencies
- Agent config loaded via JSON files or env vars

### Infrastructure & Validation
- `ECS_VALIDATED.md` - ECS Warm Pool validation report (Feb 1, 2026)

## Entry Points
- `src/agent.py` - Main agent class and demo runner
  - Run with: `python src/agent.py`
  - Import with: `from src.agent import Agent`

## Critical Files
- `src/agent.py` ⭐ - Files >100 lines marked with ⭐
  - Core Agent class (240+ lines)
  - Tool registration system
  - Task processing engine
  - Configuration management
  - Logging setup
  - Demo functionality
- `ECS_VALIDATED.md` ⭐ - Infrastructure validation documentation
  - ECS Warm Pool performance validation
  - Production readiness confirmation
  - Deployment configuration details

## Quick Navigation
```bash
# Run the demo
python src/agent.py

# Install dependencies  
pip install -r requirements.txt

# Check agent syntax
python -m py_compile src/agent.py

# Review infrastructure validation
cat ECS_VALIDATED.md
```