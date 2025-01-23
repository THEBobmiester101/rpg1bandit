from .item import Item
from .greatSword import GreatSword
from inspect import signature


class ItemOwner:

    items: list[Item] = []


    @staticmethod
    def item_callback(func):

        def item_wrapped_func(self, *args):
            relevant_items = [i for i in self.items if func.__name__ in i.callbacks]

            for it in relevant_items:
                args = (it.callbacks[func.__name__](self, *args),)
                if it.used_up:
                    self.remove_item(it)

            ret = func(self, *args) if len(signature(func).parameters) > 1 else func(self)
            return ret
        
        return item_wrapped_func


    def add_item(self, item: Item):
        if 'add_item' in item.callbacks:
            item.callbacks['add_item'](self)
        self.items.append(item)
        

    def remove_item(self, item: Item):
        if 'remove_item' in item.callbacks:
            item.callbacks['remove_item'](self)
        self.items.remove(item)
