from aiogram import Router, types
from aiogram.fsm.context import FSMContext

import utils.connectors

router = Router()


async def find_colleges(inline_query: types.InlineQuery, state: FSMContext, str_for_replace: str):
    results = []

    query = inline_query.query
    query = query.replace(str_for_replace, "").strip()

    dict_template = utils.connectors.get_data_from_template()
    print(dict_template)
    for college in dict_template:
        print(college)
        if query.lower() in college["name"].lower():
            result = types.InlineQueryResultArticle(
                id=college["tag"],
                title=college["name"],
                input_message_content=types.InputTextMessageContent(message_text=college['name']),
                description=college["tag"]
            )
            results.append(result)

    await inline_query.answer(results, cache_time=0)
