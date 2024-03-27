import os
from selenium.webdriver.remote.webdriver import WebDriver


def take_screenshot(driver: WebDriver, test_method_name: str):
    # Ensure the 'screenshots' directory exists
    screenshots_dir = os.path.join(os.getcwd(), 'screenshots')
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Find the next available file name
    count = 1
    while True:
        screenshot_path = os.path.join(screenshots_dir, f"{test_method_name}_{count}.png")
        if not os.path.exists(screenshot_path):
            break
        count += 1

    # Take the screenshot
    driver.get_screenshot_as_file(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
