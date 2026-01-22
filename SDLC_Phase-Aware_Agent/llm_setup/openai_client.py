from agents import Agent ,Runner
from src.Request import Request

sdlc_instructions= None
model = None

sdlc_agent = Agent(
    name="SDLC Master",
    instructions = sdlc_instructions,
    model = model,
    tools=[],
    output_type=Request
)

async def ask_ai(quesiton):
    try:
        result = await Runner.run(sdlc_agent,quesiton)
        print("This is the result :\n",result.final_output)
    except :
        print("Error in answering the request ",quesiton)