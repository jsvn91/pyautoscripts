from pywinauto import Application
app = Application(backend="win32").start('notepad.exe')
app.UntitledNotepad.minimize()
app.UntitledNotepad.Edit.set_text('some text\nsecond line')