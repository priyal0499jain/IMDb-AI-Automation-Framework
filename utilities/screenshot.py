import os


class Screenshot:

    @staticmethod
    def capture(driver, name):

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        driver.save_screenshot(
            f"screenshots/{name}.png"
        )