# 19.02.2025
import customtkinter as ctk
import string
alphabet = string.ascii_lowercase
alphabet1 = string.ascii_uppercase


def сaesar_cipher(s1, step):
    s_new = ''
    for elem in s1:
        if elem.isalpha():
            if elem.isupper():
                a = alphabet1.index(elem)
                b = (a + step) % 26
                c = alphabet1[b]
                s_new += c
            else:
                a = alphabet.index(elem)
                b = (a + step) % 26
                c = alphabet[b]
                s_new += c
        else:
            s_new += elem


def handler_choose_combobox(selected_value):
    if selected_value == "Шифр Цезаря":
        widget_entry.configure(placeholder_text='Укажите шаг')
    if selected_value == "Шифр с кодовым словом":
        widget_entry.configure(placeholder_text='Укажите кодовое слово')


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


root = ctk.CTk()
root.title("Программа шифрования")
root.geometry("1000x500")
my_font = ctk.CTkFont(family="Roboto", size=20)

widget_label = ctk.CTkLabel(master=root)
widget_label.configure(text="Программа шифрования", font=my_font)

elems = ["Шифр Цезаря", "Шифр с кодовым словом"]
widget_combobox = ctk.CTkComboBox(master=root)
widget_combobox.configure(font=my_font, values=elems, state="readonly", width=400, command=handler_choose_combobox)
widget_combobox.set("Выберите шифр")

widget_entry = ctk.CTkEntry(master=root)
widget_entry.configure(font=my_font, placeholder_text="", width=250)

widget_entry1 = ctk.CTkEntry(master=root)
widget_entry1.configure(font=my_font, placeholder_text="Строка, которую хотите зашифровать", width=371)
widget_entry2 = ctk.CTkEntry(master=root)
widget_entry2.configure(font=my_font, placeholder_text="Результат", width=250, state='readonly')

widget_button = ctk.CTkButton(master=root)
widget_button.configure(font=my_font, text='Принять')

rows, columns = 6, 1
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

widget_label.grid(row=0, column=0)
widget_combobox.grid(row=1, column=0)
widget_entry.grid(row=2, column=0)
widget_entry1.grid(row=3, column=0)
widget_entry2.grid(row=4, column=0)
widget_button.grid(row=5, column=0)

root.mainloop()
