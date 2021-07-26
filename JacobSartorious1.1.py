import webbrowser
import time

delay = float(input("How long would you like the delay to be? "))

print("In order to stop this code from running, quit the process in your IDE.")
print("I am not responsible for any damage this creates.")
runInput = input("Would you like to run this? 'y' to run, anything else to quit. ")
rounds = 0 
while runInput == 'y':
	print("no stopping now!")
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
	webbrowser.open('https://www.youtube.com/watch?v=UuLk2A08svU')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=PmY-Lr8Bd_E')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=MxaCGoDqJ0M')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=fQPp-Hp0o2Q')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=DrRwBe_OVMQ')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=V3y6MQg662A')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=qO_jc3djl3g')
	time.sleep(delay)
	webbrowser.open('https://www.youtube.com/watch?v=gfKG8Afw6yg')
	time.sleep(delay)
	rounds = rounds + 1
	print(rounds)
else:
	print('run stopped')
	print('check out more projects from the creator here: ')
	print('julianagar.carrd.co')
