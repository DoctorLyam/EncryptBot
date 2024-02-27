#from get_token import generate_token
import codecs
from random import choice, sample
import numpy as np
import os

import telebot
from telebot import types, State
bot=telebot.TeleBot('...') #библиотека telebot, класс TeleBot

tokens_dict = {}
flag = ''

k1 = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р']
k2 = ['с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','a','b','c']
k3 = ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
k4 = ['v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','?','!']

keylist = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н',
           'о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','?','!']

letters_in_name = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н',
           'о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
           's','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','_']


@bot.message_handler(commands=['start']) #какие команды будем отслеживать
def start(message): #метод лучше создать по имени коменды, которую отслеживаем
  global flag
  flag = 'START'
  bot.send_message(message.chat.id, f'''Привет, {message.from_user.first_name}! Этот бот обеспечивает безопасность переписки.
По команде /how_is_it_work можно узнать необходимые подробности.''', parse_mode='html')
  
@bot.message_handler(commands=['how_is_it_work'])
def how_is_it_work(message):
  global flag
  flag = 'how_is_it_work'
  #bot_sh = '[Бот шифрования](https://t.me/LyamEncryptBot)'
  #bot_dsh = 
  bot.send_message(message.chat.id, f'''Бот "ЛямоШифрование" работает по уникальной системе шифрования сообщений, которая позволяет сделать переписку максимально безопасной.
  ________________________
\n\nПрежде, чем зашифровать сообщение, пользователю следует получить токен, введя команду /get_token. Обновлять токен можно неограниченное число раз, так как при создании нового удаляется старый. Поэтому <b>НЕ ХРАНИТЕ СВОИ ПАРОЛИ, ЗАШИФРОВАННЫМИ В ЭТОМ БОТЕ.</b>
\n\nПосле того, как токен получен, сообщение можно зашифровать, используя команду /encrypt.
\n<b>ВАЖНО!</b> Данная система шифрования уникальна и не имеет аналогов в мире. 
Но гарантия безопасности общения здесь влечет за собой ряд ограничений в оперировании символами. 
Чтобы система шифрования работала, важно соблюдать два правила:
1) Сообщение должно начинаться с двух или более валидных(шифруемых) символов из списка ниже (пробел является невалидным(нешифруемым) символом, поэтому сообщение не должно начинаться с одной буквы).\n
2) Помни, что шифруются только символы, представленные ниже, и в случаях особой секретности следует использовать только их:\n
['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н',
'о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','?','!']
\n\nЕсли пользователь желает расшифровать сообщение, нужно использовать команду /decrypt. К зашифрованному сообщению ему необходимо получить токен от пользователя, который это сообщение отправил
<b>Важно, чтобы зашифрованное сообщение было скопировано в абсолютной точности</b>''', parse_mode='html')

