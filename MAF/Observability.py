import asyncio
from agent_framework import ChatAgent
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from agent_framework.observability import configure_otel_providers
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk._logs.export import ConsoleLogRecordExporter 

# Console에 trace와 log를 출력하도록 설정
# 동시에 환경변수에 지정된 OTEL_EXPORTER_OTLP_ENDPOINT로도 전송됨 (Aspire Dashboard)
configure_otel_providers(
    exporters=[
        ConsoleSpanExporter(),        # Trace를 콘솔에 출력
        ConsoleLogRecordExporter()    # Log를 콘솔에 출력
    ]
)

# Create the agent - telemetry is automatically enabled
agent = ChatAgent(
    chat_client=AzureOpenAIChatClient(credential=AzureCliCredential()),
    name="Joker",
    instructions="You are good at telling jokes who responds in korean."
)

# Run the agent
async def main() -> None:
    result = await agent.run("Tell me a joke about a pirate.")
    print(result.text)

if __name__ == "__main__":
    asyncio.run(main())
