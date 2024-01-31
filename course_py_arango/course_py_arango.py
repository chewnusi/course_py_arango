from arango import ArangoClient
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# Initialize a client
client = ArangoClient(hosts="http://localhost:8529")

# Connect to the database
db = client.db("science_journal", username="root", password="")

#головна вкладка
root = Tk()
root.title('База даних науковий журнал')
root.iconbitmap('icon.ico')
root.geometry("1000x400")

#вкладки для таблиць
notebook = ttk.Notebook()
notebook.pack(expand=True, fill=BOTH)
author = ttk.Frame(notebook)
article = ttk.Frame(notebook)
annotation = ttk.Frame(notebook)
key_words = ttk.Frame(notebook)
reviewer = ttk.Frame(notebook)
review = ttk.Frame(notebook)
them_areas = ttk.Frame(notebook)

author.pack(fill=BOTH, expand=True)
article.pack(fill=BOTH, expand=True)
annotation.pack(fill=BOTH, expand=True)
key_words.pack(fill=BOTH, expand=True)
reviewer.pack(fill=BOTH, expand=True)
them_areas.pack(fill=BOTH, expand=True)
review.pack(fill=BOTH, expand=True)

notebook.add(author, text="Автори")
notebook.add(article, text="Статті")
notebook.add(annotation, text="Анотації")
notebook.add(key_words, text="Ключові слова")
notebook.add(reviewer, text="Рецензенти")
notebook.add(them_areas, text="Тематичні напрямки")
notebook.add(review, text="Рецензії")

#таблиці на вкладках
col_au = ('id_auth', 'name', 'surname', 'middle_name', 'phone_num', 'email')
col_ar = ('id_art', 'title', 'date', 'link')
col_ann = ('id_ann', 'id_ar', 'language', 'text')
col_kw = ('id_kw', 'kw_eng', 'kw_ukr')
col_revr = ('id_revr', 'name', 'surname', 'middle_name', 'email')
col_tha = ('id_tha', 'tha_eng', 'tha_ukr')
col_rev = ('id_rev', 'id_art', 'm_nov', 'm_topic', 'm_compll', 'm_complp', 'm_qual', 'conclusion', 'remarks')

tree_au = ttk.Treeview(author, columns=col_au, show='headings')
tree_ar = ttk.Treeview(article, columns=col_ar, show='headings')
tree_ann = ttk.Treeview(annotation, columns=col_ann, show='headings')
tree_kw = ttk.Treeview(key_words, columns=col_kw, show='headings')
tree_revr = ttk.Treeview(reviewer, columns=col_revr, show='headings')
tree_tha = ttk.Treeview(them_areas, columns=col_tha, show='headings')
tree_rev = ttk.Treeview(review, columns=col_rev, show='headings')

tree_au.heading('id_auth', text='Id-автора')
tree_au.heading('name', text='Ім`я')
tree_au.heading('surname', text='Прізвище')
tree_au.heading('middle_name', text='По батькові')
tree_au.heading('phone_num', text='Номер телефону')
tree_au.heading('email', text='Email')

tree_ar.heading('id_art', text='Id-статті')
tree_ar.heading('title', text='Заголовок')
tree_ar.heading('date', text='Дата')
tree_ar.heading('link', text='Посилання')

tree_ann.heading('id_ann', text='Id-анотації')
tree_ann.heading('id_ar', text='Id-статті')
tree_ann.heading('language', text='Мова')
tree_ann.heading('text', text='Текст')

tree_kw.heading('id_kw', text='Id-ключового слова')
tree_kw.heading('kw_eng', text='Ключове слово англійською')
tree_kw.heading('kw_ukr', text='Ключове слово українською')

tree_revr.heading('id_revr', text='Id-рецензенту')
tree_revr.heading('name', text='Ім`я')
tree_revr.heading('surname', text='Прізвище')
tree_revr.heading('middle_name', text='По батькові')
tree_revr.heading('email', text='Email')

tree_tha.heading('id_tha', text='Id-тематичного напряму')
tree_tha.heading('tha_eng', text='Тематичний напрямок англійською')
tree_tha.heading('tha_ukr', text='Тематичний напрямок українською')

tree_rev.heading('id_rev', text='Id-рецензії')
tree_rev.heading('id_art', text='Id-статті')
tree_rev.heading('m_nov', text='Новизна')
tree_rev.heading('m_topic', text='Актуальність')
tree_rev.heading('m_compll', text='Повнота літературного огляду')
tree_rev.heading('m_complp', text='Повнота викладення матеріалу')
tree_rev.heading('m_qual', text='Якість тексту')
tree_rev.heading('conclusion', text='Висновок')
tree_rev.heading('remarks', text='Зауваження')


#виведення записів
cursor = db.aql.execute('FOR doc IN author RETURN {_key: doc._key, Name: doc.Name, Surname: doc.Surname, MiddleName: doc.MiddleName, Phone: doc.PhoneNumber, Email: doc.Email}')
for doc in cursor:
     values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['Phone'], doc['Email'])
     tree_au.insert('', 'end', None, values=values)

cursor = db.aql.execute('FOR doc IN article RETURN {_key: doc._key, Title: doc.Title, Date: doc.Date, FileLink: doc.FileLink}')
for doc in cursor:
     values = (doc['_key'], doc['Title'], doc['Date'], doc['FileLink'])
     tree_ar.insert('', 'end', None, values=values)

cursor = db.aql.execute('FOR doc IN annotation RETURN {_key: doc._key, IdArticle: doc.IdArticle, Language: doc.Language, AnnotationText: doc.AnnotationText}')
for doc in cursor:
     values = (doc['_key'], doc['IdArticle'], doc['Language'], doc['AnnotationText'])
     tree_ann.insert('', 'end', None, values=values)

cursor = db.aql.execute('FOR doc IN key_words RETURN {_key: doc._key, KeyWordEng: doc.KeyWordEng, KeyWordUkr: doc.KeyWordUkr}')
for doc in cursor:
     values = (doc['_key'], doc['KeyWordEng'], doc['KeyWordUkr'])
     tree_kw.insert('', 'end', None, values=values)

cursor = db.aql.execute('FOR doc IN reviewer RETURN {_key: doc._key, Name: doc.Name, Surname: doc.Surname, MiddleName: doc.MiddleName, Email: doc.Email}')
for doc in cursor:
     values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['Email'])
     tree_revr.insert('', 'end', None, values=values)

cursor = db.aql.execute('FOR doc IN thematic_areas RETURN {_key: doc._key, ThematicAreaEng: doc.ThematicAreaEng, ThematicAreaUkr: doc.ThematicAreaUkr}')
for doc in cursor:
     values = (doc['_key'], doc['ThematicAreaEng'], doc['ThematicAreaUkr'])
     tree_tha.insert('', 'end', None, values=values)

cursor = db.aql.execute('FOR doc IN review RETURN {_key: doc._key, IdArticle: doc.IdArticle, MarkNovelty: doc.MarkNovelty, MarkTopicality: doc.MarkTopicality, MarkCompletnessL: doc.MarkCompletnessL, MarkCompletnessP: doc.MarkCompletnessP, MarkQuality: doc.MarkQuality, Conclusion: doc.Conclusion, Remarks: doc.Remarks}')
for doc in cursor:
     values = (doc['_key'], doc['IdArticle'], doc['MarkNovelty'], doc['MarkTopicality'], doc['MarkCompletnessL'], doc['MarkCompletnessP'], doc['MarkQuality'], doc['Conclusion'], doc['Remarks'])
     tree_rev.insert('', 'end', None, values=values)
 
tree_au.grid(row=1, column=0, sticky='nsew')
tree_ar.grid(row=1, column=0, sticky='nsew')
tree_ann.grid(row=1, column=0, sticky='nsew')
tree_kw.grid(row=1, column=0, sticky='nsew')
tree_revr.grid(row=1, column=0, sticky='nsew')
tree_tha.grid(row=1, column=0, sticky='nsew')
tree_rev.grid(row=1, column=0, sticky='nsew')

vscrollbar_1 = ttk.Scrollbar(author, orient= VERTICAL, command=tree_au.yview)
tree_au.configure(yscroll=vscrollbar_1.set)
vscrollbar_1.grid(row=1, column=1, sticky='ns')
vscrollbar_2 = ttk.Scrollbar(article, orient= VERTICAL, command=tree_ar.yview)
tree_ar.configure(yscroll=vscrollbar_2.set)
vscrollbar_2.grid(row=1, column=1, sticky='ns')
vscrollbar_3 = ttk.Scrollbar(annotation, orient= VERTICAL, command=tree_ann.yview)
tree_ann.configure(yscroll=vscrollbar_3.set)
vscrollbar_3.grid(row=1, column=1, sticky='ns')
vscrollbar_4 = ttk.Scrollbar(key_words, orient= VERTICAL, command=tree_kw.yview)
tree_kw.configure(yscroll=vscrollbar_4.set)
vscrollbar_4.grid(row=1, column=1, sticky='ns')
vscrollbar_5 = ttk.Scrollbar(reviewer, orient= VERTICAL, command=tree_revr.yview)
tree_revr.configure(yscroll=vscrollbar_5.set)
vscrollbar_5.grid(row=1, column=1, sticky='ns')
vscrollbar_6 = ttk.Scrollbar(them_areas, orient= VERTICAL, command=tree_tha.yview)
tree_tha.configure(yscroll=vscrollbar_6.set)
vscrollbar_6.grid(row=1, column=1, sticky='ns')
vscrollbar_7 = ttk.Scrollbar(review, orient= VERTICAL, command=tree_rev.yview)
tree_rev.configure(yscroll=vscrollbar_7.set)
vscrollbar_7.grid(row=1, column=1, sticky='ns')

hscrollbar_1 = ttk.Scrollbar(author, orient= HORIZONTAL, command=tree_au.xview)
tree_au.configure(xscroll=hscrollbar_1.set)
hscrollbar_1.grid(row=2, column=0, sticky='ew')
hscrollbar_2 = ttk.Scrollbar(article, orient= HORIZONTAL, command=tree_ar.xview)
tree_ar.configure(xscroll=hscrollbar_2.set)
hscrollbar_2.grid(row=2, column=0, sticky='ew')
hscrollbar_3 = ttk.Scrollbar(annotation, orient= HORIZONTAL, command=tree_ann.xview)
tree_ann.configure(xscroll=hscrollbar_3.set)
hscrollbar_3.grid(row=2, column=0, sticky='ew')
hscrollbar_4 = ttk.Scrollbar(key_words, orient= HORIZONTAL, command=tree_kw.xview)
tree_kw.configure(xscroll=hscrollbar_4.set)
hscrollbar_4.grid(row=2, column=0, sticky='ew')
hscrollbar_5 = ttk.Scrollbar(reviewer, orient= HORIZONTAL, command=tree_revr.xview)
tree_revr.configure(xscroll=hscrollbar_5.set)
hscrollbar_5.grid(row=2, column=0, sticky='ew')
hscrollbar_6 = ttk.Scrollbar(them_areas, orient= HORIZONTAL, command=tree_tha.xview)
tree_tha.configure(xscroll=hscrollbar_6.set)
hscrollbar_6.grid(row=2, column=0, sticky='ew')
hscrollbar_7 = ttk.Scrollbar(review, orient= HORIZONTAL, command=tree_rev.xview)
tree_rev.configure(xscroll=hscrollbar_7.set)
hscrollbar_7.grid(row=2, column=0, sticky='ew')

author.grid_rowconfigure(1, weight=1)
author.grid_columnconfigure(0, weight=1)
article.grid_rowconfigure(1, weight=1)
article.grid_columnconfigure(0, weight=1)
annotation.grid_rowconfigure(1, weight=1)
annotation.grid_columnconfigure(0, weight=1)
key_words.grid_rowconfigure(1, weight=1)
key_words.grid_columnconfigure(0, weight=1)
reviewer.grid_rowconfigure(1, weight=1)
reviewer.grid_columnconfigure(0, weight=1)
review.grid_rowconfigure(1, weight=1)
review.grid_columnconfigure(0, weight=1)
them_areas.grid_rowconfigure(1, weight=1)
them_areas.grid_columnconfigure(0, weight=1)

