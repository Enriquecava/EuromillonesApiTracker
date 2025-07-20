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
        self.prize_category = page.locator('[data-cat=""]')
        self.prize_money = page.locator('[data-prize=""]')

    async def getNthPrizeCategory(self,value:int):
        category: str = await self.prize_category.nth(value).text_content()
        string = category.split('(')[1].split(')')[0]
        numbers = [int(c) for c in string if c.isdigit()]
        balls, stars = numbers
        return [balls,stars]
    
    async def getNthPrizeMoney(self,value:int):
        money: str = await self.prize_money.nth(value).text_content()
        format_money:str = money.replace(" €", "").replace(".", "").replace(",", ".")
        return format_money

    async def getPices(self):
        data={}
        for i in range(1,13):
            category= await self.getNthPrizeCategory(i)
            money = await self.getNthPrizeMoney(i)

            balls_key = str(category[0])
            stars_key = str(category[1])
            if balls_key not in data:
                data[balls_key] = {}

            data[balls_key][stars_key] = money
        
        return data

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
    