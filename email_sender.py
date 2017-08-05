# coding:utf-8

from Tkinter import *
from tkMessageBox import *

import smtplib
from email.mime.text import MIMEText

# resolve UnicodeDecodeError
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 构造方法
def send():
    SMTPserver = 'smtp.126.com'
    sender = 'superhin@126.com'
    password = 'hanzhichao520'

    message = content_txt.get(1.0, END)
    msg = MIMEText(message,'plain','utf-8')

    msg['Subject'] = subject_entry.get()
    msg['From'] = sender
    msg['To'] = receiver_entry.get()

    mailserver =smtplib.SMTP(SMTPserver, 25)
    mailserver.login(sender, password)
    mailserver.sendmail(sender, [sender], msg.as_string())
    mailserver.quit()
    showinfo('sucess', 'send email success')
    content_txt.delete(1.0, END)
    receiver_entry.delete(0, END)
    subject_entry.delete(0, END)

# 构造ui
root = Tk()
root.title('简单邮件发送器')
root.geometry('600x400+300+200')
root.resizable(False, False)

header = Frame(root)
receiver_lbl = Label(header, text='收件人')
receiver_entry = Entry(header, width=78)
subject_lbl = Label(header, text='主题')
subject_entry = Entry(header, width=78)
content_txt = Text(header, undo=True)

receiver_lbl.grid(row=0, column=0)
receiver_entry.grid(row=0, column=1)
subject_lbl.grid(row=1, column=0)
subject_entry.grid(row=1, column=1)
header.pack(side=TOP)

tool_bar = Frame(root)
send_btn= Button(tool_bar, text='发送', padx=10, command=send)
send_btn.pack(side=RIGHT)
tool_bar.pack(side=BOTTOM, fill=X)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

content_txt = Text(root, yscrollcommand=scroll.set)
scroll.config(command=content_txt.yview)
content_txt.pack(expand=YES, fill=BOTH)






root.mainloop()