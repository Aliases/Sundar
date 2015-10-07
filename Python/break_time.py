import webbrowser
import time
url = 'http://idiotinside.com'

total_breaks=3
break_count =0
print("Program started on "+time.ctime())
while (break_count<total_breaks):
	
	time.sleep(10)
	webbrowser.open_new(url) # opens in default browser
	break_count+=1
