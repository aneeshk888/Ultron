from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.parallel_agent import ParallelAgent

hair_care_agent = Agent(
    model='gemini-2.5-flash',
    name='hair_care_agent',
    description="I am your personal hair care advisor who provides tips and routines for healthy hair.",
    instruction="You are a helpful assistant who helps user to take care of thier hair in best possible ways by providing some routines to maintain an healthy hair",,
)
print("✅ Hair Care Agent created.")


skin_care_agent = Agent(
    model='gemini-2.5-flash',
    name='skin_care_agent',
    description="I am your personal skin care advisor who provides tips and routines for healthy skin.",
    instruction="You are a helpful assistant who helps user to take care of thier skins in best possible way by providing some routines to maintain healthy skin.",,
)
print("✅ Skin Care Agent created.")

gym_care_agent = Agent(
    model='gemini-2.5-flash',
    name='gym_care_agent',
    description="I am your personal fitness trainer who helps you stay fit and healthy through customized workout plans and nutrition advice.",
    instruction="Your are a helpful assistant who helps user plan stay fit, plan customized workout plans and gives best nutrition adivice",,
)
print("✅ Fitness Trainer Agent created.")


meal_planner_agent = Agent(
    model='gemini-2.5-flash',
    name='meal_planner_agent',
    description="I am your meal planner agent who helps user create healthy diet plans",
    instruction="You are a helpful assistant who helps user plan their diet plan best possible way to stay healthy and fit.",,
)
print("✅ Meal Planner Agent created.")

aggregator_agent = Agent(
    model='gemini-2.5-flash',
    name='health_aggregator_agent',
    description="I am an aggregator agent who combines the advice from hair care, skin care, fitness trainer, and meal planner agents to provide a comprehensive health and wellness plan.",
    instruction="You are a helpful assistant who combines the advice from hair care, skin care, fitness trainer, and meal planner agents to provide a comprehensive health and wellness plan.",,
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



retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)


