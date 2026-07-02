from playwright.sync_api import sync_playwright
import requests

URL = "https://services.rcsed.ac.uk/exams/exam-details-membership-in-orthodontics-part-b"

BOT_TOKEN = "8841127547:AAH3h1DLJIVrz7Vphi050tdPF4auYOcVhLM"
CHAT_ID = "676405292"

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg},
    )

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(URL, wait_until="networkidle")

    text = page.locator("body").inner_text()
    print(text)
print("Finished")

    if "There are currently no live dates for this exam" not in text:
        send(f"🚨 MOrth Part B قد يكون فتح!\n{URL}")

    browser.close()
