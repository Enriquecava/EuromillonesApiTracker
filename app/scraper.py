from playwright.async_api import async_playwright

async def get_euromillones(fecha: str):
    url = f"https://www.combinacionganadora.com/euromillones/resultados/{fecha}"
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        
        await page.wait_for_selector(".tabla-sorteos .sorteo")

        fila = page.locator(".tabla-sorteos .sorteo").first
        if not await fila.is_visible():
            await browser.close()
            return None

        bolas = await fila.locator(".numero").all_inner_texts()
        estrellas = await fila.locator(".estrella").all_inner_texts()

        await browser.close()

        return {
            "fecha": fecha,
            "numeros": [int(b) for b in bolas],
            "estrellas": [int(e) for e in estrellas]
        }
