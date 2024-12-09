from deskframe.views.dialogBuilder import *
import os


class onCreate:
    def __init__(self, R):
        # button1 = R.getElementByID("button1")
        # button1.configure(command=self.print_button)
        pass

    def print_button(self):
        print("Button 1")


if __name__ == '__main__':
    win = Builder("activity_rename.xml")
    mainClass = onCreate(R=win)
    win.getMainLoop().mainloop()
