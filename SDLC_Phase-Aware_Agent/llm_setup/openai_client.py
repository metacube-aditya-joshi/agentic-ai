from langchain.agents import create_agent
from langchain.chat_models  import init_chat_model
from langchain.checkpoint.memory import InMemorySaver

SYSTEM_PROMPT = """
You are an exprienced software developer which has extensive knowledge of software development lifecycle.
you give answers percise and with reason which help junior developer to understand the statement in a pretty easy fashion.
If any exprienced person ask you something you give a subtle and point to point answer which make the questioner statisfied.
"""
checkpointer = InMemorySaver()

model = init_chat_model(
    temprature =0.3,
    timeout=10,
)

agent = create_agent(
    model= model,
    system_prompt = SYSTEM_PROMPT,
    checkpointer = checkpointer
)

def ask_question(question):
    response = agent.invoke(question)
    return response