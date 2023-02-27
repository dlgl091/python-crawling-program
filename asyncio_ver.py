import aiohttp
import asyncio
import time
import settings as set
import pandas as pd


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status


async def main(url, date_list):
    async with aiohttp.ClientSession() as session:
        text = [asyncio.ensure_future(fetch(session, url.format(i)))
                   for i in date_list]
        res = await asyncio.gather(*text)
        return res

