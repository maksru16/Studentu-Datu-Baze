import tkinter as tk
import sqlite3
from tkinter import messagebox

top = tk.Tk()
top.title('Database of new students')
top.geometry("693x900")
top.configure(background='#595260', pady=3)

conn = sqlite3.connect('new_students.db')

c = conn.cursor()

c.execute("""CREATE TABLE if not exists students (
    first_name text, 
    last_name text,
    age integer,
    gender text,
    speciality text,
    language text,
    category text,
    study_place text,
    gpa integer,
    exam_grade integer
    )""")

def update():
    conn = sqlite3.connect('new_students.db')
    c = conn.cursor()

    record_id = delete_box.get()
    
    c.execute("""UPDATE students SET
          first_name = :first, 
          last_name = :last,
          age = :age,
          gender = :gender,
          speciality = :speciality,
          language = :language,
          category = :category,
          study_place = :study_place,
          gpa = :gpa,
          exam_grade = :exam_grade

          WHERE oid = :oid""",
            {
            'first': f_name_edit.get(),
            'last': l_name_edit.get(),
            'age': age_edit.get(),
            'gender': gender_edit.get(),
            'speciality': speciality_edit.get(),
            'language': language_edit.get(),
            'category': l_category_edit.get(),
            'study_place': study_place_edit.get(),
            'gpa' : gpa_edit.get(),
            'exam_grade': exam_grade_edit.get(),
            'oid': record_id
            })
    
    conn.commit()
    conn.close()

    edit_window.destroy()
    
