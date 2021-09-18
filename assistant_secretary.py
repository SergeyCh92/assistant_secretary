import sys
import tkinter as tk

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def press_key(event):
	global last_btn
	if event.char == '\r':
		(last_btn)()

def print_name(num, doc=documents):
	request = num
	for el in doc:
		if el['number'] == num:
			# print(el['name'])
			return el['name']
		else:
			continue
	return 'Документ с указанным номером отсутствует.'

def search_shelf(num ,my_dir=directories):
	available = False
	# number = input('Введите номер документа: ')
	for el in my_dir.values():
		if num in el:
			available = True
			break
	
	if available:
		for shelf, numb in my_dir.items():
			for i in numb:
				if i == num:
					return f'Документ номер {num} на полке {shelf}.'
					# break
	else:
		return 'Документ с указанным Вами номером не существует.'

def print_list(doc=documents):
	data = ''
	count = 0
	for list_doc in doc:
		for el in list_doc.values():
			data += ' ' + el
			count += 1
			if count == 3:
				data += '\n'
				count = 0
	return data

def add_doc(doc=documents, my_dir=directories):
	my_list = [i for i in my_dir]
	my_str = ''
	count = 0
	for i in my_list:
		if count != len(my_list) - 1:
			my_str += i + ', '
			count += 1
		else:
			my_str += i

	data = input('Введите тип документа (например passport): ')
	person = input('Введите имя владельца: ')
	number_doc = input('Введите номер документа: ')
	number_shelf = input(f'Введите номер полки, на которую хотите поместить досье (выберите из списка - {my_str}): ')
	
	if number_shelf not in my_dir:
		print('Выбранная Вами полка не существует. Повторите вызов команды и выберите полку из предложенного списка.')
	else:
		doc.append({'type': data, 'number': number_doc, 'name': person})
		my_dir[number_shelf].append(number_doc)
		print('Введенные Вами данные успешно добавлены.')

def del_doc(number ,doc=documents, my_dir=directories):
	available = False
	# number = input('Введите номер документа подлежащего удалению: ')
	for el in my_dir.values():
		if number in el:
			available = True
			break
	
	if available:
		end = False
		for shelf, num in my_dir.items():
			if end:
				break
			for i in num:
				if i == number:
					my_dir[shelf].remove(number)
					# print(f'Документ номер {number} удален с полки {shelf}.')
					end = True
					break
		for el in doc:
			if el['number'] == number:
				doc.remove(el)
				return f'Документ номер {number} удален с полки {shelf}.'
	else:
		return 'Документ с указанным Вами номером не существует.'

def move_doc(shelf, number ,doc=documents, my_dir=directories):
	available = False
	old_shelf = ''
	# shelf = input('Введите номер полки, на которую Вы хотите переместить документ: ')
	# number = input('Введите номер документа, который необходимо переместить: ')

	if shelf not in my_dir:
		# print('Указанная Вами полка отсутствует.')
		return 'Указанная Вами полка отсутствует.'
	for sh, num in my_dir.items():
		if number in num:
			available = True
			old_shelf = sh
			break

	if available:
		my_dir[shelf].append(number)
		my_dir[old_shelf].remove(number)
		return f'Документ {number} перемещен на полку {shelf}.'
	else:
		return 'Указанный Вами документ отсутствует.'

def add_shelf(my_dir=directories):
	shelf = input('Введите номер полки, которую хотите добавить: ')

	if shelf in my_dir:
		print('Такая полка уже существует.')
	else:
		my_dir[shelf] = []
		print(f'Полка номер {shelf} успешно добавлена.')

def error():
	print('Введенная Вами команда не существует.')

text1 = '''Для работы с документами Вам доступны следующие команды:
	p – people - команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
	s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится
	l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
	a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
	d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.
	m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую
	as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
	q - quit - команда, которая завершит работу программы
	h - help - повторно выведет данное меню '''

# словарь использовался для консольной версии
# comm_dict = {
# 	'p': print_name,
# 	's': search_shelf,
# 	'l': print_list,
# 	'a': add_doc,
# 	'd': del_doc,
# 	'm': move_doc,
# 	'as': add_shelf,
# 	'q': sys.exit,
# 	'h': lambda: print(text1)
# }

# цикл использовался для консольной версии программы
# print(text)
# while True:
# 	print()
# 	command = input('Введите команду: ')
# 	command = command.lower().strip()
	# comm_dict.get(command, error)()

def p():
	"""Принимает номер документа и выводит на экран имя владельца"""
	global last_btn
	val = input_field.get()
	if not val:
		dispaly_field.delete(1.0, 'end')
		dispaly_field.insert(1.0, 'Введите номер документа: ')
	elif val:
		display_val = print_name(val)
		dispaly_field.delete(1.0, 'end')
		dispaly_field.insert(1.0, display_val)
		input_field.delete(0, 'end')
	last_btn = p

