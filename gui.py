# Imports
from tkinter.filedialog import *
from guizero import *
from tkinter import filedialog
import keyboard
# Variables, lists and tuples
filetypes = ['.lst', '.lvl', '.sav', '.txt']
advConfigList_Fork = []
config_list = []
config_ad = []
Settings_Window = ()
Options_Text = ()
checkbox = ()
windA = ()
listLan = ()

# Opens .TXT, .SAV (only loger studios compiled savs and .LST)
def open_file():
    global filetypes, input_box
    Tk().withdraw()   # we don't want a full GUI, so keep the root window from appearing
    fileContent = askopenfilename(defaultextension='lst', initialdir='projects')  # show an "Open" dialog box and return the path to the selected file
    # Open the file in read mode
    if fileContent != '':

        file = open(fileContent, "r")

        # Read the entire content of the file
        content = file.read()
        input_box.value = content
        # Close the file
        file.close()
    else:
        app.info("loger File editor", "Action Canceled")
# Saves .LST
def save_as():
    global input_box
    files = [('loger script Text Document', '*.lst'),
             ('Text Document', '*.txt'),
             ('All Files', '*.*')
             ]
    file = filedialog.asksaveasfilename(
        filetypes=files,
        defaultextension=".lst", initialdir='projects')
    if file:  # user selected file
        fob = open(file,'w')
        fob.write(input_box.value)
        fob.close()
    else:  # user cancel the file browser window
        app.info("loger File editor", "Action Canceled")
    fd = open(file, "r")
    d = fd.read()
    fd.close()
    m = d.split("\n")
    s = "\n".join(m[:-1])
    fd = open(file, "w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
def save_as_txt():
    global input_box
    files = [('Text Document', '*.txt'),
             ('loger script Text Document', '*.lst'),
             ('All Files', '*.*')
             ]
    file = filedialog.asksaveasfilename(
        filetypes=files,
        defaultextension=".txt", initialdir='projects')
    if file:  # user selected file
        fob = open(file, 'w')
        fob.write(input_box.value)
        fob.close()
    else:  # user cancel the file browser window
        app.info("loger File editor", "Action Canceled")
    fd = open(file, "r")
    d = fd.read()
    fd.close()
    m = d.split("\n")
    s = "\n".join(m[:-1])
    fd = open(file, "w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
def newfile():
    files = [('All Files', '*.*'),
             ('loger script Text Document', '*.lst'),
             ('Text Document', '*.txt')]
    file = filedialog.asksaveasfilename(
        filetypes=files,
        defaultextension=".txt", initialdir='projects', title="New file")
    if file:  # user selected file
        fob = open(file,'x')
        fob.close()
    else:  # user cancel the file browser window
        app.info("loger File editor", "Action Canceled")
def close():
    closeT = app.yesno("loger File editor", "Are you sure you want to quit? All unsaved progress will be lost.")
    if closeT:
        app.disable()
        app.destroy()
    else:
        pass

def font_color():
    input_box.text_color = app.select_color(color='Black')

# Disables the app lol
def cooked():
    app.disable()
# It's not done yet 😤
def coming_soon():
    app.info("loger File editor", "This feature is still a work in progress.")
def jump_scare():
    spook = app.yesno("Warning", "Warning: This is a very scary photo. Not for the faint of heart")
    if spook:
        Scare = Window(app, title="Scary - loger File editor", layout="center")
        Picture(Scare, image='assets/spooky.png')
    else:
        app.info("Warning", "That's fair.")
# ----------------------------------------------------------
def ad_config():
    global config_list, config_ad, windA, listLan, advConfigList_Fork
    config_ad = Window(app, title="Settings - loger File editor", width=400, height=300, layout="auto")
    Text(config_ad, text="Select an option.")
    config_list = ListBox(config_ad, width=390, height=230, command=adv_config, items=[
        "Theme options (beta)"
    ])
    # Update to length of config list
    windA = Window(config_ad, visible=False, width=390, height=330)
    listLan = 1
    listCall = 0
    advConfigList_Fork = []
    for i in range(listLan):
        advConfigList_Fork.append(config_list.items[listCall])
        listCall = listCall + 1
    # Config writing
    # Config gui for advanced menu
    def formatSel():
        input_box.text_bold = bold.value
        input_box.text_italic = italix.value
        input_box.text_underline = underline.value
        input_box.text_size = sizeSel.value
        input_box.font = font.value
    def resetFont():
        bold.value = 0
        italix.value = 0
        underline.value = 0
        sizeSel.value = 11
        input_box.text_color = None
        font.value = "Courier New"
    # Wind A:
    formatLabel = TitleBox(windA, text='Font options')
    bold = CheckBox(formatLabel, text='Bold', command=formatSel)
    italix = CheckBox(formatLabel, text='Italix', command=formatSel)
    underline = CheckBox(formatLabel, text="Underline", command=formatSel)
    PushButton(formatLabel, text='Font color', command=font_color)  # Font Color
    Text(formatLabel, text="--Font size--")
    sizeSel = Slider(formatLabel, start=9, end=16, command=formatSel)
    Text(formatLabel, text="--Font--")
    font = Combo(formatLabel, command=formatSel, options=["Courier New", "Cascadia Code", "Symbol", "Times New Roman", "Webdings", "Wingdings", "Yu Gothic"])
    PushButton(formatLabel, text="Reset", command=resetFont)

def adv_config(value_of_input):
    # Gui for config
    config_list.value = value_of_input
    if value_of_input == advConfigList_Fork[0]:
        windA.title = value_of_input + " - loger File editor"
        windA.visible = True
def textWrap():
    if input_box.wrap:
        input_box.wrap = False
    else:
        input_box.wrap = True
# Main Gui code
app = App(title="loger File editor", layout="center", width=800, height=600)
input_box = TextBox(app, width="fill", height="fill", multiline=True, scrollbar=True)
text = Text(app, text="loger File Editor")
menubar = MenuBar(app,
                  toplevel=["File", "Edit", "Tools"],
                  options=[
                      [ ["New", newfile], ["Open", open_file], ["Save as", save_as], ["Save as TXT", save_as_txt], ["Exit", close] ],  #File
                      [ ["Toggle text wrap", textWrap] ],  #Edit
                      [ ["Settings (Beta)", ad_config] ]  #Tools
                    ])
# Hotkeys
keyboard.add_hotkey('ctrl + alt + t', ad_config)
keyboard.add_hotkey('ctrl + n', newfile)
keyboard.add_hotkey('ctrl + o', open_file)
keyboard.add_hotkey('ctrl + s', save_as)
keyboard.add_hotkey('ctrl + shift + s', save_as_txt)
app.when_closed = close
app.icon = "assets/ico.png"
app.display()
