from pathlib import Path
from sys import path
from typing import Self, Dict

class HTMLTag:

    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = '', **kwargs: Dict[str, str]):
        self.name = name
        self.value = value
        self.attributes = kwargs
        self.__nested: list[HTMLTag] = []

    def nested(self, html_tag: Self):
        self.__nested.append(html_tag)

    def __str(self, indent_level: int) -> str:
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        result = f"{margin}<{self.name}"
        if self.attributes:
            for attr, value in self.attributes.items():
                result += f' {attr}="{value}"'
        result += f">{self.value}"
        if self.__nested:
            for tag in self.__nested:
                result += '\n' + tag.__str(indent_level + 1)
            eol = f'\n{margin}'
        result += f"{eol}</{self.name}>"
        return result

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name: str, value: str = '', **kwargs: Dict[str, str]) -> 'HTMLBuilder':
        return HTMLBuilder(name, value, **kwargs)


class HTMLBuilder:

    def __init__(self, root: HTMLTag | str, value: str = '', *, parent: Self = None, **kwargs: Dict[str, str]):
        if isinstance(root, HTMLTag):
            pass
        elif isinstance(root, str):
            root = HTMLTag(root, value, **kwargs)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')
        self.root: HTMLTag = root
        self.__parent: Self = parent

    def nested(self, name: str, value: str = '', **kwargs: Dict[str, str]) -> Self:
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested(tag)
        return HTMLBuilder(tag, parent=self)

    def sibling(self, name: str, value: str = '', **kwargs: Dict[str, str]) -> Self:
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested(tag)
        return self

    def build(self) -> HTMLTag:
        if self.__parent is None:
            return self.root
        else:
            return self.__parent.build()

# ### HTLM билдер###
# builder = HTMLBuilder('html')
# ### Добавляем хэд-тэг и название страницы###
# head = builder.nested('head')
# head.nested('title', 'Сайт "УРА- новости".')
# ### Добавляем хэддер и заголовок###
# body = builder.nested('body')
# header = body.nested('header')
# header.nested('h1', 'Новости сегодня.')
# ### Основное тело (тэг body и контент)###
# main = body.nested('main')
# main.nested('h3', 'Майкл Джордан приехал с гастролями в Россию.')
# main.nested('p', 'Выступление Майкла пройдет...')
# main.nested('h3', 'Новый способ лечения облысения ладоней.')
# main.nested('p', 'Пригодится простой советский....')
# ### Добавляем футтер тэг###
# footer = body.nested('footer')
# footer.nested('p', '© 2021 Ура-новости')
# html_tag = builder.build()
# html_string = str(html_tag)
# print(html_string)