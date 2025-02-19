# class Button:
#
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
# home = Button('Домой', '/home')
# catalog_msk = Button('Каталог', '/msk/catalog')
#
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку' + home.link)
#
# print('\n')
#
# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку' + catalog_msk.link)
#
#
#
# class Button2:
#
#
#     def __init__(self, text, link, loc):
#         self.text = text
#         self.link = link
#         self.loc = loc
#
#     def click(self):
#         return 'Клик по локатору - {}'.format(self.loc)
#
#
# home_two = Button2('Домой', '/home', 'buttom#home')
#
# print(home_two.click())


class Input:


    def __init__(self,text, loc):
        self.text = text
        self.loc = loc

class Button:


    def __init__(self,text, loc):
        self.text = text
        self.loc = loc

class Title:


    def __init__(self,text, loc):
        self.text = text
        self.loc = loc


class Link:


    def __init__(self,text, loc):
        self.text = text
        self.loc = loc


output = Input('Сообщение', 'input#output')
click = Button('Кнопка', 'button#click')
subtitle = Title('Заголовок', 'title#subtitle')
home = Link('Домой', 'link#home')

print(output.text + ' ' + output.loc)
print(click.text + ' ' + click.loc)
print(subtitle.text + ' ' + subtitle.loc)
print(home.text + ' ' + home.loc)



