import webbrowser
import time

print("Welcome to the Jacob Sartorius Music Video Spam Opener!")
print("")
print("For tips regarding the delay, refer to the README.md")
delay = int(input("How long would you like the delay to be? (in seconds)"))


print("In order to stop this code from running, quit the process in your IDE.")
print("I am not responsible for any damage this creates.")
runInput = input("Would you like to run this? 'y' to run, anything else to quit. ")

while runInput == 'y':
	webbrowser.open('https://www.youtube.com/watch?v=IvxRsDpXPGo')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=X6yXm88fCa4')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=1e_oDS5HwF8')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=yjnEi8gMlIA')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=6OSOVpEeqCc')
	time.sleep(delay)
else:
	print('check out more projects from the creator here: ')
	print('julianagar.carrd.co')
