from groq import AsyncGroq
from tenacity import retry, stop_after_attempt, wait_exponential
from config import GROQ_API_KEY, PRIMARY_MODEL, FALLBACK_MODEL

client = AsyncGroq(api_key=GROQ_API_KEY)


async def _call_model(model: str, prompt: str):
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content


@retry(stop=stop_after_attempt(2), wait=wait_exponential(min=1, max=5))
async def call_llm(prompt: str):
    try:
        return await _call_model(PRIMARY_MODEL, prompt)
    except Exception:
        return await _call_model(FALLBACK_MODEL, prompt)
