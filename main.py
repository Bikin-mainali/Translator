
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob

root = Tk()
w=1100
h=800
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('Translator')
root.iconbitmap('translator.ico')

root.resizable(0,0 )
root.configure(bg='light blue')


lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}


def gg(event=None):
    try:
        word = TextBlob(varname1.get())
        lan = word.detect_language()
        lan_todict = languages.get()
        lan_to = lan_dict[lan_todict]
        word =word.translate(from_lang=lan,to=lan_to)
        #label3.configure(text = word)
        varname2.set(word)
    except:
        varname2.set('try another keyword')


def main_exit():
    notification = messagebox.askyesnocancel('Notification', 'you want to exit ?' , parent=root)
    if (notification == True):
        root.destroy()


#################binding function
def on_enterentry1(e):
    entrybox1['bg']= 'lightblue'
def on_leaveentry1(e):
    entrybox1['bg']= 'white'


def on_enterentry2(e):
    entrybox2['bg'] = 'lightblue'
def on_leaveentry2(e):
    entrybox2['bg']= 'white'


def on_enterbtn1(e):
    btn1['bg']= 'lightgreen'
def on_leavebtn1(e):
    btn1['bg']= 'white'


def on_enterbtn2(e):
    btn2['bg']= 'lightgreen'
def on_leavebtn2(e):
    btn2['bg'] = 'white'


##combobox language
languages= StringVar()
font_box = Combobox(root,width=30,textvariable=languages,state='readonly')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=0)

### ENTRY BOX
varname1 = StringVar()
entrybox1 =Entry(root,width=60,textvariable=varname1,font=('times', 20, 'italic '))
entrybox1.place(x=150, y=40)

varname2 = StringVar()
entrybox2 = Entry(root, width=60, textvariable=varname2, font=('times',20,'italic '))
entrybox2.place(x=150, y=100)

###label
label1 = Label(root, text='Enter words : ', font=('times', 15, 'italic bold'), bg='light blue')
label1.place(x=5, y=44)

label2 = Label(root, text='Translated : ', font=('times', 15, 'italic bold'), bg='light blue')
label2.place(x=5, y=106)

label3 = Label(root, text=' ', font=('times', 15, 'italic bold'), bg='light blue')
label3.place(x=10, y=350)

#button
imgbt1 = PhotoImage(file='touch-screen.png')
imgbt2 = PhotoImage(file='logout.png')

imgbt1 = imgbt1.subsample(10,10)
imgbt2 = imgbt2.subsample(14,14)


btn1 = Button(root,text='click',bd=10,bg='light green',activebackground='red',width=200,height=50,font=('times', 15, 'italic bold'),
              image=imgbt1, compound=RIGHT,command=gg)
btn1.place(x=150,y=200)

btn2 = Button(root,text='Exit',bd=10,bg='light green',activebackground='red',width=200, height=50,font=('times', 15, 'italic bold'),
              image=imgbt2, compound=RIGHT,command=main_exit)
btn2.place(x=500,y=200)
root.bind('<Return>',gg)


########Binding
entrybox1.bind('<Enter>',on_enterentry1)
entrybox1.bind('<Leave>',on_leaveentry1)

entrybox2.bind('<Enter>',on_enterentry2)
entrybox2.bind('<Leave>',on_leaveentry2)

btn1.bind('<Enter>',on_enterbtn1)
btn1.bind('<Leave>',on_leavebtn1)

btn2.bind('<Enter>',on_enterbtn2)
btn2.bind('<Leave>',on_leavebtn2)



root.mainloop()