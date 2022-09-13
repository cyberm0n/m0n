import cv2,pyautogui,os,numpy

banner = r"""                                                                                                                 
                                               
                      ,a8888a,                 
                    ,8P"'  `"Y8,               
                   ,8P        Y8,              
88,dPYba,,adPYba,  88          88 8b,dPPYba,   
88P'   "88"    "8a 88          88 88P'   `"8a  
88      88      88 `8b        d8' 88       88  
88      88      88  `8ba,  ,ad8'  88       88  
88      88      88    "Y8888P"    88       88  v4.3

"""
print(banner)
a = input("[*]  path (.avi format)> ").strip().lower()

if a[-4:] ==".avi":
	output = a

else:
	print("[!] .avi format")
img = pyautogui.screenshot()
img = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
height, width, channels = img.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

print("[+]  Started The Record!")

while(True):
	try:
		img = pyautogui.screenshot()
		image = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
		out.write(image)
		StopIteration(0.5)
	except KeyboardInterrupt:
		print("[>]  Saved '"+output+"'")
		break

out.release()
cv2.destroyAllWindows()
