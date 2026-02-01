from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)    

def after_step(context, step):
    if step.status == "failed":
        # create screenshots folder if not present
        os.makedirs("reports/screenshots", exist_ok=True)

        screenshot_path = f"reports/screenshots/{step.name}.png"
        context.driver.save_screenshot(screenshot_path)


def after_scenario(context, scenario):
    context.driver.quit()
