import sys

class List_Node:
    def __init__(self,
                 value = None,
                 next = None,
                 prev = None):
        self._value = value
        self._next  = next
        self._prev = prev

    def __str__(self):
        return '(' + str(self._value) + ')'

    def __repr__(self):
        result = '('
        if self._prev == None:
            result += 'None'
        else:
            result += str(id(self._prev)) + ' <- '
        result += '(@' + str(id(self)) + ' ' + repr(self._value) + ') -> '
        if self._next == None:
            result += 'None)'
        else:
            result += str(id(self._next))
            result += ')'
        return result

class Double_List:

    class List_Node:
        def __init__(self,
                     value = None,
                     next = None,
                     prev = None):
            self._value = value
            self._next  = next
            self._prev = prev

        def __str__(self):
            return '(' + str(self._value) + ')'

        def __repr__(self):
            result = '('
            if self._prev == None:
                result += 'None <- '
            else:
                result += str(id(self._prev)) + ' <- '
            result += '(@' + str(id(self)) + ' ' + repr(self._value) + ') -> '
            if self._next == None:
                result += 'None)'
            else:
                result += str(id(self._next))
                result += ')'
            return result

    def __init__(self, orig = None):
        self._head = self.List_Node()
        self._tail = self.List_Node()
        self._head._next = self._tail
        self._tail._prev = self._head
        if orig != None:
            for x in orig:
                self.add_tail(x)

    def copy(self, other):
        if type(other) == Double_List:
            return Double_List(other)
        else:
            raise TypeError

    def __iter__(self):
        current = self._head._next
        while current != self._tail:
            yield current._value
            current = current._next

    def __reversed__(self):
        current = self._tail._prev
        while current != self._head:
            yield current._value
            current = current._prev

    def is_empty(self):
        if self._head._next == self._tail:
            return True
        return False

    def __add__(self, other_list):
                result = Double_List()
                for x in self:
                    result.add_tail(x)
                for x in other_list:
                    result.add_tail(x)
                return result

    def add_front(self, value):
        x = self.List_Node(value)
        x._prev = self._head
        x._next = self._head._next
        self._head._next = x
        x._next._prev = x

    def add_tail(self, value):
        x = self.List_Node(value)
        x._prev = self._tail._prev
        x._next = self._tail
        self._tail._prev = x
        x._prev._next = x

    def insert(self, value, index):
        if type(index) != int:
            raise TypeError
        elif index > len(self):
            raise IndexError
        elif index == 0:
            self.add_front(value)
        elif index == len(self):
            self.add_tail(value)
        else:
            prev = self._head
            for i in range (index):
                prev = prev._next
            new_node = self.List_Node(value, prev._next)
            prev._next = new_node

    def __len__(self):
        current = self._head._next
        count = 0
        while current != self._tail:
            count += 1
            current = current._next
        return count

    def __setitem__(self, index, value):
        if type(index) != int:
            raise TypeError
        elif 0 <= index and index < len(self):
            current = self._head
            for i in range(index):
                current = current._next
            current._value = value
        else:
            raise IndexError

    def __getitem__(self, index):
        if type(index) != int:
            raise TypeError
        elif 0 <= index and index < len(self):
            current = self._head._next
            for i in range(index):
                current = current._next
            return current._value
        else:
            raise IndexError

    def __delitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError
        else:
            if index == 0:
                victim = self._head
                self._head = self._head._next
                del victim
            else:
                prev = self._head
                for x in range(index - 1):
                    prev = prev._next
                victim = prev._next
                prev._next = victim._next
                del victim

    def __str__(self):
        result = '('
        current = self._head._next
        while current != self._tail:
            result += str(current._value)
            current = current._next
            if current != self._tail:
                result += ', '
        result += ')'
        return result

    def __repr__(self):
        prev_nodes = set()
        result = 'Linked_List(\n'
        current = self._head
        while current != None:
            prev_nodes.add(current)
            result += '  ' + repr(current)
            if current == self._head:
                result += ' == head'
            if current == self._tail:
                result += ' == tail'
            result += '\n'
            if current._next in prev_nodes:
                print ('ERROR: circular reference in node:',repr(current))
                break
            else:
                current = current._next
        result += ')'
        return result
