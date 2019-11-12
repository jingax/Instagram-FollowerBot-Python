from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os


class FollowBot:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        # open login page
        bot.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(10)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.user)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(7)
        bot.find_element_by_class_name('HoLwm').click()
        # not now option for notifications on login
        time.sleep(3)

    def followpeps(self, hashtag):
        bot = self.bot
        search = bot.find_element_by_class_name('x3qfX')
        search.send_keys(hashtag)
        time.sleep(2)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        search.send_keys(Keys.RETURN)

        time.sleep(4)

        targets = bot.find_elements_by_class_name('_bz0w')
        print(len(targets))

        for target in targets:
            time.sleep(2)
            target.click()
            time.sleep(2)
            try:
                name = bot.find_element_by_class_name('nJAzx')
                val = name.get_attribute("title")
                print(val)
                follow = bot.find_elements_by_class_name('y3zKF')
                follow[1].click()
                if not os.path.exists("foll.txt"):
                    with open("foll.txt", "w") as f:
                        f.write(val)
                        f.write('\n')
                else:
                    with open("foll.txt", "a") as f:
                        f.write(val)
                        f.write('\n')
                f.close()

            except ElementClickInterceptedException:
                pass
            except NoSuchElementException:
                pass
            except IndexError:
                pass
            finally:
                pass
            time.sleep(2)
            bot.find_element_by_class_name('ckWGn').click()

# Enter your username and password
insta = FollowBot('your-username', 'your-password')
insta.login()
insta.followpeps('#noida')
