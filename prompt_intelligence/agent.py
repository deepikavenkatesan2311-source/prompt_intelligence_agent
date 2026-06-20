from pathlib import Path

from google.adk import Agent
from google.adk.skills import load_skill_from_dir
from google.adk.tools.skill_toolset import SkillToolset

from .groq_litellm import GroqLiteLlm

SKILLS_DIR = Path(__file__).parent / "skills"

skill_toolset = SkillToolset(
    skills=[
        load_skill_from_dir(SKILLS_DIR / "analyze-draft"),
        load_skill_from_dir(SKILLS_DIR / "structure-prompt"),
    ],
)

root_agent = Agent(
    name="prompt_intelligence_coordinator",
    model=GroqLiteLlm(model="groq/openai/gpt-oss-20b"),
    description="Turns rough drafts into structured, token-efficient prompts.",
    instruction="""You are a prompt intelligence assistant.

You MUST call tools before responding:
1. Call `load_skill` with skill_name="analyze-draft" for rough drafts or new ideas.
2. Call `load_skill` with skill_name="structure-prompt" when the user wants the full structured prompt.
3. Call `load_skill_resource` when loaded skill instructions reference files under references/ or assets/.

Follow the loaded skill instructions exactly. Never skip tool calls.""",
    tools=[skill_toolset],
)
