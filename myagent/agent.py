from typing import Any, Dict
from google.adk.agents import ParallelAgent
from google.adk.agents import SequentialAgent
from google.adk.agents import Agent, LlmAgent
from google.adk.apps.app import App, EventsCompactionConfig

from google.adk.sessions import DatabaseSessionService
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.adk.tools.tool_context import ToolContext
from google.genai import types
print("✅ ADK components imported successfully.")

# Define helper functions that will be reused throughout the notebook
async def run_session(
    runner_instance: Runner,
    user_queries: list[str] | str = None,
    session_name: str = "default",
    user_id: str = "default",
    model_name: str = "gemini-2.5-flash-lite",
):
    """Runs a session with the agent.

    Args:
        runner_instance: The runner instance to use.
        user_queries: A list of user queries to send to the agent.
        session_name: The name of the session.
        user_id: The ID of the user.
        model_name: The name of the model to use.
    """
    print(f"\n ### Session: {session_name}")

    # Get app name from the Runner
    app_name = runner_instance.app_name

    # Attempt to create a new session or retrieve an existing one
    try:
        session = await session_service.create_session(
            app_name=app_name, user_id=user_id, session_id=session_name
        )
    except:
        session = await session_service.get_session(
            app_name=app_name, user_id=user_id, session_id=session_name
        )

    # Process queries if provided
    if user_queries:
        # Convert single query to list for uniform processing
        if type(user_queries) == str:
            user_queries = [user_queries]

        # Process each query in the list sequentially
        for query in user_queries:
            print(f"\nUser > {query}")

            # Convert the query string to the ADK Content format
            query = types.Content(role="user", parts=[types.Part(text=query)])

            # Stream the agent's response asynchronously
            async for event in runner_instance.run_async(
                user_id=user_id, session_id=session.id, new_message=query
            ):
                # Check if the event contains valid content
                if event.content and event.content.parts:
                    # Filter out empty or "None" responses before printing
                    if (
                        event.content.parts[0].text != "None"
                        and event.content.parts[0].text
                    ):
                        print(f"{model_name} > ", event.content.parts[0].text)
    else:
        print("No queries!")


print("✅ Helper functions defined.")


retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)


APP_NAME = "Ultron"  # Application
USER_ID = "default"  # User
SESSION = "default"  # Session
MODEL_NAME = "gemini-2.5-flash-lite"

def load_memory(tool_context: ToolContext) -> dict[str, Any]:
    """Tool to load memory from the session state."""
    return {"memory": tool_context.state.get("memory", "")}

hair_care_agent = Agent(
    model='gemini-2.5-flash',
    name='hair_care_agent',
    description="I am your personal hair care advisor who provides tips and routines for healthy hair.",
    instruction="You are a helpful assistant who helps user to take care of thier hair in best possible ways by providing some routines to maintain an healthy hair",
)
print("✅ Hair Care Agent created.")


skin_care_agent = Agent(
    model='gemini-2.5-flash',
    name='skin_care_agent',
    description="I am your personal skin care advisor who provides tips and routines for healthy skin.",
    instruction="You are a helpful assistant who helps user to take care of thier skins in best possible way by providing some routines to maintain healthy skin.",
)
print("✅ Skin Care Agent created.")

gym_care_agent = Agent(
    model='gemini-2.5-flash',
    name='gym_care_agent',
    description="I am your personal fitness trainer who helps you stay fit and healthy through customized workout plans and nutrition advice.",
    instruction="Your are a helpful assistant who helps user plan stay fit, plan customized workout plans and gives best nutrition adivice",
)
print("✅ Fitness Trainer Agent created.")


meal_planner_agent = Agent(
    model='gemini-2.5-flash',
    name='meal_planner_agent',
    description="I am your meal planner agent who helps user create healthy diet plans",
    instruction="You are a helpful assistant who helps user plan their diet plan best possible way to stay healthy and fit.",
)
print("✅ Meal Planner Agent created.")

aggregator_agent = Agent(
    model='gemini-2.5-flash',
    name='health_aggregator_agent',
    description="I am an aggregator agent who combines the advice from hair care, skin care, fitness trainer, and meal planner agents to provide a comprehensive health and wellness plan.",
    instruction="You are a helpful assistant who combines the advice from hair care, skin care, fitness trainer, and meal planner agents to provide a comprehensive health and wellness plan.",
)
print("✅ Aggregator Agent created.")


# The ParallelAgent runs all its sub-agents simultaneously.
Care_team = ParallelAgent(
    name="HealthCareTeam",
    sub_agents=[hair_care_agent, skin_care_agent, gym_care_agent, meal_planner_agent],
)

# This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.
root_agent = SequentialAgent(
    name="HealthAdvisor",
    sub_agents=[Care_team, aggregator_agent],
)

print("✅ Parallel and Sequential Agents created.")

# Step 2: Set up Session Management
# InMemorySessionService stores conversations in RAM (temporary)
# session_service = InMemorySessionService()

# Database session service
import sqlite3

def check_data_in_db():
    with sqlite3.connect("my_agent_data.db") as connection:
        cursor = connection.cursor()
        result = cursor.execute(
            "select app_name, session_id, author, content from events"
        )
        print([_[0] for _ in result.description])
        for each in result.fetchall():
            print(each)

db_url = "sqlite:///my_agent_data.db"  # Local SQLite file
session_service = DatabaseSessionService(db_url=db_url)



# Step 3: Create the Runner
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

print("✅ Stateful agent initialized!")
print(f"   - Application: {APP_NAME}")
print(f"   - User: {USER_ID}")
print(f"   - Using: {session_service.__class__.__name__}")

import asyncio

async def main():
    await run_session(
        runner,
        [
            "Hi, I am Sam! What is the capital of United States?",
            "Hello! What is my name?",  # This time, the agent should remember!
        ],
        "stateful-agentic-session",
    )
    check_data_in_db()

if __name__ == "__main__":
    asyncio.run(main())