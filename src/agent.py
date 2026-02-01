"""
Agent SDK Demo - Main Agent Implementation

This module contains the core agent class that demonstrates the capabilities
of the ATRIS Agent SDK. The agent can be extended and customized for various
use cases and integrations.
"""

import json
import logging
import os
from typing import Any, Dict, List, Optional, Union


class Agent:
    """
    Main Agent class for the SDK demonstration.
    
    This agent provides a foundation for building intelligent systems that can:
    - Process natural language inputs
    - Execute tasks using various tools
    - Maintain conversation context
    - Handle configuration and state management
    """
    
    def __init__(self, config_path: Optional[str] = None, **kwargs):
        """
        Initialize the agent with configuration.
        
        Args:
            config_path (str, optional): Path to configuration file
            **kwargs: Additional configuration parameters
        """
        self.config = self._load_config(config_path, kwargs)
        self.logger = self._setup_logging()
        self.tools = {}
        self.context = {}
        
        self.logger.info("Agent initialized successfully")
    
    def _load_config(self, config_path: Optional[str], kwargs: Dict) -> Dict[str, Any]:
        """Load configuration from file and kwargs."""
        config = {
            'name': 'DemoAgent',
            'version': '1.0.0',
            'debug': False,
            'max_iterations': 10,
            'timeout': 30,
        }
        
        # Load from config file if provided
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    file_config = json.load(f)
                config.update(file_config)
            except Exception as e:
                print(f"Warning: Could not load config from {config_path}: {e}")
        
        # Override with kwargs
        config.update(kwargs)
        return config
    
    def _setup_logging(self) -> logging.Logger:
        """Set up logging for the agent."""
        logger = logging.getLogger(f"Agent.{self.config['name']}")
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        level = logging.DEBUG if self.config.get('debug') else logging.INFO
        logger.setLevel(level)
        
        return logger
    
    def register_tool(self, name: str, tool_function, description: str = ""):
        """
        Register a tool that the agent can use.
        
        Args:
            name (str): Tool name
            tool_function: Function to execute for this tool
            description (str): Tool description for the agent
        """
        self.tools[name] = {
            'function': tool_function,
            'description': description
        }
        self.logger.info(f"Registered tool: {name}")
    
    def run(self, task: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Execute a task using the agent.
        
        Args:
            task (str): The task to execute
            context (dict, optional): Additional context for the task
            
        Returns:
            Dict containing the result and metadata
        """
        self.logger.info(f"Starting task: {task}")
        
        # Update context
        if context:
            self.context.update(context)
        
        try:
            # Process the task
            result = self._process_task(task)
            
            response = {
                'success': True,
                'result': result,
                'task': task,
                'agent': self.config['name'],
                'version': self.config['version']
            }
            
            self.logger.info("Task completed successfully")
            return response
            
        except Exception as e:
            self.logger.error(f"Task failed: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'task': task,
                'agent': self.config['name']
            }
    
    def _process_task(self, task: str) -> str:
        """
        Process the given task. Override this method for custom logic.
        
        Args:
            task (str): Task to process
            
        Returns:
            str: Task result
        """
        # TODO: Implement actual agent logic here
        # This is a placeholder implementation
        
        if "hello" in task.lower():
            return f"Hello! I'm {self.config['name']}, ready to help."
        
        if "tools" in task.lower():
            available_tools = list(self.tools.keys())
            if available_tools:
                return f"Available tools: {', '.join(available_tools)}"
            else:
                return "No tools currently registered."
        
        if "status" in task.lower():
            return f"Agent {self.config['name']} v{self.config['version']} is running."
        
        # Default response
        return f"I received your task: '{task}'. This is a demo response - implement custom logic in _process_task()."
    
    def use_tool(self, tool_name: str, *args, **kwargs) -> Any:
        """
        Use a registered tool.
        
        Args:
            tool_name (str): Name of the tool to use
            *args, **kwargs: Arguments to pass to the tool
            
        Returns:
            Tool execution result
        """
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found. Available: {list(self.tools.keys())}")
        
        tool = self.tools[tool_name]
        self.logger.info(f"Using tool: {tool_name}")
        
        try:
            result = tool['function'](*args, **kwargs)
            self.logger.debug(f"Tool {tool_name} completed successfully")
            return result
        except Exception as e:
            self.logger.error(f"Tool {tool_name} failed: {str(e)}")
            raise
    
    def get_context(self, key: Optional[str] = None) -> Union[Dict, Any]:
        """Get context data."""
        if key:
            return self.context.get(key)
        return self.context.copy()
    
    def set_context(self, key: str, value: Any) -> None:
        """Set context data."""
        self.context[key] = value
        self.logger.debug(f"Updated context: {key}")
    
    def clear_context(self) -> None:
        """Clear all context data."""
        self.context.clear()
        self.logger.info("Context cleared")


def main():
    """
    Demo function showing basic agent usage.
    """
    print("=== ATRIS Agent SDK Demo ===")
    
    # Initialize agent
    agent = Agent(name="DemoAgent", debug=True)
    
    # Register a simple demo tool
    def demo_tool(message: str) -> str:
        return f"Demo tool executed with: {message}"
    
    agent.register_tool("demo", demo_tool, "A simple demonstration tool")
    
    # Run some demo tasks
    demo_tasks = [
        "hello",
        "what tools are available?",
        "show me your status",
        "process this demo task"
    ]
    
    for task in demo_tasks:
        print(f"\n> Task: {task}")
        result = agent.run(task)
        
        if result['success']:
            print(f"✓ Result: {result['result']}")
        else:
            print(f"✗ Error: {result['error']}")
    
    # Demonstrate tool usage
    print(f"\n> Using demo tool...")
    try:
        tool_result = agent.use_tool("demo", "Hello from the agent!")
        print(f"✓ Tool result: {tool_result}")
    except Exception as e:
        print(f"✗ Tool error: {e}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()