@bot.message_handler(commands=['get_token'])
def get_token(message):
  print('GET_TOKEN+')
  #ВНОШУ ФЛАГ
  global flag
  flag = 'GET_TOKEN'
  to_ken = '' #ПОЛУЧЕННЫЙ ТОКЕН
  #создаю токен и добавляю токен в список
  if message.text == '/get_token':
    #записываю словарь из файла в словарь tokens_dict
    tokens_dict = {}
    d_list = codecs.open('dicti.txt','r','utf-8')
    if not os.stat("dicti.txt").st_size == 0:
      d_list.close()
      d_list = codecs.open('dicti.txt','r','utf-8')
      tokens_dict = eval(d_list.read())
      d_list.close()
    #Записываю строки из файла в список
    f_list = codecs.open('keys_list.txt','r','utf-8')
    keys_list = []
    #print(f'До: {keys_list}')
    for s in f_list:
      s = s.rstrip()
      keys_list = keys_list + [s]
    f_list.close()
    #print(f'После: {keys_list}')

    print('Код сработал!')
    initial_length = len(keys_list)
    while True:
      to_ken = ''
      while not len(to_ken) == 100:
          let = choice(letters_in_name)
          to_ken += let
      if to_ken not in keys_list:
          keys_list.append(to_ken)
          if len(keys_list) == initial_length + 1:
            #Здесь перезаписываю список в файл
            f_list = codecs.open('keys_list.txt','w+','utf-8')
            for line in keys_list:
                f_list.write(str(line) + '\n')
            f_list.close()
            break

    #Прибавляю часть .txt для имени файла
    keys_file = to_ken + '.txt'
    #print(keys_file)

    #генерирую файл с ключами
    fp = codecs.open(keys_file,'a+','utf=8')
    keystr = []
    for i in range(71): #64 строки
      #while not len(keystr) == 100: #пока длина строки не станет 100, выполнять:
      for i in sample(keylist, 72):
          keystr.append(i) #добавляем случайный элемент в конец строки
      keys = str(keystr).replace('[','').replace(']','').replace(',','').replace('\'','').replace(' ','')
      fp.write(keys+'\n')
      keystr = []
    #while not len(keystr) == 100: #алгоритм для последней (64) строки
    for i in sample(keylist, 72):
      keystr.append(i)
    keys = str(keystr).replace('[','').replace(']','').replace(',','').replace('\'','').replace(' ','')
    fp.write(keys)
    fp.close()

    #print(f'КЛЮЧ ПОСЛЕ ГЕНЕРАЦИИ ФАЙЛА С КЛЮЧАМИ:{keys_list}')
    # если в словаре уже есть пользователь с таким id, то удаляю значение из списка и удаляю одноименный файл
    if message.from_user.id in tokens_dict:
      token_del = str((tokens_dict[message.from_user.id])).replace('[','').replace(']','').replace('\'','') #токен для удаления
      #print('Токен для удаления: ',token_del)
      #print(f'Список сейчас: {keys_list}')
      keys_list.remove(str(token_del)) #удаление из списка
      os.remove(token_del+'.txt') #удаление файла
      #ЗДЕСЬ ПЕРЕЗАПИСЬ СПИСКА В ФАЙЛ
      f_list = codecs.open('keys_list.txt','w+','utf-8')
      for line in keys_list:
        f_list.write(str(line) + '\n')
      f_list.close()

    #Бот отправляет сообщение с новым токеном
    bot.send_message(message.chat.id, f'Твой токен: <code>{to_ken}</code>', parse_mode='HTML')
    
    #Словарь пополняется ключом/значением
    tokens_dict[message.from_user.id] = [to_ken]
    #Перезаписываем словарь в файл
    d_list = codecs.open('dicti.txt','w+','utf-8')
    data = str(tokens_dict)
    d_list.write(data)
    d_list.close()

  #print(keys_list)
  #print(tokens_dict)
###################################################################################




  #ШИФРОВАНИЕ  
@bot.message_handler(commands=['encrypt'])
def encrypt(message):
    print('ENCRYPT+')
    global flag
    flag = 'ENCRYPT'
    #записываю словарь из файла в словарь tokens_dict, чтобы убедиться, что юзер есть в словаре
    tokens_dict = {}
    d_list = codecs.open('dicti.txt','r','utf-8')
    if not os.stat("dicti.txt").st_size == 0:
        d_list.close()
        d_list = codecs.open('dicti.txt','r','utf-8')
        tokens_dict = eval(d_list.read())
        d_list.close()
    if message.from_user.id in tokens_dict:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, введи сообщение, которое хочешь зашифровать')
        #encrypt(message)

    else: bot.send_message(message.chat.id, 'Токен еще не создан')



  #ДЕШИФРОВАНИЕ  
state = {}
@bot.message_handler(commands=['decrypt'])
def decrypt(message):
    print('DECRYPT')
    global flag
    flag = 'DECRYPT'
    #Записываю строки из файла в список
    f_list = codecs.open('keys_list.txt','r','utf-8')
    keys_list = []
    #print(f'До: {keys_list}')
    for s in f_list:
      s = s.rstrip()
      keys_list = keys_list + [s]
    f_list.close()
    print(f'keys_list после записи из файла: {keys_list}')

    state[message.chat.id] = 'waiting_for_token' #состояние ввода токена
    bot.send_message(message.chat.id, 'Отправь для расшифровки сообщения токен, который прислал тебе собеседник')
#  @bot.message_handler(content_types=['text'])
#  def handle_text_message(message):
    


