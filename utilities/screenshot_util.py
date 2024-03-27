import os
from selenium.webdriver.remote.webdriver import WebDriver


def take_screenshot(driver: WebDriver, test_method_name: str):
    # Define the relative path to the 'screenshots' directory from the 'testcases' directory
    screenshots_dir = os.path.join(os.getcwd(), '..', 'screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)  # Create the directory if it doesn't exist

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