def pl():
	global last_btn
	dispaly_field.delete(1.0, 'end')
	dispaly_field.insert(1.0, print_list())
	last_btn = pl

def h():
	global last_btn
	dispaly_field.delete(1.0, 'end')
	dispaly_field.insert(1.0, text1)
	last_btn = h

def s():
	global last_btn
	val = input_field.get()
	if not val:
		dispaly_field.delete(1.0, 'end')
		dispaly_field.insert(1.0, 'Введите номер документа: ')
	else:
		display_val = search_shelf(val)
		dispaly_field.delete(1.0, 'end')
		dispaly_field.insert(1.0, display_val)
		input_field.delete(0, 'end')
	last_btn = s

def a_display(question):
	dispaly_field.delete(1.0, 'end')
	dispaly_field.insert(1.0, question)

type_doc = ''
person = ''
number_doc = ''
number_shelf = ''

def a(doc=documents, my_dir=directories):
	global last_btn
	my_list = [i for i in my_dir]
	my_str = ''
	count = 0
	for i in my_list:
		if count != len(my_list) - 1:
			my_str += i + ', '
			count += 1
		else:
			my_str += i

	global type_doc
	global person
	global number_doc
	global number_shelf

	if not type_doc:
		a_display('Введите тип документа: (например passport)')
		type_doc = input_field.get()
		input_field.delete(0, 'end')
	if type_doc and not person:
		a_display('Введите имя владельца: ')
		person = input_field.get()
		input_field.delete(0, 'end')
	if type_doc and person and not number_doc:
		a_display('Введите номер документа: ')
		number_doc = input_field.get()
		input_field.delete(0, 'end')
	if type_doc and person and number_doc and not number_shelf:
		dispaly_field.delete(1.0, 'end')
		dispaly_field.insert(1.0, f'Введите номер полки, на которую хотите поместить досье (выберите из списка - {my_str}): ')
		number_shelf = input_field.get()
		input_field.delete(0, 'end')

	if number_shelf:
		if number_shelf not in my_dir:
			dispaly_field.delete(1.0, 'end')
			dispaly_field.insert(1.0, 'Выбранная Вами полка не существует. Повторите вызов команды и выберите полку из предложенного списка.')
			type_doc = ''
			person = ''
			number_doc = ''
			number_shelf = ''
		else:
			doc.append({'type': type_doc, 'number': number_doc, 'name': person})
			my_dir[number_shelf].append(number_doc)
			dispaly_field.delete(1.0, 'end')
			dispaly_field.insert(1.0, 'Введенные Вами данные успешно добавлены.')
			type_doc = ''
			person = ''
			number_doc = ''
			number_shelf = ''
	last_btn = a

def d():
	global last_btn
	dispaly_field.delete(1.0, 'end')
	val = input_field.get()
	a_display('Введите номер документа, подлежащего удалению:')
	if val:
		a_display(del_doc(val))
		input_field.delete(0, 'end')
	last_btn = d

shelf = ''
number = ''

def m():
	global last_btn
	global shelf
	global number

	if not shelf:
		a_display('Введите номер полки, на которую Вы хотите переместить документ: ')
		shelf = input_field.get()
		input_field.delete(0, 'end')
	if shelf and not number:
		a_display('Введите номер документа, который необходимо переместить: ')
		number = input_field.get()
		input_field.delete(0, 'end')
	if number:
		a_display(move_doc(shelf, number))
		input_field.delete(0, 'end')
		shelf = ''
		number = ''
	last_btn = m

last_btn = h

def create_btn(r, c, name, com):
	return tk.Button(text=name, font=('Times new roman', 13), command=com). grid(row=r, column=c, stick='we', padx=5, pady=3)


win = tk.Tk()
win.minsize(500, 350)
win.maxsize(1000, 700)
win.title('Помощник секретаря')
win.geometry('1000x700+460+200')
win.config(bg='#3a506e')
win.resizable(False, False)

dispaly_field = tk.Text(win, font=('Arial', 15), width=89, height=17)
dispaly_field.insert(1.0, text1)
input_field = tk.Entry(win, font=('Arial', 10), width=89)
btn_q = tk.Button(text='q', font=('Times new roman', 13), activebackground='red', command=lambda : sys.exit())
btn_d = tk.Button(text='d', font=('Times new roman', 13), command=d)

dispaly_field.grid(row=0, column=0, columnspan=8, stick='we', padx=5)
input_field.grid(row=1, column=0, stick='we', columnspan=8, padx=5, pady=3)

create_btn(2, 0, 'p', p)
create_btn(2, 1, 'l', pl)
create_btn(2, 2, 'h', h)
create_btn(2, 4, 's', s)
create_btn(2, 5, 'a', a)
create_btn(3, 0, 'm', m)

btn_q.grid(row=2, column=3, stick='we', padx=5, pady=3)
btn_d.grid(row=2, column=6, stick='we', padx=5, pady=3, columnspan=2)

win.bind('<Key>', press_key)

win.mainloop()