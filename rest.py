from aiohttp import ClientSession

from config import settings


async def get_html(direction: str, org: int):
    async with (
        ClientSession() as session,
        session.post(
            url=settings.SECRET_API,
            data={
                "action": "rating",
                "ratingForm": f"org={org}",
                "eduform": 1,
                "direction": 2,
                "competitionType": 0,
                "prof": direction,
                "originals": 1,
            },
            headers={
                "Authorization": "Basic ZXllOjNlMncxcQ==",
            },
        ) as data,
    ):
        return await data.text()
