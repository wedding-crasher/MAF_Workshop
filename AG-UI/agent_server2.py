"""AG-UI server example."""

import os
from typing_extensions import Annotated
from pydantic import Field
import uvicorn
from agent_framework import ChatAgent
from agent_framework.azure import AzureOpenAIChatClient
from agent_framework_ag_ui import add_agent_framework_fastapi_endpoint
from azure.identity import AzureCliCredential
from fastapi import FastAPI

# Read required configuration
endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
deployment_name = os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

if not endpoint:
    raise ValueError("AZURE_OPENAI_ENDPOINT environment variable is required")
if not deployment_name:
    raise ValueError("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME environment variable is required")

chat_client = AzureOpenAIChatClient(
    credential=AzureCliCredential(),
    endpoint=endpoint,
    deployment_name=deployment_name,
)

# Create the AI agent
agent = ChatAgent(
    name="AGUIAssistant",
    instructions="You are a helpful assistant.",
    chat_client=chat_client,
)

# 날씨 정보를 제공하는 도구 함수 정의
def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is cloudy with a high of 15°C."

# 날씨 정보를 제공하는 Agent 생성
weather_agent = ChatAgent(
    name="AGUIAssistant",
    instructions="You are a helpful assistant.",
    chat_client=chat_client,
    tools=[get_weather]
)

# Create FastAPI app
app = FastAPI(title="AG-UI Server")

# Register the AG-UI endpoint
add_agent_framework_fastapi_endpoint(app, agent, "/")
add_agent_framework_fastapi_endpoint(app, weather_agent, "/weather")

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8888)