import pyautogui
import subprocess
import os

class AutomateExpertTool():

    def __init__(self):
        self.expert_path= "res/ExPERT/ExPERT"
        self.iso_path = "\home\jsvn\Documents\WWE\Editing\WWE Smackdown - Here Comes The Pain.ISO"
        self.new_iso_path = ""

        self.open_expert_tool()

        # self.run_in_os_mode()
        self.extract_and_rebuild()



        pass

    def open_expert_tool(self):
        self.shellscript = subprocess.Popen(['wine',self.expert_path])

        # self.shellscript.
        pass

    def exit_expert_tool(self):
        self.shellscript.kill()

    def click_on_expert_button(self,res):
        location = None
        imageFile = res

        while (location == None):
            try:
                location = pyautogui.locateOnScreen(imageFile)
            except Exception as e:
                print(e)

        print(location)
        pyautogui.click(location)

    def extract_and_rebuild(self):
        self.click_on_expert_button('res/plugin_button_1.png')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        self.click_on_expert_button('res/open_iso_button_1.png')
        pyautogui.write(self.iso_path, interval=0.1)
        pyautogui.press('enter')

        self.click_on_expert_button('res/extract_lba_button_1.png')
        self.press_ok()
        self.click_on_expert_button('res/extract_file_button_1.png')
        self.press_ok()
        self.click_on_expert_button('res/rebuild_file_button_1.png')
        self.press_ok()
        self.click_on_expert_button('res/rebuild_lba_button_1.png')
        self.press_ok()

        self.exit_expert_tool()


    def press_ok(self):
        self.click_on_expert_button('res/ok_msg.png')
        pyautogui.press('enter')

    def run_in_os_mode(self):
        self.op = ""
        print("#" * 9, "1. Extract and Rebuild iso", "#" * 9)
        print("#" * 9, "3. Exit", "#" * 9)
        while True:

            self.op = input("Enter Your Input")
            """"""
            if self.op == "1":
                print("#" * 9, "Processing the input", "#" * 9)
                self.extract_and_rebuild()
                print("#" * 9, "End Processing", "#" * 9)
                pass
            elif self.op == "2":
                pass
            else:
                break
        exit()
        pass

a = AutomateExpertTool()
# a.open_expert_tool()