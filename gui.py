# Imports
from tkinter.filedialog import *
from libraries.guizero import *
from tkinter import filedialog
import os
print("finished importing libraries")
class workSpace:
    def __init__(self,id, name, workspaceType, width, height):
        self.id = id
        self.name = name
        self.workspaceType = workspaceType
        self.width = width
        self.height = height
print("finished defining classes")
themeType = 0
themesMemContent = ["Default Light"]
memInt = 0
themesDirContent = os.listdir("assets/themes")
for i in range(len(themesDirContent)):
    memItem = themesDirContent[memInt].replace("_", " ").replace("#", "").replace(".theme", "").title()
    themesMemContent.append(memItem)
    memInt = memInt + 1
themesMemContent.sort()
print("content of themes dir" + str(os.listdir("assets/themes")))
print("content of loaded themes" + str(themesMemContent))
# Opens .TXT, .SAV (only loger studios compiled savs and .LST)
def openFile():
    global textInput
    Tk().withdraw()   # we don't want a full GUI, so keep the root window from appearing
    fileContent = askopenfilename(defaultextension='lst', initialdir='projects', title="Open - loger file editor")  # show an "Open" dialog box and return the path to the selected file
    # Open the file in read mode
    if fileContent != '':
        with open(fileContent, 'r') as f:
            # Read the entire content of the file
            content = f.read()
        textInput.value = content
        # Close the file
    else:
        app.info("loger File editor", "Action Canceled")
    print("Open file")
def saveAs():
    files = [('loger script Text Document', '*.lst'),
             ('loger File editor theme', '*.theme'),
             ('Text Document', '*.txt'),
             ('All Files', '*.*')]
    file = filedialog.asksaveasfilename(filetypes=files,defaultextension=".lst", initialdir='projects', title="Save - loger file editor")
    if textInput.visible:
        fileContent = (textSTR.value + "\n" + bgHEX.value + "\n" + textINPTSTR.value + "\n" + themeTypeINT.value + "\n"
                   + inputBoxColorHEX.value + "\n")
    else:
        fileContent = textInput.value
    if file:  # user selected file
        with open(file, 'w') as f:
            f.write(fileContent)
            fd = open(file, "r")
            d = fd.read()
            fd.close()
            m = d.split("\n")
            s = "\n".join(m[:-1])
            fd = open(file, "w+")
            for i in range(len(s)):
                fd.write(s[i])
            fd.close()
    else:  # user cancel the file browser window
        app.info("loger File editor", "Action Canceled")
    print("Save file")
def newFile():
    files = [('All Files', '*.*'),
             ('loger script Text Document', '*.lst'),
             ('Text Document', '*.txt')]
    file = filedialog.asksaveasfilename(filetypes=files,defaultextension=".lst", initialdir='projects', title="New file - loger file editor")
    if file:  # user selected file
        fob = open(file,'x')
        fob.close()
    else:  # user cancel the file browser window
        app.info("loger File editor", "Action Canceled")
    print("New file")
def close():
    closeT = app.yesno("loger File editor", "Are you sure you want to quit? All unsaved progress will be lost.")
    if closeT:
        app.disable()
        app.destroy()
def fontColor():
    textInput.text_color = app.select_color(color='Black')
    print("Font color window opened")
def comingSoon():
    app.info("loger File editor", "This feature is still a work in progress.")
    print("It's not done yet 😤")  # It's not done yet 😤
def lfeCredits():
    creditsWind = Window(app, title="Credits - loger file editor", width=300, height=200)
    memBox = TitleBox(creditsWind, "")
    Text(memBox, text="-+{loger file editor}-+\n"
                           "Development - logerdex97\n"
                           "Github - logerdex97\n"
                           "guizero - lawsie and it's contributors\n"
                           "illum font - logerdex97\n"
                           "All themes - logerdex97\n"
                           "--=Special thanks=--\n"
                           "Python - The python team")
    print("Python credits:")
    credits()
    print(":)")
