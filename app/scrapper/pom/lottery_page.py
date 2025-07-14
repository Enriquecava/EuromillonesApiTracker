from playwright.sync_api import Page, Locator

class LotteryPage:
    def __init__(self, page: Page):
        self.page = page
        self.numberOne: Locator = page.locator('ul[aria-label="Números"] >> li').nth(0)
        self.numberTwo: Locator =  page.locator('ul[aria-label="Números"] >> li').nth(1)
        self.numberThree: Locator = page.locator('ul[aria-label="Números"] >> li').nth(2)
        self.numberFour: Locator = page.locator('ul[aria-label="Números"] >> li').nth(3)
        self.numberFive: Locator = page.locator('ul[aria-label="Números"] >> li').nth(4)
        self.starOne: Locator = page.locator('[title="Estrellas"]').nth(0).locator('..')
        self.starTwo: Locator = page.locator('[title="Estrellas"]').nth(1).locator('..')

    async def  getFirstNumber(self):
        number: str = await self.numberOne.text_content()
        return number

    async def  getSecondNumber(self):
        number: str = await self.numberTwo.text_content()
        return number

    async def  getThirdNumber(self):
        number: str = await self.numberThree.text_content()
        return number

    async def  getFourthNumber(self):
        number: str = await self.numberFour.text_content()
        return number

    async def  getFithNumber(self):
        number: str = await self.numberFive.text_content()
        return number    

    async def  getFirstStar(self):
        content: str = await self.starOne.text_content()
        number: str = content.replace("E", "").strip()
        return number

    async def  getSecondStar(self):
        content: str = await self.starTwo.text_content()
        number: str = content.replace("E", "").strip()
        return number
    
    async def getLotteryNumber(self)-> list[str]:
        one: str = await self.getFirstNumber()
        two: str = await self.getSecondNumber()
        three: str = await self.getThirdNumber()
        four: str = await self.getFourthNumber()
        five: str = await self.getFithNumber()
        return [one,two,three,four,five]

    async def getStarsNumber(self)-> list[str]:
        one: str = await self.getFirstStar()
        two: str = await self.getSecondStar()
        return [one,two]
    