# Edit function
def edit():
    global edit_window
    edit_window = tk.Tk()
    edit_window.title('Database Record Editor')
    edit_window.geometry("693x510")
    edit_window.configure(background='#595260', pady=3)

    conn = sqlite3.connect('new_students.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM students WHERE oid = " + record_id)
    records = c.fetchall()

    global f_name_edit
    global l_name_edit
    global age_edit
    global gender_edit
    global speciality_edit
    global language_edit
    global l_category_edit
    global study_place_edit
    global gpa_edit
    global exam_grade_edit
    
    # Text boxes
    f_name_edit = tk.Entry(edit_window, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
    f_name_edit.grid(row=0, column=1)
    l_name_edit = tk.Entry(edit_window, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
    l_name_edit.grid(row=1, column=1)
    age_edit = tk.Entry(edit_window, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
    age_edit.grid(row=2, column=1)
    gender_edit = tk.Entry(edit_window, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
    gender_edit.grid(row=3, column=1)
    speciality_edit = tk.Entry(edit_window, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
    speciality_edit.grid(row=4, column=1)
    language_edit = tk.Entry(edit_window, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
    language_edit.grid(row=5, column=1)
    l_category_edit = tk.Entry(edit_window, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
    l_category_edit.grid(row=6, column=1)
    study_place_edit = tk.Entry(edit_window, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
    study_place_edit.grid(row=7, column=1)
    gpa_edit = tk.Entry(edit_window, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
    gpa_edit.grid(row=8, column=1)
    exam_grade_edit = tk.Entry(edit_window, width=30, borderwidth=6, relief="sunken", font = ('Helvetica Neue', 19))
    exam_grade_edit.grid(row=9, column=1)

    # Text box labels
    f_name_label = tk.Label(edit_window, text="Name", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#B3B6B7')
    f_name_label.grid(row=0, column=0)
    l_name_label = tk.Label(edit_window, text="Surname", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#B3B6B7')
    l_name_label.grid(row=1, column=0)
    age_label = tk.Label(edit_window, text="Age", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#B3B6B7')
    age_label.grid(row=2, column=0)
    gender_label = tk.Label(edit_window, text="Gender", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#B3B6B7')
    gender_label.grid(row=3, column=0)
    speciality_label = tk.Label(edit_window, text="Speciality", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#B3B6B7')
    speciality_label.grid(row=4, column=0)
    language_label = tk.Label(edit_window, text="Language", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#B3B6B7')
    language_label.grid(row=5, column=0)
    l_category_label = tk.Label(edit_window, text="Language Category", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#B3B6B7')
    l_category_label.grid(row=6, column=0)
    study_place_label = tk.Label(edit_window, text="Study place", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#B3B6B7')
    study_place_label.grid(row=7, column=0)
    gpa_edit_label = tk.Label(edit_window, text="GPA", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#B3B6B7')
    gpa_edit_label.grid(row=8, column=0)
    exam_grade_label = tk.Label(edit_window, text="Exam Grade", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#B3B6B7')
    exam_grade_label.grid(row=9, column=0)

    for record in records:
        f_name_edit.insert(0, record[0])
        l_name_edit.insert(0, record[1])
        age_edit.insert(0, record[2])
        gender_edit.insert(0, record[3])
        speciality_edit.insert(0, record[4])
        language_edit.insert(0, record[5])
        l_category_edit.insert(0, record[6])
        study_place_edit.insert(0, record[7])
        gpa_edit.insert(0, record[8])
        exam_grade_edit.insert(0, record[9])
        
    # Create a Save Button
    save_button = tk.Button(edit_window, text="Save Record", font = ('Helvetica Neue', 13, 'bold'), borderwidth=7, relief="raised", bg='#FF9500', command=update)
    save_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
    
# Delete function
def delete():
    conn = sqlite3.connect('new_students.db')
    c = conn.cursor()

    c.execute("DELETE from students WHERE oid = " + delete_box.get())

    tk.messagebox.showinfo(title='Removing from the database', message='This entry has been removed from the database')
    
    conn.commit()
    conn.close()
    
# Submit function
def submit():
    conn = sqlite3.connect('new_students.db')
    c = conn.cursor()

    c.execute("INSERT INTO students VALUES (:f_name, :l_name, :age, :gender, :speciality, :language, :l_category, :study_place, :gpa, :exam_grade)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'age': age.get(),
                  'gender': gender.get(),
                  'speciality': speciality.get(),
                  'language': language.get(),
                  'l_category': l_category.get(),
                  'study_place': study_place.get(),
                  'gpa' : gpa.get(),
                  'exam_grade': exam_grade.get(),
              })
    
    conn.commit()
    conn.close()

    f_name.delete(0, tk.END)
    l_name.delete(0, tk.END)
    age.delete(0, tk.END)
    gender.delete(0, tk.END)
    speciality.delete(0, tk.END)
    language.delete(0, tk.END)
    l_category.delete(0, tk.END)
    study_place.delete(0, tk.END)
    gpa.delete(0, tk.END)
    exam_grade.delete(0, tk.END)

def query():
    conn = sqlite3.connect('new_students.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM students")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[10]) + " " + "\t" + str(record[0]) + " " + str(record[1]) + "\n"

    query_label = tk.Label(top, font = ('Helvetica Neue', 13, 'bold'), bg='#595260', justify='left', text=print_records)
    query_label.grid(row=17, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Text boxes
f_name = tk.Entry(top, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
f_name.grid(row=0, column=1)
l_name = tk.Entry(top, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
l_name.grid(row=1, column=1)
age = tk.Entry(top, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
age.grid(row=2, column=1)
gender = tk.Entry(top, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
gender.grid(row=3, column=1)
speciality = tk.Entry(top, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
speciality.grid(row=4, column=1)
language = tk.Entry(top, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
language.grid(row=5, column=1)
l_category = tk.Entry(top, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
l_category.grid(row=6, column=1)
study_place = tk.Entry(top, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
study_place.grid(row=7, column=1)
gpa = tk.Entry(top, width=30, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19))
gpa.grid(row=8, column=1)
exam_grade = tk.Entry(top, width=30, borderwidth=6, relief="sunken", font = ('Helvetica Neue', 19))
exam_grade.grid(row=9, column=1)
delete_box = tk.Entry(top, width=16, borderwidth=6, relief="sunken", font = ('Helvetica Neue', 13, 'bold'))
delete_box.grid(row=14, column=1)

# Text box labels
f_name_label = tk.Label(top, text="Name", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#D4D4D2')
f_name_label.grid(row=0, column=0)
l_name_label = tk.Label(top, text="Surname", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#D4D4D2')
l_name_label.grid(row=1, column=0)
age_label = tk.Label(top, text="Age", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#D4D4D2')
age_label.grid(row=2, column=0)
gender_label = tk.Label(top, text="Gender", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#D4D4D2')
gender_label.grid(row=3, column=0)
speciality_label = tk.Label(top, text="Speciality", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#D4D4D2')
speciality_label.grid(row=4, column=0)
language_label = tk.Label(top, text="Language", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#D4D4D2')
language_label.grid(row=5, column=0)
l_category_label = tk.Label(top, text="Language Category", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#D4D4D2')
l_category_label.grid(row=6, column=0)
study_place_label = tk.Label(top, text="Study place", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#D4D4D2')
study_place_label.grid(row=7, column=0)
gpa_label = tk.Label(top, text="GPA", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#D4D4D2')
gpa_label.grid(row=8, column=0)
exam_grade_label = tk.Label(top, text="Exam Grade", width=16, borderwidth=7, relief="sunken", font = ('Helvetica Neue', 19), bg='#D4D4D2')
exam_grade_label.grid(row=9, column=0)
delete_box_label = tk.Label(top, text="Selected ID", font = ('Helvetica Neue', 13, 'bold'))
delete_box_label.place(x=290, y=633)

# Submit Button
submit_button = tk.Button(top, text="Add Record", font = ('Helvetica Neue', 13, 'bold'), borderwidth=7, relief="raised", bg='#FF9500', command=submit)
submit_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=147)

# Create a Query Button
query_button = tk.Button(top, text="Show Records", font = ('Helvetica Neue', 13, 'bold'), borderwidth=7, relief="raised", bg='#FF9500', command=query)
query_button.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_button = tk.Button(top, text="Delete Record", font = ('Helvetica Neue', 13, 'bold'), borderwidth=7, relief="raised", bg='#FF9500', command=delete)
delete_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create an Update Button
update_button = tk.Button(top, text="Edit Record", font = ('Helvetica Neue', 13, 'bold'), borderwidth=7, relief="raised", bg='#FF9500', command=edit)
update_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=147)

conn.commit()

# Connect OFF
conn.close()

top.mainloop()