# ----------------------------------------------------------
def adConfig():
    global sizeSel, themeSel, configAd
    configAd = Window(app, title="Settings - loger File editor", width=400, height=300, layout="grid")
    # Config gui for advanced menu
    def formatSel():
        textInput.text_bold = bold.value
        textInput.text_italic = italix.value
        textInput.text_underline = underline.value
        textInput.text_size = sizeSel.value
        textInput.font = font.value
        updateFile()
        print("Updated all font values")
    def resetFont():
        bold.value = 0
        italix.value = 0
        underline.value = 0
        sizeSel.value = 11
        if themeType == 0:
            textInput.text_color = None
        elif themeType == 1:
            textInput.text_color = "White"
        font.value = "Courier New"
        formatSel()
        updateFile()
        print("Reset all font values")
    def theme():
        global themeType
        if themeSel.value == "Default Light":
            textInput.text_color = None
            app.bg = None
            app.text_color = None
            themeType = 0
            print("switched theme to: Default Light")
        else:
            # open the theme file selected
            file = open('assets/themes/' + themeSel.value.lower().strip().replace(" ", "_") + ".theme")
            # read the content of the file opened
            content = file.readlines()
            app.bg = content[1]
            app.text_color = content[2]
            themeType = int(content[3])
            textInput.bg = content[4]
            textInput.text_color = content[0]
            updateFile()
            print("switched theme to: " + themeSel.value)
    def resetTheme():
        themeSel.value = "Default Light"
        updateFile()
        theme()
    def updateFile():
        with open("options.properties", 'w') as file:
            file.write(str(sizeSel.value) + "\n" + themeSel.value)
    # Settings Wind:
    formatLabel = TitleBox(configAd, text='Font options', grid=[1,1])  # Font options
    bold = CheckBox(formatLabel, text='Bold', command=formatSel)
    italix = CheckBox(formatLabel, text='Italix', command=formatSel)
    underline = CheckBox(formatLabel, text="Underline", command=formatSel)
    PushButton(formatLabel, text='Font color', command=fontColor)  # Font Color
    Text(formatLabel, text="--Font size--")
    sizeSel = Slider(formatLabel, start=9, end=16, command=formatSel)
    Text(formatLabel, text="--Font--")
    font = Combo(formatLabel, command=formatSel, options=["Courier New", "Cascadia Code", "ilium", "Symbol",
                                                          "Times New Roman", "Webdings", "Wingdings", "Yu Gothic"])
    PushButton(formatLabel, text="Reset", command=resetFont)
    themeLabel = TitleBox(configAd, text="Theme options", grid=[2,1])  # Theme Options
    Text(themeLabel, text="--Theme--")
    themeSel = Combo(themeLabel, command=theme, options=themesMemContent)
    PushButton(themeLabel, text="Reset", command=resetTheme)
    configAd.visible = True
    updateSys()
    theme()
def themeEditor():
    global textSTR, bgHEX, textINPTSTR, themeTypeINT, inputBoxColorHEX
    appTextSTR = TitleBox(themeEditWorkSpace, text="app Text")
    textSTR = TextBox(appTextSTR)
    appBgHEX = TitleBox(themeEditWorkSpace, text="app BG HEX")
    bgHEX = TextBox(appBgHEX)
    textInputSTR = TitleBox(themeEditWorkSpace, text="Text Input Text STR")
    textINPTSTR = TextBox(textInputSTR)
    themeType = TitleBox(themeEditWorkSpace, text="Is dark theme")
    themeTypeINT = TextBox(themeType)
    inputBoxHEX = TitleBox(themeEditWorkSpace, text="Input box BG HEX")
    inputBoxColorHEX = TextBox(inputBoxHEX)
    PushButton(themeEditWorkSpace, text="Save theme", command=saveAs, height=1)
def textWrap():
    if textInput.wrap:
        textInput.wrap = False
    else:
        textInput.wrap = True
    print("Toggled text wrap")
def curserPOS():
    curserPOSV.value = "loger File Editor | " + textInput.cursor_position
def updateSys():
    with open('options.properties') as f:
        # read the content of the file opened
        content = f.readlines()
        sizeSel.value = content[0]
        if content[1] == "NULL":
            themeSel.value = "Default Light"
        else:
            themeSel.value = content[1]
def changeWS():
    if textWorkSpace.visible:
        textWorkSpace.visible = False
        themeEditWorkSpace.visible = True
    else:
        textWorkSpace.visible = True
        themeEditWorkSpace.visible = False
# Main Gui code
app = App(title="loger File editor", layout="center", width=800, height=600)
root = app.tk
# Hotkeys
root.bind("<Control-n>", lambda e: newFile())
root.bind("<Control-o>", lambda e: openFile())
root.bind("<Control-s>", lambda e: saveAs())
root.bind("<Control-q>", lambda e: close())

# Default workspaces
textWorkSpace = workSpace(id=1, name="Text Editor", workspaceType=1, width="fill", height="fill")
textWorkSpace = TitleBox(app, text=textWorkSpace.name, width=textWorkSpace.width, height=textWorkSpace.height)
themeEditWorkSpace = workSpace(id=2, name="Theme Editor", workspaceType=2, width=600, height=600)
themeEditWorkSpace = TitleBox(app, text=themeEditWorkSpace.name, width=themeEditWorkSpace.width, height=themeEditWorkSpace.height, visible=False)
themeEditor()

textInput = TextBox(textWorkSpace, width="fill", height="fill", multiline=True, command=curserPOS)
textInput.tk.bind("<Control-s>", lambda e: saveAs())
curserPOSV = Text(textWorkSpace, text="")

menubar = MenuBar(app,
                  toplevel=["File", "Edit", "View", "Tools"],
                  options=[
                      [["New", newFile], ["Open", openFile], ["Save as", saveAs], ["Exit", close]],  #File
                      [["Toggle text wrap", textWrap]],  #Edit
                      [["Change Editor type", changeWS], ["Credits", lfeCredits]],  #View
                      [["Settings (Beta)", adConfig]]  #Tools
                    ])

app.when_closed = close
app.icon = "assets/ico.png"
curserPOS()
app.when_clicked = curserPOS
adConfig()
configAd.visible = False
app.display()
