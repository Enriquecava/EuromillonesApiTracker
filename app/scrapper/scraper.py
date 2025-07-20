from playwright.async_api import async_playwright
from scrapper.pom.lottery_page import LotteryPage
from collections import defaultdict

async def get_euromillones(fecha: str):
    url = f"https://www.combinacionganadora.com/euromillones/resultados/{fecha}"
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

        return {
            "date": fecha,
            "numbers": numbers,
            "stars": stars,
            "prices": data
        }
