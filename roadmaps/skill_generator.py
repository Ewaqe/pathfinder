import ast
from openai import OpenAI
from django.conf import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_topics(skill: str) -> list:
    return ast.literal_eval(get_answer_from_llm(settings.TOPICS_PROMPT_PATH, skill))


def generate_topic_text(skill: str, topic: str) -> str:
    user_prompt = f'Direction: {skill}\nTopic: {topic}'
    return get_answer_from_llm(settings.TOPIC_TEXT_PROMPT_PATH, user_prompt)


def get_answer_from_llm(prompt_path: str, user_prompt: str):
    with open(prompt_path, 'r') as file:
        prompt = file.read()
    messages = [
        {'role': 'system', 'content': prompt},
        {'role': 'user', 'content': user_prompt}
    ]
    chat = client.chat.completions.create(
        model='gpt-3.5-turbo', messages=messages
    )

    return chat.choices[0].message.content
