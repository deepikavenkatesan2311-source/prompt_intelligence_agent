import asyncio
import os
import sys

from dotenv import load_dotenv

load_dotenv()

APP_NAME = "prompt_intelligence"
USER_ID = "local_user"


async def run_prompt(draft: str) -> None:
    from google.adk.runners import Runner
    from google.adk.sessions import InMemorySessionService
    from google.genai import types

    from prompt_intelligence.agent import root_agent

    groq_key = os.getenv("GROQ_API_KEY") or os.getenv("GROK_API_KEY")
    if groq_key and not os.getenv("GROQ_API_KEY"):
        os.environ["GROQ_API_KEY"] = groq_key

    if not os.getenv("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY not set in .env")
        sys.exit(1)

    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )

    content = types.Content(
        role="user",
        parts=[types.Part(text=draft)],
    )

    print(f"\nDraft: {draft}\n")
    print("Agent response:\n")

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=session.id,
        new_message=content,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            print(event.content.parts[0].text)


def main() -> None:
    draft = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Enter a rough prompt draft: ")
    asyncio.run(run_prompt(draft))


if __name__ == "__main__":
    main()