#панелі
p1 = ttk.Frame(author, height = 25, borderwidth=1, relief=SOLID)
p1.grid(row=0, column=0, sticky="EW", columnspan=2)
p2 = ttk.Frame(article, height = 25, borderwidth=1, relief=SOLID)
p2.grid(row=0, column=0, sticky="EW", columnspan=2)
p3 = ttk.Frame(annotation, height = 25, borderwidth=1, relief=SOLID)
p3.grid(row=0, column=0, sticky="EW", columnspan=2)
p4 = ttk.Frame(key_words, height = 25, borderwidth=1, relief=SOLID)
p4.grid(row=0, column=0, sticky="EW", columnspan=2)
p5 = ttk.Frame(reviewer, height = 25, borderwidth=1, relief=SOLID)
p5.grid(row=0, column=0, sticky="EW", columnspan=2)
p6 = ttk.Frame(review, height = 25, borderwidth=1, relief=SOLID)
p6.grid(row=0, column=0, sticky="EW", columnspan=2)
p7 = ttk.Frame(them_areas, height = 25, borderwidth=1, relief=SOLID)
p7.grid(row=0, column=0, sticky="EW", columnspan=2)
collection_au = db["author"]
collection_ar = db["article"]
collection_kw = db["key_words"]
collection_revr = db["reviewer"]
collection_tha = db["thematic_areas"]
collection_ann = db["annotation"]
collection_rev = db["review"]
#кнопки
def cadd_au():
    id_var = StringVar()
    n_var = StringVar()
    sn_var = StringVar()
    mn_var = StringVar()
    phn_var = StringVar()
    e_var = StringVar()
    def a():        
        id = id_var.get()
        n = n_var.get()
        sn = sn_var.get()
        mn = mn_var.get()
        phn = phn_var.get()
        e = e_var.get()
        query = 'FOR author IN author FILTER author._key == @id RETURN author._key'
        result = db.aql.execute(query, bind_vars={'id': id})
        if len(list(result)) > 0:
            messagebox.showerror("Помилка", "Запис з таким ID вже існує!")
        else:
          query = 'INSERT { _key: @id, Name: @n, Surname: @sn, MiddleName: @mn, PhoneNumber: @phn, Email: @e } INTO author'
          db.aql.execute(query, bind_vars={'id': id, 'n': n, 'sn': sn, 'mn': mn, 'phn': phn, 'e': e})
          messagebox.showinfo("Успіх", "Запис додано до таблиці!")
          add_nau.destroy()
          tree_au.delete(*tree_au.get_children())
          cursor = db.aql.execute('FOR doc IN author RETURN {_key: doc._key, Name: doc.Name, Surname: doc.Surname, MiddleName: doc.MiddleName, Phone: doc.PhoneNumber, Email: doc.Email}')
          for doc in cursor:
              values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['Phone'], doc['Email'])
              tree_au.insert('', 'end', None, values=values)
    add_nau = Toplevel()
    add_nau.title('Додавання')
    add_nau.iconbitmap('add.ico')
    add_nau.geometry("240x200")
    add_nau.resizable(FALSE, FALSE)
    p1 = ttk.Frame(add_nau)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    l1 = Label(p1, text="Id-автора:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(p1, text="Ім`я:").grid(row = 1, column = 0, sticky = W, pady = 2)
    l3 = Label(p1, text="Прізвище:").grid(row = 2, column = 0, sticky = W, pady = 2)
    l4 = Label(p1, text="По батькові:").grid(row = 3, column = 0, sticky = W, pady = 2)
    l5 = Label(p1, text="Номер телефону:").grid(row = 4, column = 0, sticky = W, pady = 2)
    l6 = Label(p1, text="Email:").grid(row = 5, column = 0, sticky = W, pady = 2)
    e1 = Entry(p1, textvariable = id_var).grid(row = 0, column = 1, pady = 2)
    e2 = Entry(p1, textvariable = n_var).grid(row = 1, column = 1, pady = 2)
    e3 = Entry(p1, textvariable = sn_var).grid(row = 2, column = 1, pady = 2)
    e4 = Entry(p1, textvariable = mn_var).grid(row = 3, column = 1, pady = 2)
    e5 = Entry(p1, textvariable = phn_var).grid(row = 4, column = 1, pady = 2)
    e6 = Entry(p1, textvariable = e_var).grid(row = 5, column = 1, pady = 2)
    b1 = Button(p1, text="Додати запис", command=a)
    b1.grid(row=6, column=1, pady=10)

def cdel_au():
    id_var = StringVar()
    phn_var = StringVar()
    e_var = StringVar()
    del_au = Toplevel()
    del_au.title('Видалення')
    del_au.iconbitmap('delete.ico')
    del_au.geometry("265x210")
    del_au.resizable(FALSE, FALSE)
    p1 = ttk.Frame(del_au)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        if var.get() == 1:  
           id = id_var.get()
           result = collection_au.find({'_key': id})
           if not result:
             messagebox.showerror("Помилка", "Запису з таким ID неіснує!")
           else:
             db.aql.execute("FOR doc IN author FILTER doc._key == @id LET authorId = doc._id FOR article IN article_author FILTER article._from == authorId REMOVE article IN article_author", bind_vars={'id': id})
             db.aql.execute("FOR doc IN author FILTER doc._key == @id REMOVE doc IN author", bind_vars={'id': id})
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_au.destroy()
             tree_au.delete(*tree_au.get_children())
             cursor = db.aql.execute('FOR doc IN author RETURN {_key: doc._key, Name: doc.Name, Surname: doc.Surname, MiddleName: doc.MiddleName, Phone: doc.PhoneNumber, Email: doc.Email}')
             for doc in cursor:
                  values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['Phone'], doc['Email'])
                  tree_au.insert('', 'end', None, values=values)
        elif var.get() == 2:  
           phn = phn_var.get()
           authors = db.aql.execute("FOR doc IN author FILTER doc.PhoneNumber == @phn RETURN doc._key", bind_vars={'phn': phn})
           if not authors:
              messagebox.showerror("Помилка", "Запису з таким номером телефону неіснує!")
           else:
             id_list = [author for author in authors]
             for id in id_list:
               db.aql.execute("FOR doc IN author FILTER doc._key == @id LET authorId = doc._id FOR article IN article_author FILTER article._from == authorId REMOVE article IN article_author", bind_vars={'id': id})
             db.aql.execute("FOR doc IN author FILTER doc.PhoneNumber LIKE @phn REMOVE doc IN author", bind_vars={'phn': phn})
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_au.destroy()
             tree_au.delete(*tree_au.get_children())
             cursor = db.aql.execute('FOR doc IN author RETURN {_key: doc._key, Name: doc.Name, Surname: doc.Surname, MiddleName: doc.MiddleName, Phone: doc.PhoneNumber, Email: doc.Email}')
             for doc in cursor:
                  values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['Phone'], doc['Email'])
                  tree_au.insert('', 'end', None, values=values)
        elif var.get() == 3:  
           e = e_var.get()
           authors = db.aql.execute("FOR doc IN author FILTER doc.Email == @e RETURN doc._key", bind_vars={'e': e})
           if not authors:
              messagebox.showerror("Помилка", "Запису з таким Email неіснує!")
           else:
             id_list = [author for author in authors]
             for id in id_list:
               db.aql.execute("FOR doc IN author FILTER doc._key == @id LET authorId = doc._id FOR article IN article_author FILTER article._from == authorId REMOVE article IN article_author", bind_vars={'id': id})
             db.aql.execute("FOR doc IN author FILTER doc.Email LIKE @e REMOVE doc IN author", bind_vars={'e': e})
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_au.destroy()
             tree_au.delete(*tree_au.get_children())
             cursor = db.aql.execute('FOR doc IN author RETURN {_key: doc._key, Name: doc.Name, Surname: doc.Surname, MiddleName: doc.MiddleName, Phone: doc.PhoneNumber, Email: doc.Email}')
             for doc in cursor:
                  values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['Phone'], doc['Email'])
                  tree_au.insert('', 'end', None, values=values)
    def enabl_1():
        for child in f1.winfo_children():
           child.configure(state='normal')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='normal')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    id_del = ttk.Radiobutton(p1, text="Видалення за Id", variable=var, value=1, command=enabl_1).grid(row=0, column=0, sticky=W, pady=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, sticky=W, pady=2)
    phone_del = ttk.Radiobutton(p1, text="Видалення за номером телефону", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    email_del = ttk.Radiobutton(p1, text="Видалення за Email", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2)
    f3 = ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id-автора:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть номер телефону:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Введіть Email:")
    l3.grid(row = 0, column = 0, sticky = W, pady = 2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =40)
    e2 = Entry(f2, textvariable = phn_var)
    e2.grid(row = 0, column = 1, pady = 2)
    e3 = Entry(f3, textvariable = e_var)
    e3.grid(row = 0, column = 1, pady = 2, padx = 60)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Видалити запис", command=a)
    b1.grid(row=6, column=0, pady=10, padx = 150)

def cupd_au():
    id_var = StringVar()
    n_var = StringVar()
    sn_var = StringVar()
    mn_var = StringVar()
    phn_var = StringVar()
    e_var = StringVar()
    def a():
      id_val = id_var.get()
      n_val = n_var.get()
      sn_val = sn_var.get()
      mn_val = mn_var.get()
      phn_val = phn_var.get()
      e_val = e_var.get()
      doc = collection_au[id_val]
      doc["Name"] = n_val
      doc["Surname"] = sn_val
      doc["MiddleName"] = mn_val
      doc["PhoneNumber"] = phn_val
      doc["Email"] = e_val
      collection.update(doc)
      messagebox.showinfo("Успіх", "Запис відредаговано!")
      upd_au.destroy()
      tree_au.delete(*tree_au.get_children())
      cursor = db.aql.execute('FOR doc IN author RETURN {_key: doc._key, Name: doc.Name, Surname: doc.Surname, MiddleName: doc.MiddleName, Phone: doc.PhoneNumber, Email: doc.Email}')
      for doc in cursor:
          values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['Phone'], doc['Email'])
          tree_au.insert('', 'end', None, values=values)
    if len(tree_au.selection()) > 0:
        upd_au = Toplevel()
        upd_au.title('Редагування')
        upd_au.iconbitmap('upd.ico')
        upd_au.geometry("265x210")
        upd_au.resizable(FALSE, FALSE)
        p1 = ttk.Frame(upd_au)
        p1.grid(row=0, column=0, sticky="nsew")
        p1.grid_rowconfigure(0, weight=1)
        p1.grid_columnconfigure(0, weight=1)
        l1 = Label(p1, text="Id-автора:").grid(row = 0, column = 0, sticky = W, pady = 2)
        l2 = Label(p1, text="Ім`я:").grid(row = 1, column = 0, sticky = W, pady = 2)
        l3 = Label(p1, text="Прізвище:").grid(row = 2, column = 0, sticky = W, pady = 2)
        l4 = Label(p1, text="По батькові:").grid(row = 3, column = 0, sticky = W, pady = 2)
        l5 = Label(p1, text="Номер телефону:").grid(row = 4, column = 0, sticky = W, pady = 2)
        l6 = Label(p1, text="Email:").grid(row = 5, column = 0, sticky = W, pady = 2)
        e1 = Entry(p1, textvariable = id_var, state='disable').grid(row = 0, column = 1, pady = 2)
        e2 = Entry(p1, textvariable = n_var).grid(row = 1, column = 1, pady = 2)
        e3 = Entry(p1, textvariable = sn_var).grid(row = 2, column = 1, pady = 2)
        e4 = Entry(p1, textvariable = mn_var).grid(row = 3, column = 1, pady = 2)
        e5 = Entry(p1, textvariable = phn_var).grid(row = 4, column = 1, pady = 2)
        e6 = Entry(p1, textvariable = e_var).grid(row = 5, column = 1, pady = 2)
        b1 = Button(p1, text="Редагувати запис", command=a)
        b1.grid(row=6, column=1, pady=10, padx = 0)
        selected_item = tree_au.selection()[0]
        record_data = tree_au.item(selected_item)['values']
        id_var.set(record_data[0])
        n_var.set(record_data[1])
        sn_var.set(record_data[2])
        mn_var.set(record_data[3])
        phn_var.set(record_data[4])
        e_var.set(record_data[5])
#
def cadd_ar():
    id_var = IntVar()
    title_var = StringVar()
    date_var = StringVar()
    link_var = StringVar()
    au_list = StringVar()
    kw_list = StringVar()
    def a():        
        id = id_var.get()
        title = title_var.get()
        date = date_var.get()
        link = link_var.get()
        cur.execute("SELECT IdArticle FROM article WHERE IdArticle=?", (id,))
        if cur.fetchone() is not None:
            messagebox.showerror("Помилка", "Запис з таким ID вже існує!")
        else:
          cur.execute("INSERT INTO article (IdArticle, Title, Date, FileLink) VALUES (?, ?, ?, ?)", (id, title, date, link))
          con.commit()
          aselected_indexes = list_au.curselection()
          kselected_indexes = list_kw.curselection()
          for index in aselected_indexes:
            auth = list_au.get(index)
            cur.execute("SELECT IdAuthor FROM author WHERE Surname || ' ' || Name || ' ' || MiddleName = ?", (auth,))
            auth_id = cur.fetchone()[0]
            cur.execute("INSERT INTO article_author (IdArticle, IdAuthor) VALUES (?, ?)", (id, auth_id))
          for index in kselected_indexes:
            keyw = list_kw.get(index)
            cur.execute("SELECT IdKeyWord FROM key_words WHERE KeyWordUkr = ?", (keyw,))
            kw_id = cur.fetchone()[0]
            cur.execute("INSERT INTO article_keywords (IdArticle, IdKeyWord) VALUES (?, ?)", (id, kw_id))
          con.commit()
          messagebox.showinfo("Успіх", "Запис додано до таблиці!")
          add_nar.destroy()
          tree_ar.delete(*tree_ar.get_children())
          cur.execute('SELECT * FROM article')
          rows = cur.fetchall()
          for row in rows:
              tree_ar.insert('', 'end', values=row)
    add_nar = Toplevel()
    add_nar.title('Додавання')
    add_nar.iconbitmap('add.ico')
    add_nar.geometry("240x285")
    add_nar.resizable(FALSE, FALSE)
    p1 = ttk.Frame(add_nar)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    l1 = Label(p1, text="Id-статті:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(p1, text="Заголовок:").grid(row = 1, column = 0, sticky = W, pady = 2)
    l3 = Label(p1, text="Дата написання:").grid(row = 2, column = 0, sticky = W, pady = 2)
    l4 = Label(p1, text="Посилання:").grid(row = 3, column = 0, sticky = W, pady = 2)
    l5 = Label(p1, text="Автор(и) статті:").grid(row = 4, column = 0, sticky = W, pady = 2)
    l6 = Label(p1, text="Ключові слова:").grid(row = 6, column = 0, sticky = W, pady = 2)
    e1 = Entry(p1, textvariable = id_var).grid(row = 0, column = 1, pady = 2)
    e2 = Entry(p1, textvariable = title_var).grid(row = 1, column = 1, pady = 2)
    e3 = Entry(p1, textvariable = date_var).grid(row = 2, column = 1, pady = 2)
    e4 = Entry(p1, textvariable = link_var).grid(row = 3, column = 1, pady = 2)

    au_values = [tree_au.item(child)["values"][2] + " " + tree_au.item(child)["values"][1] + " " + tree_au.item(child)["values"][3] for child in tree_au.get_children()]
    au_values_sorted = sorted(au_values)
    au_list.set(au_values_sorted)
    list_au = Listbox(p1, listvariable=au_list, selectmode=MULTIPLE, width=20, height=2, exportselection=False)
    list_au.grid(row = 4, column = 1, pady = 2)

    kw_values = [tree_kw.item(child)["values"][-1] for child in tree_kw.get_children()]
    kw_values_sorted = sorted(kw_values)
    kw_list.set(kw_values_sorted)
    list_kw = Listbox(p1, listvariable=kw_list, selectmode=MULTIPLE, width=20, height=2, exportselection=False)
    list_kw.grid(row = 6, column = 1, pady = 2)

    vscrollbar = ttk.Scrollbar(p1, orient=VERTICAL, command=list_au.yview)
    list_au.configure(yscroll=vscrollbar.set)
    vscrollbar.grid(row=4, column=2, sticky='ns')

    hscrollbar = ttk.Scrollbar(p1, orient= HORIZONTAL, command=list_au.xview)
    list_au.configure(xscroll=hscrollbar.set)
    hscrollbar.grid(row=5, column=1, sticky='ew')

    vscrollbar = ttk.Scrollbar(p1, orient=VERTICAL, command=list_kw.yview)
    list_kw.configure(yscroll=vscrollbar.set)
    vscrollbar.grid(row=6, column=2, sticky='ns')

    hscrollbar = ttk.Scrollbar(p1, orient= HORIZONTAL, command=list_kw.xview)
    list_kw.configure(xscroll=hscrollbar.set)
    hscrollbar.grid(row=7, column=1, sticky='ew')

    b1 = Button(p1, text="Додати запис", command=a)
    b1.grid(row=8, column=1, pady=10)

def cdel_ar():
    id_var = IntVar()
    t_var = StringVar()
    d_var = StringVar()
    del_ar = Toplevel()
    del_ar.title('Видалення')
    del_ar.iconbitmap('delete.ico')
    del_ar.geometry("260x260")
    del_ar.resizable(FALSE, FALSE)
    p1 = ttk.Frame(del_ar)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        if var.get() == 1:  
           id = id_var.get()
           cur.execute("SELECT IdArticle FROM article WHERE IdArticle=?", (id,))
           if cur.fetchone() is None:
             messagebox.showerror("Помилка", "Запису з таким ID неіснує!")
           else:
             cur.execute("DELETE FROM article_author WHERE IdArticle=?", (id,))
             cur.execute("DELETE FROM article_keywords WHERE IdArticle=?", (id,))
             cur.execute("DELETE FROM article WHERE IdArticle=?", (id,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_ar.destroy()
             tree_ar.delete(*tree_ar.get_children())
             cur.execute('SELECT * FROM article')
             rows = cur.fetchall()
             for row in rows:
                tree_ar.insert('', 'end', values=row)
        elif var.get() == 2:  
           t = t_var.get()
           cur.execute("SELECT IdArticle FROM article WHERE Title=?", (t,))
           rows = cur.fetchall()
           if not rows:
             messagebox.showerror("Помилка", "Запису з таким заголовком неіснує!")
           else:
             id_list = [row[0] for row in rows]
             for id in id_list:
                cur.execute("DELETE FROM article_author WHERE IdArticle=?", (id,))
             cur.execute("DELETE FROM article_keywords WHERE IdArticle=?", (id,))
             cur.execute("DELETE FROM article WHERE Title=?", (t,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_ar.destroy()
             tree_ar.delete(*tree_ar.get_children())
             cur.execute('SELECT * FROM article')
             rows = cur.fetchall()
             for row in rows:
                tree_ar.insert('', 'end', values=row)
        elif var.get() == 3:  
           d = d_var.get()
           if var1.get() == 1:
               cur.execute("DELETE FROM article_author WHERE IdArticle IN (SELECT IdArticle FROM article WHERE Date<?)", (d,))
               cur.execute("DELETE FROM article_keywords WHERE IdArticle IN (SELECT IdArticle FROM article WHERE Date<?)", (d,))
               cur.execute("DELETE FROM article WHERE Date<?", (d,))
               con.commit()
               messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
           elif var1.get() == 2:  
               cur.execute("SELECT Date FROM article WHERE Date=?", (d,))
               if cur.fetchone() is None:
                  messagebox.showerror("Помилка", "Запису з такою датою неіснує!")
               else:
                 cur.execute("DELETE FROM article_author WHERE IdArticle IN (SELECT IdArticle FROM article WHERE Date=?)", (d,))
                 cur.execute("DELETE FROM article_keywords WHERE IdArticle IN (SELECT IdArticle FROM article WHERE Date=?)", (d,))
                 cur.execute("DELETE FROM article WHERE Date=?", (d,))
                 con.commit()
                 messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
           elif var1.get() == 3:  
                 cur.execute("DELETE FROM article_author WHERE IdArticle IN (SELECT IdArticle FROM article WHERE Date>?)", (d,))
                 cur.execute("DELETE FROM article_keywords WHERE IdArticle IN (SELECT IdArticle FROM article WHERE Date>?)", (d,))
                 cur.execute("DELETE FROM article WHERE Date>?", (d,))
                 con.commit()
                 messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
           del_ar.destroy()
           tree_ar.delete(*tree_ar.get_children())
           cur.execute('SELECT * FROM article')
           rows = cur.fetchall()
           for row in rows:
                tree_ar.insert('', 'end', values=row)
    def enabl_1():
        for child in f1.winfo_children():
           child.configure(state='normal')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='normal')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    var1 = IntVar()
    id_del = ttk.Radiobutton(p1, text="Видалення за Id", variable=var, value=1, command=enabl_1).grid(row=0, column=0, sticky=W, pady=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, sticky=W, pady=2)
    title_del = ttk.Radiobutton(p1, text="Видалення за Заголовком", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    date_del = ttk.Radiobutton(p1, text="Видалення за Датою", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2)
    f3 = ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id-автора:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть заголовок:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Введіть дату:")
    l3.grid(row = 1, column = 0, sticky = W, pady = 2, padx=2)
    les = ttk.Radiobutton(f3, text="<", variable=var1, value=1).grid(row=0, column=1, sticky=W, pady=2)
    eq = ttk.Radiobutton(f3, text="=", variable=var1, value=2).grid(row=1, column=1, sticky=W, pady=2)
    more = ttk.Radiobutton(f3, text=">", variable=var1, value=3).grid(row=2, column=1, sticky=W, pady=2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =12)
    e2 = Entry(f2, textvariable = t_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =10)
    e3 = Entry(f3, textvariable = d_var)
    e3.grid(row = 1, column = 2, pady = 2, padx =10)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Видалити запис", command=a)
    b1.grid(row=6, column=0, pady=10, padx = 150)

def cupd_ar():
    id_var = IntVar()
    title_var = StringVar()
    date_var = StringVar()
    link_var = StringVar()
    def a():
      id = id_var.get()
      title = title_var.get()
      date = date_var.get()
      link = link_var.get()
      cur.execute("UPDATE article SET Title=?, Date=?, FileLink=? WHERE IdArticle=?", (title, date, link, id))
      con.commit()
      messagebox.showinfo("Успіх", "Запис відредаговано!")
      upd_ar.destroy()
      tree_ar.delete(*tree_ar.get_children())
      cur.execute('SELECT * FROM article')
      rows = cur.fetchall()
      for row in rows:
         tree_ar.insert('', 'end', values=row)
    if len(tree_ar.selection()) > 0:
        upd_ar = Toplevel()
        upd_ar.title('Редагування')
        upd_ar.iconbitmap('upd.ico')
        upd_ar.geometry("230x140")
        upd_ar.resizable(FALSE, FALSE)
        p1 = ttk.Frame(upd_ar)
        p1.grid(row=0, column=0, sticky="nsew")
        p1.grid_rowconfigure(0, weight=1)
        p1.grid_columnconfigure(0, weight=1)
        l1 = Label(p1, text="Id-статті:").grid(row = 0, column = 0, sticky = W, pady = 2)
        l2 = Label(p1, text="Заголовок:").grid(row = 1, column = 0, sticky = W, pady = 2)
        l3 = Label(p1, text="Дата написання:").grid(row = 2, column = 0, sticky = W, pady = 2)
        l4 = Label(p1, text="Посилання:").grid(row = 3, column = 0, sticky = W, pady = 2)
        e1 = Entry(p1, textvariable = id_var, state='disable').grid(row = 0, column = 1, pady = 2)
        e2 = Entry(p1, textvariable = title_var).grid(row = 1, column = 1, pady = 2)
        e3 = Entry(p1, textvariable = date_var).grid(row = 2, column = 1, pady = 2)
        e4 = Entry(p1, textvariable = link_var).grid(row = 3, column = 1, pady = 2)
        b1 = Button(p1, text="Редагувати запис", command=a)
        b1.grid(row=6, column=1, pady=10, padx = 0)
        selected_item = tree_ar.selection()[0]
        record_data = tree_ar.item(selected_item)['values']
        id_var.set(record_data[0])
        title_var.set(record_data[1])
        date_var.set(record_data[2])
        link_var.set(record_data[3])
#
def cadd_ann():
    id_var = IntVar()
    idar_var = IntVar()
    lan_var = StringVar()
    text_var = StringVar()
    def a():        
        id = id_var.get()
        idar = idar_var.get()
        lan = lan_var.get()
        text = text_var.get()
        cur.execute("SELECT IdAnnotation FROM annotation WHERE IdAnnotation=?", (id,))
        if cur.fetchone() is not None:
            messagebox.showerror("Помилка", "Запис з таким ID вже існує!")
        else:
          cur.execute("SELECT IdArticle FROM article WHERE IdArticle=?", (idar,))
          if cur.fetchone() is None:
              messagebox.showerror("Помилка", "Не існує статті з таким ID!")
          else:
            cur.execute("INSERT INTO annotation (IdAnnotation, IdArticle, Language, AnnotationText) VALUES (?, ?, ?, ?)", (id, idar, lan, text))
            con.commit()
            messagebox.showinfo("Успіх", "Запис додано до таблиці!")
            add_nann.destroy()
            tree_ann.delete(*tree_ann.get_children())
            cur.execute('SELECT * FROM annotation')
            rows = cur.fetchall()
            for row in rows:
                tree_ann.insert('', 'end', values=row)
    add_nann = Toplevel()
    add_nann.title('Додавання')
    add_nann.iconbitmap('add.ico')
    add_nann.geometry("220x150")
    add_nann.resizable(FALSE, FALSE)
    p1 = ttk.Frame(add_nann)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    l1 = Label(p1, text="Id-анотації").grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(p1, text="Id-статті:").grid(row = 1, column = 0, sticky = W, pady = 2)
    l3 = Label(p1, text="Мова:").grid(row = 2, column = 0, sticky = W, pady = 2)
    l4 = Label(p1, text="Текст анотації:").grid(row = 3, column = 0, sticky = W, pady = 2)
    e1 = Entry(p1, textvariable = id_var).grid(row = 0, column = 1, pady = 2)
    e2 = Entry(p1, textvariable = idar_var).grid(row = 1, column = 1, pady = 2)
    e3 = Entry(p1, textvariable = lan_var).grid(row = 2, column = 1, pady = 2)
    e4 = Entry(p1, textvariable = text_var).grid(row = 3, column = 1, pady = 2)
    b1 = Button(p1, text="Додати запис", command=a)
    b1.grid(row=6, column=1, pady=10)

def cdel_ann():
    id_var = IntVar()
    idar_var = IntVar()
    l_var = StringVar()
    del_ann = Toplevel()
    del_ann.title('Видалення')
    del_ann.iconbitmap('delete.ico')
    del_ann.geometry("250x210")
    del_ann.resizable(FALSE, FALSE)
    p1 = ttk.Frame(del_ann)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        if var.get() == 1:  
           id = id_var.get()
           cur.execute("SELECT IdAnnotation FROM annotation WHERE IdAnnotation=?", (id,))
           if cur.fetchone() is None:
             messagebox.showerror("Помилка", "Запису з таким ID неіснує!")
           else:
             cur.execute("DELETE FROM annotation WHERE IdAnnotation=?", (id,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_ann.destroy()
             tree_ann.delete(*tree_ann.get_children())
             cur.execute('SELECT * FROM annotation')
             rows = cur.fetchall()
             for row in rows:
                tree_ann.insert('', 'end', values=row)
        elif var.get() == 2:  
           idar = idar_var.get()
           cur.execute("SELECT IdAnnotation FROM annotation WHERE IdArticle=?", (idar,))
           if cur.fetchone() is None:
             messagebox.showerror("Помилка", "Запису з таким ID-статті неіснує!")
           else:
             cur.execute("DELETE FROM annotation WHERE IdArticle=?", (idar,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_ann.destroy()
             tree_ann.delete(*tree_ann.get_children())
             cur.execute('SELECT * FROM annotation')
             rows = cur.fetchall()
             for row in rows:
                tree_ann.insert('', 'end', values=row)
        elif var.get() == 3:  
           l = l_var.get()
           cur.execute("SELECT IdAnnotation FROM annotation WHERE Language=?", (l,))
           if cur.fetchone() is None:
             messagebox.showerror("Помилка", "Запису з такою мовою неіснує!")
           else:
             cur.execute("DELETE FROM annotation WHERE Language=?", (l,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_ann.destroy()
             tree_ann.delete(*tree_ann.get_children())
             cur.execute('SELECT * FROM annotation')
             rows = cur.fetchall()
             for row in rows:
                  tree_ann.insert('', 'end', values=row)
    def enabl_1():
        for child in f1.winfo_children():
           child.configure(state='normal')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='normal')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    id_del = ttk.Radiobutton(p1, text="Видалення за Id-анотації", variable=var, value=1, command=enabl_1).grid(row=0, column=0, sticky=W, pady=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, sticky=W, pady=2)
    title_del = ttk.Radiobutton(p1, text="Видалення за Id-статті", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    date_del = ttk.Radiobutton(p1, text="Видалення за мовою", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2)
    f3 = ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id-анотації:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть Id-статті:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Введіть мову:")
    l3.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =12)
    e2 = Entry(f2, textvariable = idar_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =26)
    e3 = Entry(f3, textvariable = l_var)
    e3.grid(row = 0, column = 1, pady = 2, padx =37)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Видалити запис", command=a)
    b1.grid(row=6, column=0, pady=10, padx = 150)

def cupd_ann():
    id_var = IntVar()
    idar_var = IntVar()
    lan_var = StringVar()
    text_var = StringVar()
    def a():
      id = id_var.get()
      idar = idar_var.get()
      lan = lan_var.get()
      text = text_var.get()
      cur.execute("SELECT IdArticle FROM article WHERE IdArticle=?", (idar,))
      if cur.fetchone() is None:
         messagebox.showerror("Помилка", "Не існує статті з таким ID!")
      else:
         cur.execute("UPDATE annotation SET IdArticle=?, Language=?, AnnotationText=? WHERE IdAnnotation=?", (idar, lan, text, id))
         con.commit()
         messagebox.showinfo("Успіх", "Запис відредаговано!")
         upd_ann.destroy()
         tree_ann.delete(*tree_ann.get_children())
         cur.execute('SELECT * FROM annotation')
         rows = cur.fetchall()
         for row in rows:
            tree_ann.insert('', 'end', values=row)
    if len(tree_ann.selection()) > 0:
        upd_ann = Toplevel()
        upd_ann.title('Редагування')
        upd_ann.iconbitmap('upd.ico')
        upd_ann.geometry("215x170")
        upd_ann.resizable(FALSE, FALSE)
        p1 = ttk.Frame(upd_ann)
        p1.grid(row=0, column=0, sticky="nsew")
        p1.grid_rowconfigure(0, weight=1)
        p1.grid_columnconfigure(0, weight=1)
        l1 = Label(p1, text="Id-анотації:").grid(row = 0, column = 0, sticky = W, pady = 2)
        l2 = Label(p1, text="Id-статті:").grid(row = 1, column = 0, sticky = W, pady = 2)
        l3 = Label(p1, text="Мова:").grid(row = 2, column = 0, sticky = W, pady = 2)
        l4 = Label(p1, text="Текст анотації:").grid(row = 3, column = 0, sticky = W, pady = 2)
        e1 = Entry(p1, textvariable = id_var, state='disabled').grid(row = 0, column = 1, pady = 2)
        e2 = Entry(p1, textvariable = idar_var).grid(row = 1, column = 1, pady = 2)
        e3 = Entry(p1, textvariable = lan_var).grid(row = 2, column = 1, pady = 2)
        e4 = Entry(p1, textvariable = text_var).grid(row = 3, column = 1, pady = 2)
        b1 = Button(p1, text="Редагувати запис", command=a)
        b1.grid(row=5, column=1, pady=10, padx = 0)
        selected_item = tree_ann.selection()[0]
        record_data = tree_ann.item(selected_item)['values']
        id_var.set(record_data[0])
        idar_var.set(record_data[1])
        lan_var.set(record_data[2])
        text_var.set(record_data[3])
#
def cadd_revr():    
    id_var = IntVar()
    n_var = StringVar()
    sn_var = StringVar()
    mn_var = StringVar()
    e_var = StringVar()
    tha_list = StringVar()
    def a():        
        id = id_var.get()
        n = n_var.get()
        sn = sn_var.get()
        mn = mn_var.get()
        e = e_var.get()
        cur.execute("SELECT IdReviewer FROM reviewer WHERE IdReviewer=?", (id,))
        if cur.fetchone() is not None:
            messagebox.showerror("Помилка", "Запис з таким ID вже існує!")
        else:
          cur.execute("INSERT INTO reviewer (IdReviewer, Name, Surname, MiddleName, Email) VALUES (?, ?, ?, ?, ?)", (id, n, sn, mn, e))
          con.commit()
          selected_indexes = list_tha.curselection()
          for index in selected_indexes:
            thematic_area = list_tha.get(index)
            cur.execute("SELECT IdThematicArea FROM thematic_areas WHERE ThematicAreaUkr = ?", (thematic_area,))
            thematic_area_id = cur.fetchone()[0]
            cur.execute("INSERT INTO reviewer_thematicareas (IdReviewer, IdThematicArea) VALUES (?, ?)", (id, thematic_area_id))
          con.commit()
          messagebox.showinfo("Успіх", "Запис додано до таблиці!")
          add_nrevr.destroy()
          tree_revr.delete(*tree_revr.get_children())
          cur.execute('SELECT * FROM reviewer')
          rows = cur.fetchall()
          for row in rows:
              tree_revr.insert('', 'end', values=row)
    add_nrevr = Toplevel()
    add_nrevr.title('Додавання')
    add_nrevr.iconbitmap('add.ico')
    add_nrevr.geometry("310x240")
    add_nrevr.resizable(FALSE, FALSE)
    p1 = ttk.Frame(add_nrevr)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    l1 = Label(p1, text="Id-рецензента:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(p1, text="Ім`я:").grid(row = 1, column = 0, sticky = W, pady = 2)
    l3 = Label(p1, text="Прізвище:").grid(row = 2, column = 0, sticky = W, pady = 2)
    l4 = Label(p1, text="По батькові:").grid(row = 3, column = 0, sticky = W, pady = 2)
    l5 = Label(p1, text="Email:").grid(row = 4, column = 0, sticky = W, pady = 2)
    l6 = Label(p1, text="Оберіть тематичні напрямки").grid(row = 5, column = 0, sticky = W, pady = 2)
    e1 = Entry(p1, textvariable = id_var).grid(row = 0, column = 1, pady = 2)
    e2 = Entry(p1, textvariable = n_var).grid(row = 1, column = 1, pady = 2)
    e3 = Entry(p1, textvariable = sn_var).grid(row = 2, column = 1, pady = 2)
    e4 = Entry(p1, textvariable = mn_var).grid(row = 3, column = 1, pady = 2)
    e5 = Entry(p1, textvariable = e_var).grid(row = 4, column = 1, pady = 2)
    tha_values = [tree_tha.item(child)["values"][-1] for child in tree_tha.get_children()]
    tha_values_sorted = sorted(tha_values)
    tha_list.set(tha_values_sorted)
    list_tha = Listbox(p1, listvariable=tha_list, selectmode=MULTIPLE, width=20, height=2)
    list_tha.grid(row = 5, column = 1, pady = 2)

    vscrollbar = ttk.Scrollbar(p1, orient=VERTICAL, command=list_tha.yview)
    list_tha.configure(yscroll=vscrollbar.set)
    vscrollbar.grid(row=5, column=2, sticky='ns')

    hscrollbar = ttk.Scrollbar(p1, orient= HORIZONTAL, command=list_tha.xview)
    list_tha.configure(xscroll=hscrollbar.set)
    hscrollbar.grid(row=6, column=1, sticky='ew')

    b1 = Button(p1, text="Додати запис", command=a)
    b1.grid(row=7, column=1, pady=10)

def cdel_revr():
    id_var = IntVar()
    e_var = StringVar()
    del_revr = Toplevel()
    del_revr.title('Видалення')
    del_revr.iconbitmap('delete.ico')
    del_revr.geometry("240x155")
    del_revr.resizable(FALSE, FALSE)
    p1 = ttk.Frame(del_revr)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        if var.get() == 1:  
           id = id_var.get()
           cur.execute("SELECT IdReviewer FROM reviewer WHERE IdReviewer=?", (id,))
           if cur.fetchone() is None:
             messagebox.showerror("Помилка", "Запису з таким ID неіснує!")
           else:
             cur.execute("DELETE FROM reviewer_thematicareas WHERE IdReviewer=?", (id,))
             cur.execute("DELETE FROM review_reviewer WHERE IdReviewer=?", (id,))
             cur.execute("DELETE FROM reviewer WHERE IdReviewer=?", (id,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_revr.destroy()
             tree_revr.delete(*tree_revr.get_children())
             cur.execute('SELECT * FROM reviewer')
             rows = cur.fetchall()
             for row in rows:
                tree_revr.insert('', 'end', values=row)
        elif var.get() == 2:  
           e = e_var.get()
           cur.execute("SELECT IdReviewer FROM reviewer WHERE Email=?", (e,))
           rows = cur.fetchall()
           if not rows:
              messagebox.showerror("Помилка", "Запису з таким Email неіснує!")
           else:
             id_list = [row[0] for row in rows]
             for id in id_list:
               cur.execute("DELETE FROM reviewer_thematicareas WHERE IdReviewer=?", (id,))
               cur.execute("DELETE FROM review_reviewer WHERE IdReviewer=?", (id,))
             cur.execute("DELETE FROM reviewer WHERE Email LIKE ?", (e,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_revr.destroy()
             tree_revr.delete(*tree_revr.get_children())
             cur.execute('SELECT * FROM reviewer')
             rows = cur.fetchall()
             for row in rows:
                tree_revr.insert('', 'end', values=row)
    def enabl_1():
        for child in f1.winfo_children():
           child.configure(state='normal')
        for child in f2.winfo_children():
           child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    id_del = ttk.Radiobutton(p1, text="Видалення за Id", variable=var, value=1, command=enabl_1).grid(row=0, column=0, sticky=W, pady=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, sticky=W, pady=2)
    phone_del = ttk.Radiobutton(p1, text="Видалення за Email", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id-автора:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть Email:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =10)
    e2 = Entry(f2, textvariable = e_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =33)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Видалити запис", command=a)
    b1.grid(row=4, column=0, pady=10, padx = 120)

def cupd_revr():
    id_var = IntVar()
    n_var = StringVar()
    sn_var = StringVar()
    mn_var = StringVar()
    e_var = StringVar()
    def a():
      id_val = id_var.get()
      n_val = n_var.get()
      sn_val = sn_var.get()
      mn_val = mn_var.get()
      e_val = e_var.get()
      cur.execute("UPDATE reviewer SET Name=?, Surname=?, MiddleName=?, Email=? WHERE IdReviewer=?", (n_val, sn_val, mn_val, e_val, id_val))
      con.commit()
      messagebox.showinfo("Успіх", "Запис відредаговано!")
      upd_revr.destroy()
      tree_revr.delete(*tree_revr.get_children())
      cur.execute('SELECT * FROM reviewer')
      rows = cur.fetchall()
      for row in rows:
         tree_revr.insert('', 'end', values=row)
    if len(tree_revr.selection()) > 0:
        upd_revr = Toplevel()
        upd_revr.title('Редагування')
        upd_revr.iconbitmap('upd.ico')
        upd_revr.geometry("215x170")
        upd_revr.resizable(FALSE, FALSE)
        p1 = ttk.Frame(upd_revr)
        p1.grid(row=0, column=0, sticky="nsew")
        p1.grid_rowconfigure(0, weight=1)
        p1.grid_columnconfigure(0, weight=1)
        l1 = Label(p1, text="Id-рецензента:").grid(row = 0, column = 0, sticky = W, pady = 2)
        l2 = Label(p1, text="Ім`я:").grid(row = 1, column = 0, sticky = W, pady = 2)
        l3 = Label(p1, text="Прізвище:").grid(row = 2, column = 0, sticky = W, pady = 2)
        l4 = Label(p1, text="По батькові:").grid(row = 3, column = 0, sticky = W, pady = 2)
        l5 = Label(p1, text="Email:").grid(row = 4, column = 0, sticky = W, pady = 2)
        e1 = Entry(p1, textvariable = id_var, state='disable').grid(row = 0, column = 1, pady = 2)
        e2 = Entry(p1, textvariable = n_var).grid(row = 1, column = 1, pady = 2)
        e3 = Entry(p1, textvariable = sn_var).grid(row = 2, column = 1, pady = 2)
        e4 = Entry(p1, textvariable = mn_var).grid(row = 3, column = 1, pady = 2)
        e5 = Entry(p1, textvariable = e_var).grid(row = 4, column = 1, pady = 2)
        b1 = Button(p1, text="Редагувати запис", command=a)
        b1.grid(row=5, column=1, pady=10, padx = 0)
        selected_item = tree_revr.selection()[0]
        record_data = tree_revr.item(selected_item)['values']
        id_var.set(record_data[0])
        n_var.set(record_data[1])
        sn_var.set(record_data[2])
        mn_var.set(record_data[3])
        e_var.set(record_data[4])
#
def cadd_tha():
    id_var = IntVar()
    eng_var = StringVar()
    ukr_var = StringVar()
    def a():        
        id = id_var.get()
        eng = eng_var.get()
        ukr = ukr_var.get()
        cur.execute("SELECT IdThematicArea FROM thematic_areas WHERE IdThematicArea=?", (id,))
        if cur.fetchone() is not None:
            messagebox.showerror("Помилка", "Запис з таким ID вже існує!")
        else:
          cur.execute("INSERT INTO thematic_areas (IdThematicArea, ThematicAreaEng, ThematicAreaUkr) VALUES (?, ?, ?)", (id, eng, ukr))
          con.commit()
          messagebox.showinfo("Успіх", "Запис додано до таблиці!")
          add_ntha.destroy()
          tree_tha.delete(*tree_tha.get_children())
          cur.execute('SELECT * FROM thematic_areas')
          rows = cur.fetchall()
          for row in rows:
              tree_tha.insert('', 'end', values=row)
    add_ntha = Toplevel()
    add_ntha.title('Додавання')
    add_ntha.iconbitmap('add.ico')
    add_ntha.geometry("350x120")
    add_ntha.resizable(FALSE, FALSE)
    p1 = ttk.Frame(add_ntha)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    l1 = Label(p1, text="Id-тематичного напрямку:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(p1, text="Тематичний напрямок англійською:").grid(row = 1, column = 0, sticky = W, pady = 2)
    l3 = Label(p1, text="Тематичний напрямок українською:").grid(row = 2, column = 0, sticky = W, pady = 2)
    e1 = Entry(p1, textvariable = id_var).grid(row = 0, column = 1, pady = 2)
    e2 = Entry(p1, textvariable = eng_var).grid(row = 1, column = 1, pady = 2)
    e3 = Entry(p1, textvariable = ukr_var).grid(row = 2, column = 1, pady = 2)
    b1 = Button(p1, text="Додати запис", command=a)
    b1.grid(row=6, column=1, pady=10)

def cdel_tha():
    id_var = IntVar()
    eng_var = StringVar()
    ukr_var = StringVar()
    del_tha = Toplevel()
    del_tha.title('Видалення')
    del_tha.iconbitmap('delete.ico')
    del_tha.geometry("320x210")
    del_tha.resizable(FALSE, FALSE)
    p1 = ttk.Frame(del_tha)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        if var.get() == 1:  
           id = id_var.get()
           cur.execute("SELECT IdThematicArea FROM thematic_areas WHERE IdThematicArea=?", (id,))
           if cur.fetchone() is None:
             messagebox.showerror("Помилка", "Запису з таким ID неіснує!")
           else:
             cur.execute("DELETE FROM reviewer_thematicareas WHERE IdThematicArea=?", (id,))
             cur.execute("DELETE FROM thematic_areas WHERE IdThematicArea=?", (id,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_tha.destroy()
             tree_tha.delete(*tree_tha.get_children())
             cur.execute('SELECT * FROM thematic_areas')
             rows = cur.fetchall()
             for row in rows:
                tree_tha.insert('', 'end', values=row)
        elif var.get() == 2:  
           eng = eng_var.get()
           cur.execute("SELECT IdThematicArea FROM thematic_areas WHERE ThematicAreaEng=?", (eng,))
           rows = cur.fetchall()
           if not rows:
              messagebox.showerror("Помилка", "Записів з таким ключовим словом англійською не існує!")
           else:
              id_list = [row[0] for row in rows]
              for id in id_list:
                 cur.execute("DELETE FROM reviewer_thematicareas WHERE IdThematicArea=?", (id,))
              cur.execute("DELETE FROM thematic_areas WHERE ThematicAreaEng=?", (eng,))
              con.commit()
              messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
              del_tha.destroy()
              tree_tha.delete(*tree_tha.get_children())
              cur.execute('SELECT * FROM thematic_areas')
              rows = cur.fetchall()
              for row in rows:
                 tree_tha.insert('', 'end', values=row)
        elif var.get() == 3:  
           ukr = ukr_var.get()
           cur.execute("SELECT IdThematicArea FROM thematic_areas WHERE ThematicAreaUkr=?", (ukr,))
           rows = cur.fetchall()
           if not rows:
             messagebox.showerror("Помилка", "Запису з таким ключовим словом українською неіснує!")
           else:
             id_list = [row[0] for row in rows]
             for id in id_list:
               cur.execute("DELETE FROM reviewer_thematicareas WHERE IdThematicArea=?", (id,))
             cur.execute("DELETE FROM thematic_areas WHERE ThematicAreaUkr=?", (ukr,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_tha.destroy()
             tree_tha.delete(*tree_tha.get_children())
             cur.execute('SELECT * FROM thematic_areas')
             rows = cur.fetchall()
             for row in rows:
                tree_tha.insert('', 'end', values=row)
    def enabl_1():
        for child in f1.winfo_children():
           child.configure(state='normal')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='normal')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    var1 = IntVar()
    id_del = ttk.Radiobutton(p1, text="Видалення за Id", variable=var, value=1, command=enabl_1).grid(row=0, column=0, sticky=W, pady=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, sticky=W, pady=2)
    title_del = ttk.Radiobutton(p1, text="Видалення за тематичним напрямком англійською", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    date_del = ttk.Radiobutton(p1, text="Видалення за тематичним напрямком українською", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2)
    f3 = ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id ключового слова:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть напрямок англійською:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Введіть напрямок українською:")
    l3.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =32)
    e2 = Entry(f2, textvariable = eng_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =13)
    e3 = Entry(f3, textvariable = ukr_var)
    e3.grid(row = 0, column = 1, pady = 2, padx =9)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Видалити запис", command=a)
    b1.grid(row=6, column=0, pady=10, padx = 150)
#
def cadd_rev():
    id_var = IntVar()
    idar_var = IntVar()
    nov_var = IntVar()
    top_var = IntVar()
    cl_var = IntVar()
    cp_var = IntVar()
    qal_var = IntVar()
    concl_var = StringVar()
    rem_var = StringVar()
    revr_list = StringVar()
    def a():
        id = id_var.get()
        idar = idar_var.get()
        nov = nov_var.get()
        top = top_var.get()
        cl = cl_var.get()
        cp = cp_var.get()
        qal = qal_var.get()
        concl = concl_var.get()
        rem = rem_var.get() 
        cur.execute("SELECT IdReview FROM review WHERE IdReview=?", (id,))
        if cur.fetchone() is not None:
            messagebox.showerror("Помилка", "Запис з таким ID вже існує!")
        else:
          cur.execute("SELECT IdArticle FROM article WHERE IdArticle=?", (idar,))
          if cur.fetchone() is None:
              messagebox.showerror("Помилка", "Не існує статті з таким ID!")
          else:
             cur.execute("INSERT INTO review (IdReview, IdArticle, MarkNovelty, MarkTopicality, MarkCompletnessL, MarkCompletnessP, MarkQuality, Conclusion, Remarks) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, idar, nov, top, cl, cp, qal, concl, rem))
             con.commit()
             selected_index = list_revr.curselection()
             if len(selected_index) != 0:
                revr = list_revr.get(selected_index[0])
                cur.execute("SELECT IdReviewer FROM reviewer WHERE Surname || ' ' || Name || ' ' || MiddleName = ?", (revr,))
                revrr_id = cur.fetchone()[0]
                cur.execute("INSERT INTO review_reviewer (IdReview, IdReviewer) VALUES (?, ?)", (id, revrr_id))
                con.commit()
             messagebox.showinfo("Успіх", "Запис додано до таблиці!")
             add_nrev.destroy()
             tree_rev.delete(*tree_rev.get_children())
             cur.execute('SELECT * FROM review')
             rows = cur.fetchall()
             for row in rows:
                 tree_rev.insert('', 'end', values=row)
    add_nrev = Toplevel()
    add_nrev.title('Додавання')
    add_nrev.iconbitmap('add.ico')
    add_nrev.geometry("320x340")
    add_nrev.resizable(FALSE, FALSE)
    p1 = ttk.Frame(add_nrev)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    l1 = Label(p1, text="Id-рецензії:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(p1, text="Id-статті:").grid(row = 1, column = 0, sticky = W, pady = 2)
    l3 = Label(p1, text="Новизна:").grid(row = 2, column = 0, sticky = W, pady = 2)
    l4 = Label(p1, text="Актуальність:").grid(row = 3, column = 0, sticky = W, pady = 2)
    l5 = Label(p1, text="Повнота літературного огляду:").grid(row = 4, column = 0, sticky = W, pady = 2)
    l6 = Label(p1, text="Повнота викладення:").grid(row = 5, column = 0, sticky = W, pady = 2)
    l7 = Label(p1, text="Наукова якість:").grid(row = 6, column = 0, sticky = W, pady = 2)
    l8 = Label(p1, text="Висновок:").grid(row = 7, column = 0, sticky = W, pady = 2)
    l9 = Label(p1, text="Зауваження:").grid(row = 8, column = 0, sticky = W, pady = 2)
    l10 = Label(p1, text="Оберіть рецензента:").grid(row = 9, column = 0, sticky = W, pady = 2)
    e1 = Entry(p1, textvariable = id_var).grid(row = 0, column = 1, pady = 2)
    e2 = Entry(p1, textvariable = idar_var).grid(row = 1, column = 1, pady = 2)
    e3 = Entry(p1, textvariable = nov_var).grid(row = 2, column = 1, pady = 2)
    e4 = Entry(p1, textvariable = top_var).grid(row = 3, column = 1, pady = 2)
    e5 = Entry(p1, textvariable = cl_var).grid(row = 4, column = 1, pady = 2)
    e6 = Entry(p1, textvariable = cp_var).grid(row = 5, column = 1, pady = 2)
    e7 = Entry(p1, textvariable = qal_var).grid(row = 6, column = 1, pady = 2)
    e8 = Entry(p1, textvariable = concl_var).grid(row = 7, column = 1, pady = 2)
    e9 = Entry(p1, textvariable = rem_var).grid(row = 8, column = 1, pady = 2)

    revr_values = [tree_revr.item(child)["values"][2] + " " + tree_revr.item(child)["values"][1] + " " + tree_revr.item(child)["values"][3] for child in tree_revr.get_children()]
    revr_values_sorted = sorted(revr_values)
    revr_list.set(revr_values_sorted)
    list_revr = Listbox(p1, listvariable=revr_list, selectmode=SINGLE, width=20, height=2)
    list_revr.grid(row = 9, column = 1, pady = 2)

    vscrollbar = ttk.Scrollbar(p1, orient=VERTICAL, command=list_revr.yview)
    list_revr.configure(yscroll=vscrollbar.set)
    vscrollbar.grid(row=9, column=2, sticky='ns')

    hscrollbar = ttk.Scrollbar(p1, orient= HORIZONTAL, command=list_revr.xview)
    list_revr.configure(xscroll=hscrollbar.set)
    hscrollbar.grid(row=10, column=1, sticky='ew')

    b1 = Button(p1, text="Додати запис", command=a)
    b1.grid(row=11, column=1, pady=10)
#
def cadd_kw():
    id_var = IntVar()
    eng_var = StringVar()
    ukr_var = StringVar()
    def a():        
        id = id_var.get()
        eng = eng_var.get()
        ukr = ukr_var.get()
        cur.execute("SELECT IdKeyWord FROM key_words WHERE IdKeyWord=?", (id,))
        if cur.fetchone() is not None:
            messagebox.showerror("Помилка", "Запис з таким ID вже існує!")
        else:
          cur.execute("INSERT INTO key_words (IdKeyWord, KeyWordEng, KeyWordUkr) VALUES (?, ?, ?)", (id, eng, ukr))
          con.commit()
          messagebox.showinfo("Успіх", "Запис додано до таблиці!")
          add_nkw.destroy()
          tree_kw.delete(*tree_kw.get_children())
          cur.execute('SELECT * FROM key_words')
          rows = cur.fetchall()
          for row in rows:
              tree_kw.insert('', 'end', values=row)
    add_nkw = Toplevel()
    add_nkw.title('Додавання')
    add_nkw.iconbitmap('add.ico')
    add_nkw.geometry("310x120")
    add_nkw.resizable(FALSE, FALSE)
    p1 = ttk.Frame(add_nkw)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    l1 = Label(p1, text="Id-ключового слова:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(p1, text="Ключове слово англійською:").grid(row = 1, column = 0, sticky = W, pady = 2)
    l3 = Label(p1, text="Ключове слово українською:").grid(row = 2, column = 0, sticky = W, pady = 2)
    e1 = Entry(p1, textvariable = id_var).grid(row = 0, column = 1, pady = 2)
    e2 = Entry(p1, textvariable = eng_var).grid(row = 1, column = 1, pady = 2)
    e3 = Entry(p1, textvariable = ukr_var).grid(row = 2, column = 1, pady = 2)
    b1 = Button(p1, text="Додати запис", command=a)
    b1.grid(row=6, column=1, pady=10)

def cdel_kw():
    id_var = IntVar()
    eng_var = StringVar()
    ukr_var = StringVar()
    del_kw = Toplevel()
    del_kw.title('Видалення')
    del_kw.iconbitmap('delete.ico')
    del_kw.geometry("300x210")
    del_kw.resizable(FALSE, FALSE)
    p1 = ttk.Frame(del_kw)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        if var.get() == 1:  
           id = id_var.get()
           cur.execute("SELECT IdKeyWord FROM key_words WHERE IdKeyWord=?", (id,))
           if cur.fetchone() is None:
             messagebox.showerror("Помилка", "Запису з таким ID неіснує!")
           else:
             cur.execute("DELETE FROM article_keywords WHERE IdKeyWord=?", (id,))
             cur.execute("DELETE FROM key_words WHERE IdKeyWord=?", (id,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_kw.destroy()
             tree_kw.delete(*tree_kw.get_children())
             cur.execute('SELECT * FROM key_words')
             rows = cur.fetchall()
             for row in rows:
                tree_kw.insert('', 'end', values=row)
        elif var.get() == 2:  
           eng = eng_var.get()
           cur.execute("SELECT IdKeyWord FROM key_words WHERE KeyWordEng=?", (eng,))
           rows = cur.fetchall()
           if not rows:
              messagebox.showerror("Помилка", "Записів з таким ключовим словом англійською не існує!")
           else:
              id_list = [row[0] for row in rows]
              for id in id_list:
                 cur.execute("DELETE FROM article_keywords WHERE IdKeyWord=?", (id,))
              cur.execute("DELETE FROM key_words WHERE KeyWordEng=?", (eng,))
              con.commit()
              messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
              del_kw.destroy()
              tree_kw.delete(*tree_kw.get_children())
              cur.execute('SELECT * FROM key_words')
              rows = cur.fetchall()
              for row in rows:
                 tree_kw.insert('', 'end', values=row)
        elif var.get() == 3:  
           ukr = ukr_var.get()
           cur.execute("SELECT IdKeyWord FROM key_words WHERE KeyWordUkr=?", (ukr,))
           rows = cur.fetchall()
           if not rows:
             messagebox.showerror("Помилка", "Запису з таким ключовим словом українською неіснує!")
           else:
             id_list = [row[0] for row in rows]
             for id in id_list:
               cur.execute("DELETE FROM article_keywords WHERE IdKeyWord=?", (id,))
             cur.execute("DELETE FROM key_words WHERE KeyWordUkr=?", (ukr,))
             con.commit()
             messagebox.showinfo("Успіх", "Запис видалено з таблиці!")
             del_kw.destroy()
             tree_kw.delete(*tree_kw.get_children())
             cur.execute('SELECT * FROM key_words')
             rows = cur.fetchall()
             for row in rows:
                tree_kw.insert('', 'end', values=row)
    def enabl_1():
        for child in f1.winfo_children():
           child.configure(state='normal')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='normal')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    var1 = IntVar()
    id_del = ttk.Radiobutton(p1, text="Видалення за Id", variable=var, value=1, command=enabl_1).grid(row=0, column=0, sticky=W, pady=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, sticky=W, pady=2)
    title_del = ttk.Radiobutton(p1, text="Видалення за ключовим словом англійською", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    date_del = ttk.Radiobutton(p1, text="Видалення за ключовим словом українською", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2)
    f3 = ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id ключового слова:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть слово англійською:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Введіть слово українською:")
    l3.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =12)
    e2 = Entry(f2, textvariable = eng_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =13)
    e3 = Entry(f3, textvariable = ukr_var)
    e3.grid(row = 0, column = 1, pady = 2, padx =10)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Видалити запис", command=a)
    b1.grid(row=6, column=0, pady=10, padx = 150)
##
def csort_au():
    sort_au = Toplevel()
    sort_au.title('Сортування')
    sort_au.iconbitmap('sort.ico')
    sort_au.geometry("200x300")
    sort_au.resizable(FALSE, FALSE)
    p1 = ttk.Frame(sort_au)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        sort_au.destroy()
        tree_au.delete(*tree_au.get_children())
        if var.get() == 1:
           if var1.get() == 1:
               cursor = db.aql.execute('FOR doc IN author SORT TO_NUMBER(doc._key) ASC RETURN doc')
           elif var1.get() == 2:
               cursor = db.aql.execute('FOR doc IN author SORT TO_NUMBER(doc._key) DESC RETURN doc')
        elif var.get() == 2:
           if var1.get() == 1:
               cursor = db.aql.execute('FOR doc IN author SORT doc.Name ASC RETURN doc')
           elif var1.get() == 2:
               cursor = db.aql.execute('FOR doc IN author SORT doc.Name DESC RETURN doc')
        elif var.get() == 3:
           if var1.get() == 1:
               cursor = db.aql.execute('FOR doc IN author SORT doc.Surname ASC RETURN doc')
           elif var1.get() == 2:
               cursor = db.aql.execute('FOR doc IN author SORT doc.Surname DESC RETURN doc')
        elif var.get() == 4:
           if var1.get() == 1:
               cursor = db.aql.execute('FOR doc IN author SORT doc.MiddleName ASC RETURN doc')
           elif var1.get() == 2:
               cursor = db.aql.execute('FOR doc IN author SORT doc.MiddleName DESC RETURN doc')
        elif var.get() == 5:
           if var1.get() == 1:
               cursor = db.aql.execute('FOR doc IN author SORT doc.PhoneNumber ASC RETURN doc')
           elif var1.get() == 2:
               cursor = db.aql.execute('FOR doc IN author SORT doc.PhoneNumber DESC RETURN doc')
        elif var.get() == 6:
           if var1.get() == 1:
               cursor = db.aql.execute('FOR doc IN author SORT doc.Email ASC RETURN doc')
           elif var1.get() == 2:
               cursor = db.aql.execute('FOR doc IN author SORT doc.Email DESC RETURN doc')
        for doc in cursor:
           values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['PhoneNumber'], doc['Email'])
           tree_au.insert('', 'end', None, values=values)
    var = IntVar()
    var1 = IntVar()    
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=0, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Оберіть поле за яким сортувати:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    sid = ttk.Radiobutton(f1, text="Id-автора", variable=var, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    sn = ttk.Radiobutton(f1, text="Ім`я", variable=var, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    ssn = ttk.Radiobutton(f1, text="Прізвище", variable=var, value=3).grid(row=3, column=0, sticky=W, pady=2, padx=2)
    smn = ttk.Radiobutton(f1, text="По батькові", variable=var, value=4).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    sph = ttk.Radiobutton(f1, text="Номер телефону", variable=var, value=5).grid(row=5, column=0, sticky=W, pady=2, padx=2)
    se = ttk.Radiobutton(f1, text="Email", variable=var, value=6).grid(row=6, column=0, sticky=W, pady=2, padx=2)
    f2 = ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=1, column=0, sticky=W, pady=2)
    l2 = Label(f2, text="Оберіть варіант сортування:        ")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    asc = ttk.Radiobutton(f2, text="За зростанням", variable=var1, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    desc = ttk.Radiobutton(f2, text="За спаданням", variable=var1, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    b1 = Button(p1, text="Сортувати", command=a)
    b1.grid(row=3, column=0, pady=5, padx = 100)

def csort_ar():
    sort_ar = Toplevel()
    sort_ar.title('Сортування')
    sort_ar.iconbitmap('sort.ico')
    sort_ar.geometry("190x245")
    sort_ar.resizable(FALSE, FALSE)
    p1 = ttk.Frame(sort_ar)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        sort_ar.destroy()
        tree_ar.delete(*tree_ar.get_children())
        if var.get() == 1:
           if var1.get() == 1:
               cur.execute('SELECT * FROM article ORDER BY IdArticle ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM article ORDER BY IdArticle DESC')
        elif var.get() == 2:
           if var1.get() == 1:
               cur.execute('SELECT * FROM article ORDER BY Title ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM article ORDER BY Title DESC')
        elif var.get() == 3:
           if var1.get() == 1:
               cur.execute('SELECT * FROM article ORDER BY Date ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM article ORDER BY Date DESC')
        elif var.get() == 4:
           if var1.get() == 1:
               cur.execute('SELECT * FROM article ORDER BY FileLink ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM article ORDER BY FileLink DESC')
        rows = cur.fetchall()
        for row in rows:
            tree_ar.insert('', 'end', values=row)
    var = IntVar()
    var1 = IntVar()    
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=0, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Оберіть поле за яким сортувати:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    sid = ttk.Radiobutton(f1, text="Id-статті", variable=var, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    st = ttk.Radiobutton(f1, text="Заголовок", variable=var, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    sd = ttk.Radiobutton(f1, text="Дата", variable=var, value=3).grid(row=3, column=0, sticky=W, pady=2, padx=2)
    sfl = ttk.Radiobutton(f1, text="Посилання", variable=var, value=4).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    f2 = ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=1, column=0, sticky=W, pady=2)
    l2 = Label(f2, text="Оберіть варіант сортування:        ")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    asc = ttk.Radiobutton(f2, text="За зростанням", variable=var1, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    desc = ttk.Radiobutton(f2, text="За спаданням", variable=var1, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    b1 = Button(p1, text="Сортувати", command=a)
    b1.grid(row=3, column=0, pady=5, padx = 100)

def csort_ann():
    sort_ann = Toplevel()
    sort_ann.title('Сортування')
    sort_ann.iconbitmap('sort.ico')
    sort_ann.geometry("200x250")
    sort_ann.resizable(FALSE, FALSE)
    p1 = ttk.Frame(sort_ann)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        sort_ann.destroy()
        tree_ann.delete(*tree_ann.get_children())
        if var.get() == 1:
           if var1.get() == 1:
               cur.execute('SELECT * FROM annotation ORDER BY IdAnnotation ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM annotation ORDER BY IdAnnotation DESC')
        elif var.get() == 2:
           if var1.get() == 1:
               cur.execute('SELECT * FROM annotation ORDER BY IdArticle ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM annotation ORDER BY IdArticle DESC')
        elif var.get() == 3:
           if var1.get() == 1:
               cur.execute('SELECT * FROM annotation ORDER BY Language ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM annotation ORDER BY Language DESC')
        elif var.get() == 4:
           if var1.get() == 1:
               cur.execute('SELECT * FROM annotation ORDER BY AnnotationText ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM annotation ORDER BY AnnotationText DESC')
        rows = cur.fetchall()
        for row in rows:
            tree_ann.insert('', 'end', values=row)
    var = IntVar()
    var1 = IntVar()    
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=0, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Оберіть поле за яким сортувати:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    sid = ttk.Radiobutton(f1, text="Id-анотації", variable=var, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    sn = ttk.Radiobutton(f1, text="Id-статті", variable=var, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    ssn = ttk.Radiobutton(f1, text="Мова", variable=var, value=3).grid(row=3, column=0, sticky=W, pady=2, padx=2)
    smn = ttk.Radiobutton(f1, text="Текст анотації", variable=var, value=4).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    f2 = ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=1, column=0, sticky=W, pady=2)
    l2 = Label(f2, text="Оберіть варіант сортування:        ")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    asc = ttk.Radiobutton(f2, text="За зростанням", variable=var1, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    desc = ttk.Radiobutton(f2, text="За спаданням", variable=var1, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    b1 = Button(p1, text="Сортувати", command=a)
    b1.grid(row=3, column=0, pady=5, padx = 100)

def csort_kw():
    sort_kw = Toplevel()
    sort_kw.title('Сортування')
    sort_kw.iconbitmap('sort.ico')
    sort_kw.geometry("200x220")
    sort_kw.resizable(FALSE, FALSE)
    p1 = ttk.Frame(sort_kw)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        sort_kw.destroy()
        tree_kw.delete(*tree_kw.get_children())
        if var.get() == 1:
           if var1.get() == 1:
               cur.execute('SELECT * FROM key_words ORDER BY IdKeyWord ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM key_words ORDER BY IdKeyWord DESC')
        elif var.get() == 2:
           if var1.get() == 1:
               cur.execute('SELECT * FROM key_words ORDER BY KeyWordEng ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM key_words ORDER BY KeyWordEng DESC')
        elif var.get() == 3:
           if var1.get() == 1:
               cur.execute('SELECT * FROM key_words ORDER BY KeyWordUkr ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM key_words ORDER BY KeyWordUkr DESC')
        rows = cur.fetchall()
        for row in rows:
            tree_kw.insert('', 'end', values=row)
    var = IntVar()
    var1 = IntVar()    
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=0, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Оберіть поле за яким сортувати:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    sid = ttk.Radiobutton(f1, text="Id-ключового слова", variable=var, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    sn = ttk.Radiobutton(f1, text="Ключове слово англійською", variable=var, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    ssn = ttk.Radiobutton(f1, text="Ключове слово українською", variable=var, value=3).grid(row=3, column=0, sticky=W, pady=2, padx=2)
    f2 = ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=1, column=0, sticky=W, pady=2)
    l2 = Label(f2, text="Оберіть варіант сортування:        ")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    asc = ttk.Radiobutton(f2, text="За зростанням", variable=var1, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    desc = ttk.Radiobutton(f2, text="За спаданням", variable=var1, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    b1 = Button(p1, text="Сортувати", command=a)
    b1.grid(row=3, column=0, pady=5, padx = 100)

def csort_revr():
    sort_revr = Toplevel()
    sort_revr.title('Сортування')
    sort_revr.iconbitmap('sort.ico')
    sort_revr.geometry("200x270")
    sort_revr.resizable(FALSE, FALSE)
    p1 = ttk.Frame(sort_revr)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        sort_revr.destroy()
        tree_revr.delete(*tree_revr.get_children())
        if var.get() == 1:
           if var1.get() == 1:
               cur.execute('SELECT * FROM reviewer ORDER BY IdReviewer ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM reviewer ORDER BY IdReviewer DESC')
        elif var.get() == 2:
           if var1.get() == 1:
               cur.execute('SELECT * FROM reviewer ORDER BY Name ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM reviewer ORDER BY Name DESC')
        elif var.get() == 3:
           if var1.get() == 1:
               cur.execute('SELECT * FROM reviewer ORDER BY Surname ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM reviewer ORDER BY Surname DESC')
        elif var.get() == 4:
           if var1.get() == 1:
               cur.execute('SELECT * FROM reviewer ORDER BY MiddleName ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM reviewer ORDER BY MiddleName DESC')
        elif var.get() == 5:
           if var1.get() == 1:
               cur.execute('SELECT * FROM reviewer ORDER BY Email ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM reviewer ORDER BY Email DESC')
        rows = cur.fetchall()
        for row in rows:
            tree_revr.insert('', 'end', values=row)
    var = IntVar()
    var1 = IntVar()    
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=0, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Оберіть поле за яким сортувати:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    sid = ttk.Radiobutton(f1, text="Id-рецензенту", variable=var, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    sn = ttk.Radiobutton(f1, text="Ім`я", variable=var, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    ssn = ttk.Radiobutton(f1, text="Прізвище", variable=var, value=3).grid(row=3, column=0, sticky=W, pady=2, padx=2)
    smn = ttk.Radiobutton(f1, text="По батькові", variable=var, value=4).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    sph = ttk.Radiobutton(f1, text="Email", variable=var, value=5).grid(row=5, column=0, sticky=W, pady=2, padx=2)
    f2 = ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=1, column=0, sticky=W, pady=2)
    l2 = Label(f2, text="Оберіть варіант сортування:        ")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    asc = ttk.Radiobutton(f2, text="За зростанням", variable=var1, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    desc = ttk.Radiobutton(f2, text="За спаданням", variable=var1, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    b1 = Button(p1, text="Сортувати", command=a)
    b1.grid(row=3, column=0, pady=5, padx = 100)

def csort_rev():
    sort_rev = Toplevel()
    sort_rev.title('Сортування')
    sort_rev.iconbitmap('sort.ico')
    sort_rev.geometry("240x370")
    sort_rev.resizable(FALSE, FALSE)
    p1 = ttk.Frame(sort_rev)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        sort_rev.destroy()
        tree_rev.delete(*tree_rev.get_children())
        if var.get() == 1:
           if var1.get() == 1:
               cur.execute('SELECT * FROM review ORDER BY IdReview ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM review ORDER BY IdReview DESC')
        elif var.get() == 2:
           if var1.get() == 1:
               cur.execute('SELECT * FROM review ORDER BY IdArticle ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM review ORDER BY IdArticle DESC')
        elif var.get() == 3:
           if var1.get() == 1:
               cur.execute('SELECT * FROM review ORDER BY MarkNovelty ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM review ORDER BY MarkNovelty DESC')
        elif var.get() == 4:
           if var1.get() == 1:
               cur.execute('SELECT * FROM review ORDER BY MarkTopicality ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM review ORDER BY MarkTopicality DESC')
        elif var.get() == 5:
           if var1.get() == 1:
               cur.execute('SELECT * FROM review ORDER BY MarkCompletnessL ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM review ORDER BY MarkCompletnessL DESC')
        elif var.get() == 6:
           if var1.get() == 1:
               cur.execute('SELECT * FROM review ORDER BY MarkCompletnessP ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM review ORDER BY MarkCompletnessP DESC')
        elif var.get() == 7:
           if var1.get() == 1:
               cur.execute('SELECT * FROM review ORDER BY MarkCompletnessP ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM review ORDER BY MarkCompletnessP DESC')
        elif var.get() == 8:
           if var1.get() == 1:
               cur.execute('SELECT * FROM review ORDER BY Conclusion ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM review ORDER BY Conclusion DESC')
        elif var.get() == 9:
           if var1.get() == 1:
               cur.execute('SELECT * FROM review ORDER BY Remarks ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM review ORDER BY Remarks DESC')
        rows = cur.fetchall()
        for row in rows:
            tree_rev.insert('', 'end', values=row)
    var = IntVar()
    var1 = IntVar()    
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=0, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Оберіть поле за яким сортувати:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    s1 = ttk.Radiobutton(f1, text="Id-рецензії", variable=var, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    s2 = ttk.Radiobutton(f1, text="Id-статті", variable=var, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    s3 = ttk.Radiobutton(f1, text="Оцінка новизни", variable=var, value=3).grid(row=3, column=0, sticky=W, pady=2, padx=2)
    s4 = ttk.Radiobutton(f1, text="Оцінка актуальності", variable=var, value=4).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    s5 = ttk.Radiobutton(f1, text="Оцінка повноти літературного огляду", variable=var, value=5).grid(row=5, column=0, sticky=W, pady=2, padx=2)
    s6 = ttk.Radiobutton(f1, text="Оцінка повноти викладення", variable=var, value=6).grid(row=6, column=0, sticky=W, pady=2, padx=2)
    s7 = ttk.Radiobutton(f1, text="Оцінка наукової якості", variable=var, value=7).grid(row=7, column=0, sticky=W, pady=2, padx=2)
    s8 = ttk.Radiobutton(f1, text="Висновок", variable=var, value=8).grid(row=8, column=0, sticky=W, pady=2, padx=2)
    s9 = ttk.Radiobutton(f1, text="Зауваження", variable=var, value=9).grid(row=9, column=0, sticky=W, pady=2, padx=2)
    f2 = ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=1, column=0, sticky=W, pady=2)
    l2 = Label(f2, text="Оберіть варіант сортування:                       ")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    asc = ttk.Radiobutton(f2, text="За зростанням", variable=var1, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    desc = ttk.Radiobutton(f2, text="За спаданням", variable=var1, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    b1 = Button(p1, text="Сортувати", command=a)
    b1.grid(row=3, column=0, pady=5, padx = 100)

def csort_tha():
    sort_tha = Toplevel()
    sort_tha.title('Сортування')
    sort_tha.iconbitmap('sort.ico')
    sort_tha.geometry("230x220")
    sort_tha.resizable(FALSE, FALSE)
    p1 = ttk.Frame(sort_tha)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        sort_tha.destroy()
        tree_tha.delete(*tree_tha.get_children())
        if var.get() == 1:
           if var1.get() == 1:
               cur.execute('SELECT * FROM thematic_areas ORDER BY IdThematicArea ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM thematic_areas ORDER BY IdThematicArea DESC')
        elif var.get() == 2:
           if var1.get() == 1:
               cur.execute('SELECT * FROM thematic_areas ORDER BY ThematicAreaEng ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM thematic_areas ORDER BY ThematicAreaEng DESC')
        elif var.get() == 3:
           if var1.get() == 1:
               cur.execute('SELECT * FROM thematic_areas ORDER BY ThematicAreaUkr ASC')
           elif var1.get() == 2:
               cur.execute('SELECT * FROM thematic_areas ORDER BY ThematicAreaUkr DESC')
        rows = cur.fetchall()
        for row in rows:
            tree_tha.insert('', 'end', values=row)
    var = IntVar()
    var1 = IntVar()    
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=0, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Оберіть поле за яким сортувати:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    sid = ttk.Radiobutton(f1, text="Id-тематичного напрямку", variable=var, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    sn = ttk.Radiobutton(f1, text="Тематичний напрямок англійською", variable=var, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    ssn = ttk.Radiobutton(f1, text="Тематичний напрямок українською", variable=var, value=3).grid(row=3, column=0, sticky=W, pady=2, padx=2)
    f2 = ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=1, column=0, sticky=W, pady=2)
    l2 = Label(f2, text="Оберіть варіант сортування:                  ")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2, padx=2)
    asc = ttk.Radiobutton(f2, text="За зростанням", variable=var1, value=1).grid(row=1, column=0, sticky=W, pady=2, padx=2)
    desc = ttk.Radiobutton(f2, text="За спаданням", variable=var1, value=2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    b1 = Button(p1, text="Сортувати", command=a)
    b1.grid(row=3, column=0, pady=5, padx = 100)
####
def csearch_au():
    id_var = StringVar()
    phn_var = StringVar()
    e_var = StringVar()
    s_var = StringVar()
    search_au = Toplevel()
    var=IntVar()
    search_au.title('Пошук')
    search_au.iconbitmap('search.ico')
    search_au.geometry("270x255")
    search_au.resizable(FALSE, FALSE)
    p1 = ttk.Frame(search_au)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        table=Toplevel()
        table.title('Результат')
        tree = ttk.Treeview(table, columns=col_au, show='headings')
        tree.heading('id_auth', text='Id-автора')
        tree.heading('name', text='Ім`я')
        tree.heading('surname', text='Прізвище')
        tree.heading('middle_name', text='По батькові')
        tree.heading('phone_num', text='Номер телефону')
        tree.heading('email', text='Email')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        if var.get() == 1:  
           id = id_var.get()
           query = 'FOR doc IN author FILTER doc._key == @id RETURN doc'
           cursor = db.aql.execute(query, bind_vars={'id': id})
           results = list(cursor)
           if len(results) == 0:
              messagebox.showerror("Помилка", "Записів з таким ID неіснує!")
           else:
              for doc in results:
                 values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['PhoneNumber'], doc['Email'])
                 tree.insert('', 'end', None, values=values)
        elif var.get() == 2:  
           phn = phn_var.get()
           query = 'FOR doc IN author FILTER doc.PhoneNumber == @phn RETURN doc'
           cursor = db.aql.execute(query, bind_vars={'phn': phn})
           results = list(cursor)
           if len(results) == 0:
               messagebox.showerror("Помилка", "Записів з таким номером телефону неіснує!")
           else:
              for doc in results:
                 values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['PhoneNumber'], doc['Email'])
                 tree.insert('', 'end', None, values=values)
        elif var.get() == 3:  
           e = e_var.get()
           query = 'FOR doc IN author FILTER doc.Email == @e RETURN doc'
           cursor = db.aql.execute(query, bind_vars={'e': e})
           results = list(cursor)
           if len(results) == 0:
               messagebox.showerror("Помилка", "Записів з таким Email неіснує!")
           else:
              for doc in results:
                 values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['PhoneNumber'], doc['Email'])
                 tree.insert('', 'end', None, values=values)
        elif var.get() == 4:
            s = s_var.get()
            query = 'FOR doc IN author FILTER doc.Surname == @s RETURN doc'
            cursor = db.aql.execute(query, bind_vars={'s': s})
            results = list(cursor)
            if len(results) == 0:
               messagebox.showerror("Помилка", "Записів з таким Прізвищем неіснує!")
            else:
               for doc in results:
                 values = (doc['_key'], doc['Name'], doc['Surname'], doc['MiddleName'], doc['PhoneNumber'], doc['Email'])
                 tree.insert('', 'end', None, values=values)
    def enabl_1():
        for child in f1.winfo_children():
           child.configure(state='normal')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
        for child in f4.winfo_children():
           child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='normal')
        for child in f3.winfo_children():
           child.configure(state='disabled')
        for child in f4.winfo_children():
           child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='normal')
        for child in f4.winfo_children():
           child.configure(state='disabled')
    def enabl_4():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
        for child in f4.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    id= ttk.Radiobutton(p1, text="Пошук за Id", variable=var, value=1, command=enabl_1).grid(row=0, column=0, sticky=W, pady=2, padx=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, sticky=W, pady=2)
    phone = ttk.Radiobutton(p1, text="Пошук за номером телефону", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    email = ttk.Radiobutton(p1, text="Пошук за Email", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    f3 = ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    surn = ttk.Radiobutton(p1, text="Пошук за прізвищем", variable=var, value=4, command=enabl_4).grid(row=6, column=0, sticky=W, pady=2, padx=2)
    f4 = ttk.Frame(p1, relief=GROOVE)
    f4.grid(row=7, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id-автора:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть номер телефону:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Введіть Email:")
    l3.grid(row = 0, column = 0, sticky = W, pady = 2)
    l4 = Label(f4, text="Введіть Прізвище:")
    l4.grid(row = 0, column = 0, sticky = W, pady = 2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =42)
    e2 = Entry(f2, textvariable = phn_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =2)
    e3 = Entry(f3, textvariable = e_var)
    e3.grid(row = 0, column = 1, pady = 2, padx = 65)
    e4 = Entry(f4, textvariable = s_var)
    e4.grid(row = 0, column = 1, pady = 2, padx = 42)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    for child in f4.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Знайти", command=a)
    b1.grid(row=8, column=0, pady=10, padx = 150)

def csearch_ar():
    id_var = IntVar()
    title_var = StringVar()
    date_var = StringVar()
    var1=IntVar()
    search_article = Toplevel()
    search_article.title('Пошук')
    search_article.iconbitmap('search.ico')
    search_article.geometry("235x255")
    search_article.resizable(FALSE, FALSE)
    p1 = ttk.Frame(search_article)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        table=Toplevel()
        table.title('Результат')
        tree = ttk.Treeview(table, columns=col_ar, show='headings')
        tree.heading('id_art', text='Id-статті')
        tree.heading('title', text='Заголовок')
        tree.heading('date', text='Дата')
        tree.heading('link', text='Посилання')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        if var.get() == 1:
            id_article = id_var.get()
            cur.execute("SELECT * FROM article WHERE IdArticle=?", (id_article,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Помилка", "Записів з таким Id неіснує!")
            else:
                for row in rows:
                    tree.insert("", "end", values=row)
        elif var.get() == 2:
            title = title_var.get()
            cur.execute("SELECT * FROM article WHERE Title=?", (title,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Помилка", "Записів з таким заголовком неіснує!")
            else:
                for row in rows:
                    tree.insert("", "end", values=row)
        elif var.get() == 3:
            date = date_var.get()
            if var1.get() == 1:
               cur.execute("SELECT * FROM article WHERE Date<?", (date,))
               rows = cur.fetchall()
               if not rows:
                  messagebox.showerror("Помилка", "Записів з такою датою неіснує!")
               else:
                  for row in rows:
                    tree.insert("", "end", values=row)
            elif var1.get() == 2:  
               cur.execute("SELECT * FROM article WHERE Date=?", (date,))
               rows = cur.fetchall()
               if not rows:
                  messagebox.showerror("Помилка", "Записів з такою датою неіснує!")
               else:
                  for row in rows:
                    tree.insert("", "end", values=row)
            elif var1.get() == 3:  
               cur.execute("SELECT * FROM article WHERE Date>?", (date,))
               rows = cur.fetchall()
               if not rows:
                  messagebox.showerror("Помилка", "Записів з такою датою неіснує!")
               else:
                  for row in rows:
                    tree.insert("", "end", values=row)            
    def enabl_1():
        for child in f1.winfo_children():
            child.configure(state='normal')
        for child in f2.winfo_children():
            child.configure(state='disabled')
        for child in f3.winfo_children():
            child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
            child.configure(state='disabled')
        for child in f2.winfo_children():
            child.configure(state='normal')
        for child in f3.winfo_children():
            child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
            child.configure(state='disabled')
        for child in f2.winfo_children():
            child.configure(state='disabled')
        for child in f3.winfo_children():
            child.configure(state='normal')
    var = IntVar()
    id_article_radio = ttk.Radiobutton(p1, text="Пошук за Id-статті", variable=var, value=1, command=enabl_1)
    id_article_radio.grid(row=0, column=0, sticky=W, pady=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, pady=2, sticky="nsew")
    phone = ttk.Radiobutton(p1, text="Пошук за Заголовком", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    email = ttk.Radiobutton(p1, text="Пошук за Датою", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    f3 = ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id-статті:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть заголовок:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Введіть дату:")
    l3.grid(row = 0, column = 0, sticky = W, pady = 2)
    les = ttk.Radiobutton(f3, text="<", variable=var1, value=1).grid(row=0, column=1, sticky=W, pady=2)
    eq = ttk.Radiobutton(f3, text="=", variable=var1, value=2).grid(row=1, column=1, sticky=W, pady=2)
    more = ttk.Radiobutton(f3, text=">", variable=var1, value=3).grid(row=2, column=1, sticky=W, pady=2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =10)
    e2 = Entry(f2, textvariable = title_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =2)
    e3 = Entry(f3, textvariable = date_var)
    e3.grid(row = 1, column = 2, pady = 2, padx =2)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Знайти", command=a)
    b1.grid(row=6, column=0, pady=10, padx = 150)

def csearch_ann():
    ann_var = IntVar()
    art_var = IntVar()
    search_ann = Toplevel()
    search_ann.title('Пошук')
    search_ann.iconbitmap('search.ico')
    search_ann.geometry("250x155")
    search_ann.resizable(FALSE, FALSE)
    p1 = ttk.Frame(search_ann)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        table=Toplevel()
        table.title('Результат')
        tree = ttk.Treeview(table, columns=col_ann, show='headings')
        tree.heading('id_ann', text='Id-анотації')
        tree.heading('id_ar', text='Id-статті')
        tree.heading('language', text='Мова')
        tree.heading('text', text='Текст')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        if var.get() == 1:  
            ann = ann_var.get()
            cur.execute("SELECT * FROM annotation WHERE IdAnnotation=?", (ann,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Помилка", "Записів з таким ID-анотації неіснує!")
            else:
                for row in rows:
                    tree.insert("", "end", values=row)
        elif var.get() == 2:  
            art = art_var.get()
            cur.execute("SELECT * FROM annotation WHERE IdArticle=?", (art,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Помилка", "Записів з таким ID-статті неіснує!")
            else:
                for row in rows:
                    tree.insert("", "end", values=row)
    def enabl_1():
        for child in f1.winfo_children():
            child.configure(state='normal')
        for child in f2.winfo_children():
            child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
            child.configure(state='disabled')
        for child in f2.winfo_children():
            child.configure(state='normal')
    var = IntVar()
    id_article_radio = ttk.Radiobutton(p1, text="Пошук за Id-анотації", variable=var, value=1, command=enabl_1)
    id_article_radio.grid(row=0, column=0, sticky=W, pady=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, pady=2, sticky="nsew")
    annot = ttk.Radiobutton(p1, text="Пошук за Id-статті", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id-анотації:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть Id-статті:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    e1 = Entry(f1, textvariable = ann_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =10)
    e2 = Entry(f2, textvariable = art_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =20)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Знайти", command=a)
    b1.grid(row=6, column=0, pady=10, padx = 150)

def csearch_kw():
    id_var = IntVar()
    kw_eng_var = StringVar()
    kw_ukr_var = StringVar()
    search_kw = Toplevel()
    search_kw.title('Пошук')
    search_kw.iconbitmap('search.ico')
    search_kw.geometry("336x210")
    search_kw.resizable(FALSE, FALSE)
    p1 = ttk.Frame(search_kw)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        table = Toplevel()
        table.title('Результат')
        tree = ttk.Treeview(table, columns=col_kw, show='headings')
        tree.heading('id_kw', text='Id-ключового слова')
        tree.heading('kw_eng', text='Ключове слово англійською')
        tree.heading('kw_ukr', text='Ключове слово українською')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        if var.get() == 1:
            id = id_var.get()
            cur.execute("SELECT * FROM key_words WHERE IdKeyWord=?", (id,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Помилка", "Записів з таким ID неіснує!")
            else:
                for row in rows:
                    tree.insert("", "end", values=row)
        elif var.get() == 2:
            kw_eng = kw_eng_var.get()
            cur.execute("SELECT * FROM key_words WHERE KeyWordEng=?", (kw_eng,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Помилка", "Записів з таким англійським ключовим словом неіснує!")
            else:
                for row in rows:
                    tree.insert("", "end", values=row)
        elif var.get() == 3:
            kw_ukr = kw_ukr_var.get()
            cur.execute("SELECT * FROM key_words WHERE KeyWordUkr=?", (kw_ukr,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Помилка", "Записів з таким українським ключовим словом неіснує!")
            else:
                for row in rows:
                    tree.insert("", "end", values=row)
    def enabl_1():
        for child in f1.winfo_children():
            child.configure(state='normal')
        for child in f2.winfo_children():
            child.configure(state='disabled')
        for child in f3.winfo_children():
            child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
            child.configure(state='disabled')
        for child in f2.winfo_children():
            child.configure(state='normal')
        for child in f3.winfo_children():
            child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    id_ = ttk.Radiobutton(p1, text="Пошук за Id-ключового слова", variable=var, value=1, command=enabl_1)
    id_.grid(row=0, column=0, sticky=W, pady=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, pady=2, sticky="nsew")
    eng = ttk.Radiobutton(p1, text="Пошук за ключовим словом англійською", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    ukr = ttk.Radiobutton(p1, text="Пошук за ключовим словом українською", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    f3 =  ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id-ключового слова:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть ключове слово англійською:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Введіть ключове слово українською:")
    l3.grid(row = 0, column = 0, sticky = W, pady = 2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =48)
    e2 = Entry(f2, textvariable = kw_eng_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =2)
    e3 = Entry(f3, textvariable = kw_ukr_var)
    e3.grid(row = 0, column = 1, pady = 2, padx =2)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Знайти", command=a)
    b1.grid(row=6, column=0, pady=10, padx = 200)

def csearch_revr():
    id_var = IntVar()
    s_var = StringVar()
    e_var = StringVar()
    search_revr = Toplevel()
    var=IntVar()
    search_revr.title('Пошук')
    search_revr.iconbitmap('search.ico')
    search_revr.geometry("255x210")
    search_revr.resizable(FALSE, FALSE)
    p1 = ttk.Frame(search_revr)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        table=Toplevel()
        table.title('Результат')
        tree = ttk.Treeview(table, columns=col_revr, show='headings')
        tree.heading('id_revr', text='Id-рецензенту')
        tree.heading('name', text='Ім`я')
        tree.heading('surname', text='Прізвище')
        tree.heading('middle_name', text='По батькові')
        tree.heading('email', text='Email')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        if var.get() == 1:  
           id = id_var.get()
           cur.execute("SELECT * FROM reviewer WHERE IdReviewer=?", (id,))
           rows = cur.fetchall()
           if not rows:
              messagebox.showerror("Помилка", "Записів з таким ID неіснує!")
           else:
              for row in rows:
                tree.insert("", "end", values=row)
        elif var.get() == 2:  
           s = s_var.get()
           cur.execute("SELECT * FROM reviewer WHERE Surname=?", (s,))
           rows = cur.fetchall()
           if not rows:
               messagebox.showerror("Помилка", "Записів з таким Прізвищем неіснує!")
           else:
               for row in rows:
                   tree.insert("", "end", values=row)
        elif var.get() == 3:  
           e = e_var.get()
           cur.execute("SELECT * FROM reviewer WHERE Email=?", (e,))
           rows = cur.fetchall()
           if not rows:
               messagebox.showerror("Помилка", "Записів з таким Email неіснує!")
           else:
               for row in rows:
                   tree.insert("", "end", values=row)
    def enabl_1():
        for child in f1.winfo_children():
           child.configure(state='normal')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='normal')
        for child in f3.winfo_children():
           child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    id= ttk.Radiobutton(p1, text="Пошук за Id", variable=var, value=1, command=enabl_1).grid(row=0, column=0, sticky=W, pady=2, padx=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, sticky=W, pady=2)
    phone = ttk.Radiobutton(p1, text="Пошук за Прізвищем", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    email = ttk.Radiobutton(p1, text="Пошук за Email", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    f3 = ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id-рецензенту:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть Прізвище:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Введіть Email:")
    l3.grid(row = 0, column = 0, sticky = W, pady = 2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =2)
    e2 = Entry(f2, textvariable = s_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =25)
    e3 = Entry(f3, textvariable = e_var)
    e3.grid(row = 0, column = 1, pady = 2, padx =49)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Знайти", command=a)
    b1.grid(row=6, column=0, pady=10, padx = 150)

def csearch_tha():
    id_var = IntVar()
    tha_eng_var = StringVar()
    tha_ukr_var = StringVar()
    search_tha = Toplevel()
    search_tha.title('Пошук')
    search_tha.iconbitmap('search.ico')
    search_tha.geometry("380x210")
    search_tha.resizable(FALSE, FALSE)
    p1 = ttk.Frame(search_tha)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        table = Toplevel()
        table.title('Результат')
        tree = ttk.Treeview(table, columns=col_tha, show='headings')
        tree.heading('id_tha', text='Id-тематичного напряму')
        tree.heading('tha_eng', text='Тематичний напрямок англійською')
        tree.heading('tha_ukr', text='Тематичний напрямок українською')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        if var.get() == 1:
            id = id_var.get()
            cur.execute("SELECT * FROM thematic_areas WHERE IdThematicArea=?", (id,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Помилка", "Записів з таким ID неіснує!")
            else:
                for row in rows:
                    tree.insert("", "end", values=row)
        elif var.get() == 2:
            tha_eng = tha_eng_var.get()
            cur.execute("SELECT * FROM thematic_areas WHERE ThematicAreaEng=?", (tha_eng,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Помилка", "Записів з таким тематичним напрямком англійською неіснує!")
            else:
                for row in rows:
                    tree.insert("", "end", values=row)
        elif var.get() == 3:
            tha_ukr = tha_ukr_var.get()
            cur.execute("SELECT * FROM thematic_areas WHERE ThematicAreaUkr=?", (tha_ukr,))
            rows = cur.fetchall()
            if not rows:
                messagebox.showerror("Помилка", "Записів з таким тематичним напрямком українською неіснує!")
            else:
                for row in rows:
                    tree.insert("", "end", values=row)
    def enabl_1():
        for child in f1.winfo_children():
            child.configure(state='normal')
        for child in f2.winfo_children():
            child.configure(state='disabled')
        for child in f3.winfo_children():
            child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
            child.configure(state='disabled')
        for child in f2.winfo_children():
            child.configure(state='normal')
        for child in f3.winfo_children():
            child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    id_ = ttk.Radiobutton(p1, text="Пошук за Id-тематичного напрямку", variable=var, value=1, command=enabl_1)
    id_.grid(row=0, column=0, sticky=W, pady=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, pady=2, sticky="nsew")
    eng = ttk.Radiobutton(p1, text="Пошук за тематичним напрямком англійською", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    ukr = ttk.Radiobutton(p1, text="Пошук за тематичним напрямком українською", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    f3 =  ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    l1 = Label(f1, text="Введіть Id-тематичного напрямку:")
    l1.grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Введіть тематичний напрямок англійською:")
    l2.grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Введіть тематичний напрямок українською:")
    l3.grid(row = 0, column = 0, sticky = W, pady = 2)
    e1 = Entry(f1, textvariable = id_var)
    e1.grid(row = 0, column = 1, pady = 2, padx =60)
    e2 = Entry(f2, textvariable = tha_eng_var)
    e2.grid(row = 0, column = 1, pady = 2, padx =5)
    e3 = Entry(f3, textvariable = tha_ukr_var)
    e3.grid(row = 0, column = 1, pady = 2, padx =5)
    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Знайти", command=a)
    b1.grid(row=6, column=0, pady=10, padx = 200)

def csearch_rev():
    id_var = IntVar()
    idar_var = IntVar()
    m1_var = IntVar()
    m2_var = IntVar()
    m3_var = IntVar()
    m4_var = IntVar()
    m5_var = IntVar()
    search_rev = Toplevel()
    var=IntVar()
    search_rev.title('Пошук')
    search_rev.iconbitmap('search.ico')
    search_rev.geometry("300x420")
    search_rev.resizable(FALSE, FALSE)
    p1 = ttk.Frame(search_rev)
    p1.grid(row=0, column=0, sticky="nsew")
    p1.grid_rowconfigure(0, weight=1)
    p1.grid_columnconfigure(0, weight=1)
    def a():
        table=Toplevel()
        table.title('Результат')
        tree = ttk.Treeview(table, columns=col_rev, show='headings')
        tree.heading('id_rev', text='Id-рецензії')
        tree.heading('id_art', text='Id-статті')
        tree.heading('m_nov', text='Новизна')
        tree.heading('m_topic', text='Актуальність')
        tree.heading('m_compll', text='Повнота літературного огляду')
        tree.heading('m_complp', text='Повнота викладення матеріалу')
        tree.heading('m_qual', text='Якість тексту')
        tree.heading('conclusion', text='Висновок')
        tree.heading('remarks', text='Зауваження')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        if var.get() == 1:  
           id = id_var.get()
           cur.execute("SELECT * FROM review WHERE IdReview=?", (id,))
           rows = cur.fetchall()
           if not rows:
              messagebox.showerror("Помилка", "Записів з таким ID неіснує!")
           else:
              for row in rows:
                tree.insert("", "end", values=row)
        elif var.get() == 2:  
           idar = idar_var.get()
           cur.execute("SELECT * FROM review WHERE IdArticle=?", (idar,))
           rows = cur.fetchall()
           if not rows:
               messagebox.showerror("Помилка", "Записів з таким ID-статті неіснує!")
           else:
               for row in rows:
                   tree.insert("", "end", values=row)
        elif var.get() == 3:  
           m1 = m1_var.get()
           cur.execute("SELECT * FROM review WHERE MarkNovelty=?", (m1,))
           rows = cur.fetchall()
           if not rows:
               messagebox.showerror("Помилка", "Записів з такою оцінкою неіснує!")
           else:
               for row in rows:
                   tree.insert("", "end", values=row)
        elif var.get() == 4:  
           m2 = m2_var.get()
           cur.execute("SELECT * FROM review WHERE MarkTopicality=?", (m2,))
           rows = cur.fetchall()
           if not rows:
               messagebox.showerror("Помилка", "Записів з такою оцінкою неіснує!")
           else:
               for row in rows:
                   tree.insert("", "end", values=row)
        elif var.get() == 5:  
           m3 = m3_var.get()
           cur.execute("SELECT * FROM review WHERE MarkCompletnessL=?", (m3,))
           rows = cur.fetchall()
           if not rows:
               messagebox.showerror("Помилка", "Записів з такою оцінкою неіснує!")
           else:
               for row in rows:
                   tree.insert("", "end", values=row)
        elif var.get() == 6:  
           m4 = m4_var.get()
           cur.execute("SELECT * FROM review WHERE MarkCompletnessP=?", (m4,))
           rows = cur.fetchall()
           if not rows:
               messagebox.showerror("Помилка", "Записів з такою оцінкою неіснує!")
           else:
               for row in rows:
                   tree.insert("", "end", values=row)
        elif var.get() == 7:  
           m5 = m5_var.get()
           cur.execute("SELECT * FROM review WHERE MarkQuality=?", (m5,))
           rows = cur.fetchall()
           if not rows:
               messagebox.showerror("Помилка", "Записів з такою оцінкою неіснує!")
           else:
               for row in rows:
                   tree.insert("", "end", values=row)
    def enabl_1():
        for child in f1.winfo_children():
           child.configure(state='normal')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
        for child in f4.winfo_children():
           child.configure(state='disabled')
        for child in f5.winfo_children():
           child.configure(state='disabled')
        for child in f6.winfo_children():
           child.configure(state='disabled')
        for child in f7.winfo_children():
           child.configure(state='disabled')
    def enabl_2():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='normal')
        for child in f3.winfo_children():
           child.configure(state='disabled')
        for child in f4.winfo_children():
           child.configure(state='disabled')
        for child in f5.winfo_children():
           child.configure(state='disabled')
        for child in f6.winfo_children():
           child.configure(state='disabled')
        for child in f7.winfo_children():
           child.configure(state='disabled')
    def enabl_3():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='normal')
        for child in f4.winfo_children():
           child.configure(state='disabled')
        for child in f5.winfo_children():
           child.configure(state='disabled')
        for child in f6.winfo_children():
           child.configure(state='disabled')
        for child in f7.winfo_children():
           child.configure(state='disabled')
    def enabl_4():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
        for child in f4.winfo_children():
           child.configure(state='normal')
        for child in f5.winfo_children():
           child.configure(state='disabled')
        for child in f6.winfo_children():
           child.configure(state='disabled')
        for child in f7.winfo_children():
           child.configure(state='disabled')
    def enabl_5():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
        for child in f4.winfo_children():
           child.configure(state='disabled')
        for child in f5.winfo_children():
           child.configure(state='normal')
        for child in f6.winfo_children():
           child.configure(state='disabled')
        for child in f7.winfo_children():
           child.configure(state='disabled')
    def enabl_6():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
        for child in f4.winfo_children():
           child.configure(state='disabled')
        for child in f5.winfo_children():
           child.configure(state='disabled')
        for child in f6.winfo_children():
           child.configure(state='normal')
        for child in f7.winfo_children():
           child.configure(state='disabled')
    def enabl_7():
        for child in f1.winfo_children():
           child.configure(state='disabled')
        for child in f2.winfo_children():
           child.configure(state='disabled')
        for child in f3.winfo_children():
           child.configure(state='disabled')
        for child in f4.winfo_children():
           child.configure(state='disabled')
        for child in f5.winfo_children():
           child.configure(state='disabled')
        for child in f6.winfo_children():
           child.configure(state='disabled')
        for child in f7.winfo_children():
           child.configure(state='normal')
    var = IntVar()
    rbid = ttk.Radiobutton(p1, text="Пошук за Id-рецензії", variable=var, value=1, command=enabl_1).grid(row=0, column=0, sticky=W, pady=2, padx=2)
    f1 = ttk.Frame(p1, relief=GROOVE)
    f1.grid(row=1, column=0, sticky=W, pady=2)
    rbidar = ttk.Radiobutton(p1, text="Пошук за Id-статті", variable=var, value=2, command=enabl_2).grid(row=2, column=0, sticky=W, pady=2, padx=2)
    f2 =  ttk.Frame(p1, relief=GROOVE)
    f2.grid(row=3, column=0, sticky=W, pady=2)
    rbn = ttk.Radiobutton(p1, text="Пошук за оцінкою новизни", variable=var, value=3, command=enabl_3).grid(row=4, column=0, sticky=W, pady=2, padx=2)
    f3 = ttk.Frame(p1, relief=GROOVE)
    f3.grid(row=5, column=0, sticky=W, pady=2)
    rba = ttk.Radiobutton(p1, text="Пошук за оцінкою актальності", variable=var, value=4, command=enabl_4).grid(row=6, column=0, sticky=W, pady=2, padx=2)
    f4 = ttk.Frame(p1, relief=GROOVE)
    f4.grid(row=7, column=0, sticky=W, pady=2)
    rbl = ttk.Radiobutton(p1, text="Пошук за оцінкою повноти літературного огляду", variable=var, value=5, command=enabl_5).grid(row=8, column=0, sticky=W, pady=2, padx=2)
    f5 =  ttk.Frame(p1, relief=GROOVE)
    f5.grid(row=9, column=0, sticky=W, pady=2)
    rbc = ttk.Radiobutton(p1, text="Пошук за оцінкою повнити викладення", variable=var, value=6, command=enabl_6).grid(row=10, column=0, sticky=W, pady=2, padx=2)
    f6 = ttk.Frame(p1, relief=GROOVE)
    f6.grid(row=11, column=0, sticky=W, pady=2)
    rbq = ttk.Radiobutton(p1, text="Пошук за оцінкою наукової якості", variable=var, value=7, command=enabl_7).grid(row=12, column=0, sticky=W, pady=2, padx=2)
    f7 = ttk.Frame(p1, relief=GROOVE)
    f7.grid(row=13, column=0, sticky=W, pady=2)

    l1 = Label(f1, text="Id-рецензії:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l2 = Label(f2, text="Id-статті:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l3 = Label(f3, text="Новизна:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l4 = Label(f4, text="Актуальність:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l5 = Label(f5, text="Повнота літературного огляду:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l6 = Label(f6, text="Повнота викладення:").grid(row = 0, column = 0, sticky = W, pady = 2)
    l7 = Label(f7, text="Наукова якість:").grid(row = 0, column = 0, sticky = W, pady = 2)
    e1 = Entry(f1, textvariable = id_var).grid(row = 0, column = 1, pady = 2, padx=108)
    e2 = Entry(f2, textvariable = idar_var).grid(row = 0, column = 1, pady = 2, padx=122)
    e3 = Entry(f3, textvariable = m1_var).grid(row = 0, column = 1, pady = 2, padx=120)
    e4 = Entry(f4, textvariable = m2_var).grid(row = 0, column = 1, pady = 2, padx=96)
    e5 = Entry(f5, textvariable = m3_var).grid(row = 0, column = 1, pady = 2)
    e5 = Entry(f6, textvariable = m4_var).grid(row = 0, column = 1, pady = 2, padx=54)
    e5 = Entry(f7, textvariable = m5_var).grid(row = 0, column = 1, pady = 2, padx=85)


    for child in f1.winfo_children():
           child.configure(state='disabled')
    for child in f2.winfo_children():
           child.configure(state='disabled')
    for child in f3.winfo_children():
           child.configure(state='disabled')
    for child in f4.winfo_children():
           child.configure(state='disabled')
    for child in f5.winfo_children():
           child.configure(state='disabled')
    for child in f6.winfo_children():
           child.configure(state='disabled')
    for child in f7.winfo_children():
           child.configure(state='disabled')
    b1 = Button(p1, text="Знайти", command=a)
    b1.grid(row=14, column=0, pady=10, padx = 150)
#######
def ar_au():
    id_var = StringVar()
    if len(tree_au.selection()) > 0:
        table = Toplevel()
        table.title('Статті автора')
        table.iconbitmap('article.ico')
        tree = ttk.Treeview(table, columns=col_ar, show='headings')
        tree.heading('id_art', text='Id-статті')
        tree.heading('title', text='Заголовок')
        tree.heading('date', text='Дата')
        tree.heading('link', text='Посилання')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        selected_item = tree_au.selection()[0]
        record_data = tree_au.item(selected_item)['values']
        id_var.set(record_data[0])
        id = id_var.get()
        cursor = db.aql.execute("FOR author IN author FILTER author._key == @id FOR article_author IN article_author FILTER article_author._from == author._id FOR article IN article FILTER article._id == article_author._to RETURN article", bind_vars={'id': id})
        results = list(cursor)
        if len(results) == 0:
           messagebox.showerror("Помилка", "У цього автора ще немає статтей!")
        else:
            for doc in results:
               values = (doc['_key'], doc['Title'], doc['Date'], doc['FileLink'])
               tree.insert('', 'end', None, values=values)
    else:
        messagebox.showerror("Помилка", "Оберіть запис у таблиці!")

def au_ar():
    id_var = IntVar()
    if len(tree_ar.selection()) > 0:
        table = Toplevel()
        table.title('Автори статті')
        table.iconbitmap('person.ico')
        tree = ttk.Treeview(table, columns=col_au, show='headings')
        tree.heading('id_auth', text='Id-автора')
        tree.heading('name', text='Ім`я')
        tree.heading('surname', text='Прізвище')
        tree.heading('middle_name', text='По батькові')
        tree.heading('phone_num', text='Номер телефону')
        tree.heading('email', text='Email')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        selected_item = tree_ar.selection()[0]
        record_data = tree_ar.item(selected_item)['values']
        id_var.set(record_data[0])
        id = id_var.get()
        cur.execute("SELECT * FROM author WHERE IdAuthor IN (SELECT IdAuthor FROM article_author WHERE IdArticle = ?)", (id,))
        rows = cur.fetchall()
        if not rows:
           messagebox.showerror("Помилка", "Для цієї статті не призначено авторів!")
        else:
           for row in rows:
              tree.insert("", "end", values=row)
    else:
        messagebox.showerror("Помилка", "Оберіть запис у таблиці!")

def kw_ar():
    id_var = IntVar()
    if len(tree_ar.selection()) > 0:
        table = Toplevel()
        table.title('Ключові слова статті')
        table.iconbitmap('key.ico')
        tree = ttk.Treeview(table, columns=col_kw, show='headings')
        tree.heading('id_kw', text='Id-ключового слова')
        tree.heading('kw_eng', text='Ключове слово англійською')
        tree.heading('kw_ukr', text='Ключове слово українською')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        selected_item = tree_ar.selection()[0]
        record_data = tree_ar.item(selected_item)['values']
        id_var.set(record_data[0])
        id = id_var.get()
        cur.execute("SELECT * FROM key_words WHERE IdKeyWord IN (SELECT IdKeyWord FROM article_keywords WHERE IdArticle = ?)", (id,))
        rows = cur.fetchall()
        if not rows:
           messagebox.showerror("Помилка", "У цієї статті немає ключових слів!")
        else:
           for row in rows:
              tree.insert("", "end", values=row)
    else:
        messagebox.showerror("Помилка", "Оберіть запис у таблиці!")

def ar_kw():
    id_var = IntVar()
    if len(tree_kw.selection()) > 0:
        table = Toplevel()
        table.title('Статті ключового слова')
        table.iconbitmap('article.ico')
        tree = ttk.Treeview(table, columns=col_ar, show='headings')
        tree.heading('id_art', text='Id-статті')
        tree.heading('title', text='Заголовок')
        tree.heading('date', text='Дата')
        tree.heading('link', text='Посилання')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        selected_item = tree_kw.selection()[0]
        record_data = tree_kw.item(selected_item)['values']
        id_var.set(record_data[0])
        id = id_var.get()
        cur.execute("SELECT * FROM article WHERE IdArticle IN (SELECT IdArticle FROM article_keywords WHERE IdKeyWord = ?)", (id,))
        rows = cur.fetchall()
        if not rows:
           messagebox.showerror("Помилка", "Це ключове слово ще не застосовано до статтей!")
        else:
           for row in rows:
              tree.insert("", "end", values=row)
    else:
        messagebox.showerror("Помилка", "Оберіть запис у таблиці!")

def tha_revr():
    id_var = IntVar()
    if len(tree_revr.selection()) > 0:
        table = Toplevel()
        table.title('Тематичні напрямки рецензента')
        table.iconbitmap('key.ico')
        tree = ttk.Treeview(table, columns=col_tha, show='headings')
        tree.heading('id_tha', text='Id-тематичного напряму')
        tree.heading('tha_eng', text='Тематичний напрямок англійською')
        tree.heading('tha_ukr', text='Тематичний напрямок українською')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        selected_item = tree_revr.selection()[0]
        record_data = tree_revr.item(selected_item)['values']
        id_var.set(record_data[0])
        id = id_var.get()
        cur.execute("SELECT * FROM thematic_areas WHERE IdThematicArea IN (SELECT IdThematicArea FROM reviewer_thematicareas WHERE IdReviewer = ?)", (id,))
        rows = cur.fetchall()
        if not rows:
           messagebox.showerror("Помилка", "У цього рецензента немає тематичних напрямків!")
        else:
           for row in rows:
              tree.insert("", "end", values=row)
    else:
        messagebox.showerror("Помилка", "Оберіть запис у таблиці!")

def revr_tha():
    id_var = IntVar()
    if len(tree_tha.selection()) > 0:
        table = Toplevel()
        table.title('Рецензенти з тематичним напрямком')
        table.iconbitmap('person.ico')
        tree = ttk.Treeview(table, columns=col_revr, show='headings')
        tree.heading('id_revr', text='Id-рецензенту')
        tree.heading('name', text='Ім`я')
        tree.heading('surname', text='Прізвище')
        tree.heading('middle_name', text='По батькові')
        tree.heading('email', text='Email')
        tree.grid(row=0, column=0, sticky='nsew')
        table.columnconfigure(0, weight=1)
        selected_item = tree_tha.selection()[0]
        record_data = tree_tha.item(selected_item)['values']
        id_var.set(record_data[0])
        id = id_var.get()
        cur.execute("SELECT * FROM reviewer WHERE IdReviewer IN (SELECT IdReviewer FROM reviewer_thematicareas WHERE IdThematicArea = ?)", (id,))
        rows = cur.fetchall()
        if not rows:
           messagebox.showerror("Помилка", "Немає рецензентів з цим тематичним напрямком!")
        else:
           for row in rows:
              tree.insert("", "end", values=row)
    else:
        messagebox.showerror("Помилка", "Оберіть запис у таблиці!")

add_au = Button(p1, text="Додати", command=cadd_au)
add_au.grid(row=0, column=0, sticky="NW", padx=0)
del_au = Button(p1, text="Видалити", command=cdel_au)
del_au.grid(row=0, column=1, sticky="N", padx=0)
upd_au = Button(p1, text="Змінити", command=cupd_au)
upd_au.grid(row=0, column=2, sticky="N", padx=0)
sort_au = Button(p1, text="Сортування", command=csort_au)
sort_au.grid(row=0, column=3, sticky="N", padx=0)
search_au = Button(p1, text="Пошук", command=csearch_au)
search_au.grid(row=0, column=4, sticky="N", padx=0)
art_auth = Button(p1, text="Статті автора", command=ar_au)
art_auth.grid(row=0, column=5, sticky="N", padx=0)

add_ar = Button(p2, text="Додати", command=cadd_ar)
add_ar.grid(row=0, column=0, sticky="NW", padx=0)
del_ar = Button(p2, text="Видалити", command=cdel_ar)
del_ar.grid(row=0, column=1, sticky="N", padx=0)
upd_ar = Button(p2, text="Змінити", command=cupd_ar)
upd_ar.grid(row=0, column=2, sticky="N", padx=0)
sort_ar = Button(p2, text="Сортування", command=csort_ar)
sort_ar.grid(row=0, column=3, sticky="N", padx=0)
search_ar = Button(p2, text="Пошук", command=csearch_ar)
search_ar.grid(row=0, column=4, sticky="N", padx=0)
auth_art = Button(p2, text="Автори статті", command=au_ar)
auth_art.grid(row=0, column=5, sticky="N", padx=0)
kw_art = Button(p2, text="Ключові слова статті", command=kw_ar)
kw_art.grid(row=0, column=6, sticky="N", padx=0)

add_ann = Button(p3, text="Додати", command=cadd_ann)
add_ann.grid(row=0, column=0, sticky="NW", padx=0)
del_ann = Button(p3, text="Видалити", command=cdel_ann)
del_ann.grid(row=0, column=1, sticky="N", padx=0)
upd_ann = Button(p3, text="Змінити", command=cupd_ann)
upd_ann.grid(row=0, column=2, sticky="N", padx=0)
sort_ann = Button(p3, text="Сортування", command=csort_ann)
sort_ann.grid(row=0, column=3, sticky="N", padx=0)
search_ann = Button(p3, text="Пошук", command=csearch_ann)
search_ann.grid(row=0, column=4, sticky="N", padx=0)

add_kw = Button(p4, text="Додати", command=cadd_kw)
add_kw.grid(row=0, column=0, sticky="NW", padx=0)
del_kw = Button(p4, text="Видалити", command=cdel_kw)
del_kw.grid(row=0, column=1, sticky="N", padx=0)
sort_kw = Button(p4, text="Сортування", command=csort_kw)
sort_kw.grid(row=0, column=2, sticky="N", padx=0)
search_kw = Button(p4, text="Пошук", command=csearch_kw)
search_kw.grid(row=0, column=3, sticky="N", padx=0)
art_kw = Button(p4, text="Статті ключового слова", command=ar_kw)
art_kw.grid(row=0, column=4, sticky="N", padx=0)

add_revr = Button(p5, text="Додати", command=cadd_revr)
add_revr.grid(row=0, column=0, sticky="NW", padx=0)
del_revr = Button(p5, text="Видалити", command=cdel_revr)
del_revr.grid(row=0, column=1, sticky="N", padx=0)
upd_revr = Button(p5, text="Змінити", command=cupd_revr)
upd_revr.grid(row=0, column=2, sticky="N", padx=0)
sort_revr = Button(p5, text="Сортування", command=csort_revr)
sort_revr.grid(row=0, column=3, sticky="N", padx=0)
search_revr = Button(p5, text="Пошук", command=csearch_revr)
search_revr.grid(row=0, column=4, sticky="N", padx=0)
tha_reviewer = Button(p5, text="Тематичні напрямки рецензента", command=tha_revr)
tha_reviewer.grid(row=0, column=5, sticky="N", padx=0)

add_rev = Button(p6, text="Додати", command=cadd_rev)
add_rev.grid(row=0, column=0, sticky="NW", padx=0)
sort_rev = Button(p6, text="Сортування", command=csort_rev)
sort_rev.grid(row=0, column=1, sticky="N", padx=0)
search_rev = Button(p6, text="Пошук", command=csearch_rev)
search_rev.grid(row=0, column=2, sticky="N", padx=0)

add_tha = Button(p7, text="Додати", command=cadd_tha)
add_tha.grid(row=0, column=0, sticky="NW", padx=0)
del_tha = Button(p7, text="Видалити", command=cdel_tha)
del_tha.grid(row=0, column=1, sticky="N", padx=0)
sort_tha = Button(p7, text="Сортування", command=csort_tha)
sort_tha.grid(row=0, column=2, sticky="N", padx=0)
search_tha = Button(p7, text="Пошук", command=csearch_tha)
search_tha.grid(row=0, column=3, sticky="N", padx=0)
reviewer_tha = Button(p7, text="Тематичні напрямки рецензента", command=revr_tha)
reviewer_tha.grid(row=0, column=4, sticky="N", padx=0)

root.mainloop()
