import pyautogui


location = None
imageFile = 'image.png'

while (location == None):
    try:
        location = pyautogui.locateOnScreen(imageFile)
    except Exception as e:
        print(e)

print(location)