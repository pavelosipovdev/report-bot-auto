from aiogram import Router, types
from aiogram.fsm.context import FSMContext

import utils.connectors

router = Router()


async def find_colleges(inline_query: types.InlineQuery, state: FSMContext, str_for_replace: str):
    results = []

    query = inline_query.query
    query = query.replace(str_for_replace, "").strip()

    for college in utils.connectors.dict_colleges:
        if query.lower() in college["name"].lower() or query.lower() in college["tag"].lower():
            result = types.InlineQueryResultArticle(
                id=college["id"],
                title=college["name"],
                input_message_content=types.InputTextMessageContent(message_text="@" + college['tag']),
                description=college["tag"]
            )
            results.append(result)

    await inline_query.answer(results, cache_time=0)
