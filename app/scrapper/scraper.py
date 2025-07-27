from playwright.async_api import async_playwright
from scrapper.pom.lottery_page import LotteryPage
from storage import save_result, get_result_by_date
from typing import List
from storage import db
from collections import defaultdict

async def get_euromillones(date: str):
    url = f"https://www.combinacionganadora.com/euromillones/resultados/{date}"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(record_video_dir="videos/")
        page = await browser.new_page()
        lotteryPage = LotteryPage(page)
        await page.goto(url)
        
        numbers: List[str] = await lotteryPage.getLotteryNumber()
        stars: List[str] = await lotteryPage.getStarsNumber()

        data = await lotteryPage.getPices()

        await browser.close()
        print(f"Data for {numbers} and {stars} on {date}")
        save_result(date,numbers,stars, data)
        db.session.commit()

