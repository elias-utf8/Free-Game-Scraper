# The licence of project
LICENCE = """
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Import all modules
try: # Setup try statement to catch the error
    import requests # Try to import requests
except ImportError: # If it has not been installed
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
    exit() # Exit the program



import json #Extract data
from colorama import Fore, Back, Style # Color for design :)

import os
os.system('cls' if os.name == 'nt' else 'clear')
import time
import ctypes



 # Pause

class GameScraper(): # Create object

	def __init__(self):
		self.fileName = "Instructions.txt"

	def main(self):

		ctypes.windll.kernel32.SetConsoleTitleW("Scraper - Made by KursK#1826")

		print(LICENCE)
		time.sleep(6)
		os.system('cls' if os.name == 'nt' else 'clear')
		print(Fore.WHITE)
		change = Style.RESET_ALL + Fore.CYAN
		change_2 = Style.RESET_ALL + Fore.BLUE
		card = f"""


      ::::::::   ::::::::  :::::::::      :::     :::::::::  :::::::::: :::::::::
    :+:    :+: :+:    :+: :+:    :+:   :+: :+:   :+:    :+: :+:        :+:    :+:
   +:+        +:+        +:+    +:+  +:+   +:+  +:+    +:+ +:+        +:+    +:+ {change}
  +#++:++#++ +#+        +#++:++#:  +#++:++#++: +#++:++#+  +#++:++#   +#++:++#:
        +#+ +#+        +#+    +#+ +#+     +#+ +#+        +#+        +#+    +#+
#+#    #+# #+#    #+# #+#    #+# #+#     #+# #+#        #+#        #+#    #+#{change_2}
########   ########  ###    ### ###     ### ###        ########## ###    ###



		"""


		self.slowType(card, .0001)
		print(Style.RESET_ALL)
		gameStand = Fore.CYAN +  "game stand" + Style.RESET_ALL
		Soft = Fore.CYAN + "softwares" + Style.RESET_ALL
		Others = Fore.CYAN + "others" + Style.RESET_ALL

		


		platformTable = "pc | ps4 | ps5 | xbox-one | xbox-series-xs | switch | android | ios | vr|  epic-games-store| steam | battlenet | origin | xbox-360 | drm-free | google"
		typeTable= "game | loot | beta"
		self.slowType(f"\nPlease select {Fore.GREEN}one{Style.RESET_ALL} platform preference, if so type it here or press enter to ignore:\n ", .02, newLine = False)
		print(Fore.CYAN + platformTable)
		print(Style.RESET_ALL)
		preferences = input('> ')

		if preferences == "":
			self.slowType(f"\nPlease select {Fore.GREEN}one{Style.RESET_ALL} type preference, if so type it here or press enter to ignore:\n ", .02, newLine = False)
			type = input('> ')
			if type == "":
				self.scrap()
			if type:
				self.scrap(type=type)

		if preferences:
			self.slowType(f"\nPlease select {Fore.GREEN}one{Style.RESET_ALL} type preference, if so type it here or press enter to ignore:\n ", .02, newLine = False)
			print(Fore.CYAN + typeTable)
			print(Style.RESET_ALL)
			type = input('> ')
			if type == "":
				print(f"filters : {preferences}")
				self.scrap(platform=preferences)
			if type:
				print(f"filters : {preferences}, {type}")
				self.scrap(platform=preferences, type=type)





	def scrap(self, platform=None, type=None):



		if platform and type:
			print(f"All result for [{Fore.CYAN + platform + Style.RESET_ALL}] and [{Fore.CYAN  + type + Style.RESET_ALL}]" )
			url = f"https://www.gamerpower.com/api/giveaways?platform={platform}&type={type}"
		elif platform:
			url = f"https://www.gamerpower.com/api/giveaways?platform={platform}"
			print(f"All result for [{ Fore.CYAN + platform + Style.RESET_ALL}]" )
		elif type:
			url = f"https://www.gamerpower.com/api/giveaways?type={type}"
			print(f"All result for [{Fore.CYAN + type + Style.RESET_ALL}]" )
		else:
			url = f"https://www.gamerpower.com/api/giveaways"

		response = requests.get(url).text
		response = json.loads(response)

		c = 0
		try:
			with open(self.fileName, "w", encoding="utf-8") as file:
				for i in response:
					c = c+1
					time.sleep(0.5)

					title = i['title']
					worth = i['worth']
					instructions = i['instructions']
					statu = i['status']
					typ = i['type']
					freeLabel = "FREE"

					freeLabels = Fore.GREEN + "FREE" + Style.RESET_ALL
					worthers = Fore.RED + worth + Style.RESET_ALL
					titles = Fore.BLUE + title + Style.RESET_ALL
					status = Fore.GREEN + statu + Style.RESET_ALL
					types = Fore.YELLOW + typ + Style.RESET_ALL

					print('{} - {} | , old price : {} - new price : {} | status : {}'.format(titles , types, worthers, freeLabels, status))

					
					file.write(f"{title} - {typ} - {worth} - {freeLabel} - {instructions}") # Load up the file in write mode

            
			print(f"Total results : {c}")
			self.slowType("Press enter for exit program", .02)
			end = input("")
			if end == "":
				exit()

		except TypeError:
			print("There is nothing giveaway here")
	def slowType(self, text, speed, newLine = True):
		for i in text:
			print(i, end = "", flush = True)
			time.sleep(speed)
		if newLine:
			print()



if __name__ == '__main__':
    Scrap = GameScraper()
    Scrap.main()
