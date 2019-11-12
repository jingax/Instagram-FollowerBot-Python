import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

if not os.path.exists("foll.txt"):
    exit(0)

with open("foll.txt", "r") as f:
    follow_names = f.readlines()
f.close()


class UnFollowBot:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(10)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        # password = bot.fin
        email.clear()
        # print(len(email))
        # print(len(password))
        password.clear()
        email.send_keys(self.user)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(7)
        block = bot.find_element_by_class_name('HoLwm').click()
        time.sleep(3)
        # print(len(block))

    def unfollowpeps(self, following_names):
        bot = self.bot

        for nam in following_names:
            try:
                search = bot.find_element_by_class_name('x3qfX')
                search.send_keys(nam.rstrip('\n'))
                time.sleep(2)
                search.send_keys(Keys.RETURN)
                time.sleep(2)
                search.send_keys(Keys.RETURN)
                time.sleep(4)
                unfollow_button = bot.find_elements_by_class_name('yZn4P')
                unfollow_button[0].click()
                time.sleep(2)
                # print(len(targets))
                bot.find_element_by_class_name('-Cab_').click()
                time.sleep(2)
                for name in follow_names:
                    print(name.rstrip('\n'))
                    with open('unfoll.txt', 'a+') as f:
                        f.write(name)
                    f.close()
                    print('kkkkk')

            except ElementClickInterceptedException:
                pass
            except NoSuchElementException:
                pass
            except IndexError:
                pass
            finally:
                pass

        with open("unfoll.txt", "r") as f:
            unfollow_names = f.readlines()
        f.close()

        if len(unfollow_names) == len(follow_names):
            os.remove('unfoll.txt')
            os.remove('foll.txt')


# Enter your username and password
insta = UnFollowBot('your-username', 'your-password')
insta.login()
insta.unfollowpeps(follow_names)
