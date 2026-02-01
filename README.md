# Agent SDK Demo

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

## ECS Direct Execution

Run Claude Code on AWS Fargate using ECS Direct Execution for serverless, scalable agent deployments.

### Overview

ECS Direct Execution allows you to run Claude Code agents on AWS Fargate without managing infrastructure. This approach provides:
- Serverless execution with automatic scaling
- Pay-per-use pricing model
- No server maintenance or patching
- Isolated execution environments
- Integration with AWS services (CloudWatch, IAM, VPC)

### Prerequisites

- AWS CLI configured with appropriate credentials
- Docker installed locally
- AWS account with ECS and Fargate permissions
- Anthropic API key

### Setup

1. Build and push the Docker image:
```bash
docker build -t agent-sdk-demo .
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
docker tag agent-sdk-demo:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/agent-sdk-demo:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/agent-sdk-demo:latest
```

2. Create an ECS task definition:
```json
{
  "family": "claude-code-agent",
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "256",
  "memory": "512",
  "containerDefinitions": [
    {
      "name": "agent",
      "image": "<account-id>.dkr.ecr.us-east-1.amazonaws.com/agent-sdk-demo:latest",
      "environment": [
        {
          "name": "ANTHROPIC_API_KEY",
          "value": "your-api-key"
        }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/claude-code-agent",
          "awslogs-region": "us-east-1",
          "awslogs-stream-prefix": "ecs"
        }
      }
    }
  ]
}
```

3. Run the task using ECS Direct Execution:
```bash
aws ecs run-task \
  --cluster your-cluster-name \
  --launch-type FARGATE \
  --task-definition claude-code-agent \
  --network-configuration "awsvpcConfiguration={subnets=[subnet-xxxxx],securityGroups=[sg-xxxxx],assignPublicIp=ENABLED}"
```

### Best Practices

- Use AWS Secrets Manager or Parameter Store for API keys instead of environment variables
- Configure CloudWatch Logs for monitoring and debugging
- Set appropriate CPU and memory limits based on workload
- Use VPC endpoints for private communication with AWS services
- Implement proper IAM roles with least-privilege permissions
- Enable container insights for enhanced monitoring

### Cost Optimization

- Use Fargate Spot for non-critical workloads (up to 70% cost savings)
- Right-size CPU and memory allocations
- Implement task auto-scaling based on metrics
- Use scheduled tasks for predictable workloads

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