@bot.message_handler(content_types=['text'])
def encrypt1(message):
    print('!!!')
    #записываю словарь из файла в словарь tokens_dict, чтобы записать обновленные токен и имя с ключами
    if flag == 'ENCRYPT':
        print('flag = ENCRYPT')
        tokens_dict = {}
        d_list = codecs.open('dicti.txt','r','utf-8')
        if not os.stat("dicti.txt").st_size == 0:
            d_list.close()
            d_list = codecs.open('dicti.txt','r','utf-8')
            tokens_dict = eval(d_list.read())
            d_list.close()
        keys_file_name = str((tokens_dict[message.from_user.id])).replace('[','').replace(']','').replace('\'','')+'.txt'
        fp = codecs.open(keys_file_name, 'r', 'utf-8')
        for i in range(72):
            if 0<=i<=17:
                f1 = fp.readline()
                mod1 = codecs.open('mod1.txt', 'a+', 'utf=8')
                mod1.write(str(f1))
                mod1.close()
            if 17<i<=35:
                f2 = fp.readline()
                mod2 = codecs.open('mod2.txt', 'a+', 'utf=8')
                mod2.write(str(f2))
                mod2.close()        
            if 35<i<=53:
                f3 = fp.readline()
                mod3 = codecs.open('mod3.txt', 'a+', 'utf=8')
                mod3.write(str(f3))
                mod3.close()   
            if 53<i<=71:
                f4 = fp.readline()
                mod4 = codecs.open('mod4.txt', 'a+', 'utf=8')
                mod4.write(str(f4))
                mod4.close()           
        fp.close() 

        #запись содержимых полученных файлов в переменные. Удаление файлов после записи
        def matrix_from_file(file_name):
            mod1 = codecs.open(file_name, 'r', 'utf=8')
            variable_save = mod1.read()
            mod1.close()
            os.remove(file_name)
            return variable_save
        matrix111 = matrix_from_file('mod1.txt')
        matrix222 = matrix_from_file('mod2.txt')
        matrix333 = matrix_from_file('mod3.txt')
        matrix444 = (matrix_from_file('mod4.txt')+'\n')

        #print(matrix111)

        #помещение полученных выше строк в матрицу
        def str_to_mtrx(matrix):
            temp = [matrix[idx: idx + 73] for idx in range(0, len(matrix), 73)]
            res = [list(ele) for ele in temp]
            return res

        #удаление последнего столбца ['\n'] из матрицы
        matrix11 = np.array(str_to_mtrx(matrix111))
        matrix1 = np.delete(matrix11, np.s_[-1:], axis=1)

        matrix22 = np.array(str_to_mtrx(matrix222))
        matrix2 = np.delete(matrix22, np.s_[-1:], axis=1)

        matrix33 = np.array(str_to_mtrx(matrix333))
        matrix3 = np.delete(matrix33, np.s_[-1:], axis=1)

        matrix44 = np.array(str_to_mtrx(matrix444))
        matrix4 = np.delete(matrix44, np.s_[-1:], axis=1)

        #print(matrix1)
        #print(matrix2)
        #print(matrix3)
        #print(matrix4)

        #ожидание ввода слова от пользователя и создание пустой строки для приема в нее зашифрованного слова
        w = (str(message.text)).lower()
        print(f'Отправленное сообщение: {w}')
        w1 = ''

        #определение, какая из четырех матриц будет использована, исходя из того, какой будет первая буква в слове
        if w[0] == 'а' or w[0] == 'д' or w[0] == 'з' or w[0] == 'л' or w[0] == 'п' or w[0] == 'у' or w[0] == 'ч' or w[0] == 'ы'or w[0] == 'я' or w[0] == 'd' or w[0] == 'h' or w[0] == 'l' or w[0] == 'p' or w[0] == 't' or w[0] == 'x' or w[0] == '1' or w[0] == '5' or w[0] == '9':
            m = matrix1
        elif w[0] == 'б' or w[0] == 'е' or w[0] == 'и' or w[0] == 'м' or w[0] == 'р' or w[0] == 'ф' or w[0] == 'ш' or w[0] == 'ь' or w[0] == 'a' or w[0] == 'e' or w[0] == 'i' or w[0] == 'm' or w[0] == 'q' or w[0] == 'u' or w[0] == 'y' or w[0] == '2' or w[0] == '6' or w[0] == '.':
            m = matrix2
        elif w[0] == 'в' or w[0] == 'ё' or w[0] == 'й' or w[0] == 'н' or w[0] == 'с' or w[0] == 'х' or w[0] == 'щ' or w[0] == 'э' or w[0] == 'b' or w[0] == 'f' or w[0] == 'j' or w[0] == 'n' or w[0] == 'r' or w[0] == 'v' or w[0] == 'z' or w[0] == '3' or w[0] == '7' or w[0] == '?':
            m = matrix3
        elif w[0] == 'г' or w[0] == 'ж' or w[0] == 'к' or w[0] == 'о' or w[0] == 'т' or w[0] == 'ц' or w[0] == 'ъ' or w[0] == 'ю' or w[0] == 'c' or w[0] == 'g' or w[0] == 'k' or w[0] == 'o' or w[0] == 's' or w[0] == 'w' or w[0] == '0' or w[0] == '4' or w[0] == '8' or w[0] == '!':
            m = matrix4
        #print(m)

        #шифровка
        try:
            print('!!!1111')
            if (w[0] in keylist) and(len(w)>1) and (w[1] in keylist):
                for i in range(18): #18 строк и 18 символов в каждом из списков k, т.к. в зависимости от второй буквы в слове выбираем нужную строчку
                    if w[1] == k1[i] or w[1] == k2[i] or w[1] == k3[i] or w[1] == k4[i]:   
                        for c in w:
                            for n in range(72): #72 символа в строке
                                #if (c == keylist[n]) and (w1.count(m[i][n])>=1) and (c != '!'):
                                    #c = [m[i][n+1]]
                                if (c == keylist[n]): #and (w1.count(m[i][n])<1):
                                    c = [m[i][n]]                 
                            w1 = (w1+str(c)).replace('[','').replace(']','').replace(',','').replace('\'','')
                        if m.all == matrix1.all:
                            w1 = (w1+str(1))
                        elif m.all == matrix2.all:
                            w1 = (w1+str(2))
                        elif m.all == matrix3.all:
                            w1 = (w1+str(3))
                        elif m.all == matrix4.all:
                            w1 = (w1+str(4))
                        if 0<=i<=9:
                            w1 = (w1+'0'+str(i+1))
                        elif 10<=i<=18:
                            w1 = (w1+str(i+1))
        except telebot.apihelper.ApiTelegramException:
            bot.send_message(message.chat.id, '''Уважаемый пользователь! Данная система шифрования уникальна и не имеет аналогов в мире. 
    Но гарантия безопасности общения здесь влечет за собой ряд ограничений в оперировании символами. 
    Чтобы система шифрования работала, важно соблюдать два правила:\n
    1) Сообщение должно начинаться с двух или более валидных символов из списка ниже (пробел является невалидным символом, поэтому Ваше сообщение не должно начинаться с одной буквы).\n
    2) Помнить, что шифруются только символы, представленные ниже, и в случаях особой секретности использовать только их:\n
    ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н',
    'о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.','?','!']''')
            return
        bot.send_message(message.chat.id, w1)
    elif flag == 'DECRYPT':
        to_list = []
        # Проверяем, находится ли пользователь в процессе ввода токена или сообщения для расшифровки
        if message.chat.id in state: 
            if state[message.chat.id] == 'waiting_for_token':# Если пользователь ожидает токен, проверяем его наличие в списке          
                to = message.text
                to_list += [to]
                #print(f'ПРОВЕРКА ФАЙЛА1 {to_list}')
                #ЗАПИСЬ to_list (токена) в файл для открытия файла с ключами ниже 
                f_list = codecs.open('one_key_dysc.txt','w','utf-8')
                f_list.write(str(to_list))
                f_list.close()

                ###------------------------ТЕСТОВАЯ ВСТАВКА----------------------------------
                f_list = codecs.open('keys_list.txt','r','utf-8')
                keys_list = []
                #print(f'До: {keys_list}')
                for s in f_list:
                    s = s.rstrip()
                    keys_list = keys_list + [s]
                f_list.close()

                if to not in keys_list:
                    bot.send_message(message.chat.id, 'Такого токена не существует')
                    print(f'ТОКЕНЫ В СПИСКЕ: {keys_list}')
                else: #Если токен найден, устанавливаем состояние в "ожидание сообщения для расшифровки"
                    state[message.chat.id] = 'waiting_for_message'
                    bot.send_message(message.chat.id, 'Отправь сообщение собеседника для расшифровки')
                    print(f'ТОКЕНЫ В СПИСКЕ: {keys_list}')
            elif state[message.chat.id] == 'waiting_for_message':
                me = message.text
                #######ЗАПИСЫВАЮ СПИСОК ИЗ ФАЙЛА В to_list
                f_list = codecs.open('one_key_dysc.txt','r','utf-8')
                to_list = []
                #print(f'До: {keys_list}')
                for s in f_list:
                    s = s.rstrip()
                    to_list = to_list + [s]
                f_list.close()
                #записываю введенный пользователем токен в переменную, чтобы потом использовать для открытия файла с ключами
                keys_file_name = (str(to_list)).replace('[','').replace(']','').replace('\'','').replace('\"','')+'.txt'
                print(f'ПРОВЕРКА ФАЙЛА {keys_file_name}')
                #Запись в отдельные файлы ключей из единого файла с ключами
                fp = codecs.open(keys_file_name, 'r', 'utf-8')
                for i in range(72):
                    if 0<=i<=17:
                        f1 = fp.readline()
                        mod1 = codecs.open('mod1.txt', 'a+', 'utf=8')
                        mod1.write(str(f1))
                        mod1.close()
                    if 17<i<=35:
                        f2 = fp.readline()
                        mod2 = codecs.open('mod2.txt', 'a+', 'utf=8')
                        mod2.write(str(f2))
                        mod2.close()        
                    if 35<i<=53:
                        f3 = fp.readline()
                        mod3 = codecs.open('mod3.txt', 'a+', 'utf=8')
                        mod3.write(str(f3))
                        mod3.close()   
                    if 53<i<=71:
                        f4 = fp.readline()
                        mod4 = codecs.open('mod4.txt', 'a+', 'utf=8')
                        mod4.write(str(f4))
                        mod4.close()           
                fp.close() 

                #запись содержимых полученных файлов в переменные. Удаление файлов после записи
                def matrix_from_file(file_name):
                    mod1 = codecs.open(file_name, 'r', 'utf=8')
                    variable_save = mod1.read()
                    mod1.close()
                    os.remove(file_name)
                    return variable_save
                matrix111 = matrix_from_file('mod1.txt')
                matrix222 = matrix_from_file('mod2.txt')
                matrix333 = matrix_from_file('mod3.txt')
                matrix444 = (matrix_from_file('mod4.txt')+'\n')

                #print(matrix111)

                #помещение полученных выше строк в матрицу
                def str_to_mtrx(matrix):
                    temp = [matrix[idx: idx + 73] for idx in range(0, len(matrix), 73)]
                    res = [list(ele) for ele in temp]
                    return res

                #удаление последнего столбца ['\n'] из матрицы
                matrix11 = np.array(str_to_mtrx(matrix111))
                matrix1 = np.delete(matrix11, np.s_[-1:], axis=1)

                matrix22 = np.array(str_to_mtrx(matrix222))
                matrix2 = np.delete(matrix22, np.s_[-1:], axis=1)

                matrix33 = np.array(str_to_mtrx(matrix333))
                matrix3 = np.delete(matrix33, np.s_[-1:], axis=1)

                matrix44 = np.array(str_to_mtrx(matrix444))
                matrix4 = np.delete(matrix44, np.s_[-1:], axis=1)

                #print(matrix1)
                #print(matrix2)
                #print(matrix3)
                #print(matrix4)

                #ожидание ввода слова от пользователя и создание пустой строки для приема в нее зашифрованного слова
                w = (str(me)).lower()
                w1 = ''

                #определение длины введенного слова
                kolvo = len(w)

                try:
                #Определение номера матрицы
                    if w[kolvo-3] == '1':
                        m1 = matrix1
                        #print('matrix1: ', m1)
                        #print(m1[17][71])
                    elif w[kolvo-3] == '2':
                        m1 = matrix2
                        #print('matrix2: ', m1)
                    elif w[kolvo-3] == '3':
                        m1 = matrix3
                        #print('matrix3: ', m1)
                    elif w[kolvo-3] == '4':
                        m1 = matrix4
                        #print('matrix4: ', m1)
                except IndexError:
                    bot.send_message(message.chat.id, 'В зашифрованном сообщении не может быть только одна буква!')   
                    return
                #дешифруем
                try:
                    for c in w[:-3]:
                        if c in m1:
                            m2 = m1[(int(w[kolvo-2]+w[kolvo-1])-1),:] #выделил список(ряд) в матрице
                            index = (list(m2)).index(c) #нашел индекс буквы в списке m2, выделенном из матрицы
                            c = keylist[index] #меняю значение буквы из введенного слова на букву из списка keylist с тем же индексом, что в матрице
                            w1 = (w1+str(c))
                        else:
                            w1 = (w1+str(c))
                except NameError:
                    bot.send_message(message.chat.id, 'Зашифрованное сообщение отправлено боту с ошибкой. Попробуйте скопировать сообщение еще раз и отправить снова!')
                    #bot.register_next_step_handler(message, decrypt)
                except IndexError:
                    bot.send_message(message.chat.id, 'Зашифрованное сообщение отправлено боту с ошибкой. Попробуйте скопировать сообщение еще раз и отправить снова!')
                #except apihelper.ApiTelegramException:
                #except Exception:
                    #bot.send_message(message.chat.id, 'Зашифрованное сообщение отправлено боту с ошибкой. Попробуйте скопировать сообщение еще раз и отправить снова!')    
                    return
                bot.send_message(message.chat.id, w1)

              
                #state.pop(message.chat.id)

            print(state)

bot.polling(non_stop=True)
