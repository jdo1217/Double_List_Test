import sys
from double_list import Double_List
#from double_list import Linked_List as Double_List

def except_str(exception):
    t = str(type(exception))
    if t.startswith('<class'):
        return t[8:-2] + '(' + str(exception) + ')'
    else:
        return t + '(' + str(exception) + ')'

def main():
    yesNo = {True:'yes', False:'no'}

    try:
        empty_list = Double_List()
    except Exception as e:
        print('Double_List.__init__() raises exception:', e)
        print("Cannot proceed.")
        sys.exit()

    print( '-----------------' )
    print( 'Testing is_empty:' )
    try:
        print('() empty?', yesNo[empty_list.is_empty()])
    except Exception as e:
        print('is_empty() raised', except_str(e))

    try:
        evens = Double_List([2,4,6,8])
        print( evens, 'empty?', yesNo[evens.is_empty()])
    except Exception as e:
        print('(2, 4, 6, 8).is_empty() raised', except_str(e))

    print( '-----------------' )
    print( 'Testing __iter__:' )
    try:
        evens = Double_List([2,4,6,8])
        print( 'Even values:', list(evens.__iter__()))
    except Exception as e:
        print( '(2, 4, 6, 8).__iter__() raised', except_str(e))

    print( '-----------------' )
    print( 'Testing __reversed__:' )
    try:
        evens = Double_List([2,4,6,8])
        print('Even values:', list(evens.__reversed__()))
    except Exception as e:
        print('(2, 4, 6, 8).__reversed__() raised', except_str(e))

    print( '-----------------' )
    print( 'Testing add_front:' )
    try:
        evens.add_front(0)
        print('After adding 0 at front:', evens)
    except Exception as e:
        print('(2, 4, 6, 8).add_front(0) raised', except_str(e))

    try:
        empty_list.add_front(0)
        print('After adding 0 to front of empty list:', empty_list)
    except Exception as e:
        print('().add_front(0) raised', except_str(e))

    print( '-----------------' )
    print( 'Testing add_tail:' )
    try:
        evens = Double_List([2,4,6,8])
        evens.add_tail(10)
        print('After appending 10:', evens)
    except Exception as e:
        print('(2, 4, 6, 8).append(10) raised', except_str(e))

    try:
        empty_list = Double_List()
        empty_list.add_tail(10)
        print('After appending 10 to empty list:', empty_list)
    except Exception as e:
        print('().append(10) raised', except_str(e))

    print( '-----------------' )
    print( 'Testing __len__:' )
    try:
        evens = Double_List([2,4,6,8])
        print('Length should be 4:', len(evens) )
    except Exception as e:
        print('(2, 4, 6, 8).__len__() raised', except_str(e))

    try:
        empty_list = Double_List()
        print( 'Length of empty list should be 0:', len(empty_list) )
    except Exception as e:
        print('().__len__() raised', except_str(e))

    print( '-----------------' )
    print( 'Testing __setitem__:' )
    try:
        evens = Double_List([2,4,6,8])
        evens[2] = 60
        print( '3rd item should be 60:', evens)
    except Exception as e:
        print('(2, 4, 6, 8).__setitem__(2, 60) raised', except_str(e))

    """
    print( '-----------------' )
    print( 'Testing __delitem__:' )
    try:
        evens = Double_List([2,4,6,8])
        del evens[2]
        print( 'after deleting 2th item should be (2, 4, 8):', evens )
    except Exception as e:
        print('(2, 4, 6, 8).__delitem__(2) raised', except_str(e))

    try:
        del evens[2]
        print( 'after deleting tail item should be (2, 4):', evens )
    except Exception as e:
        print('(2, 4, 8).__delitem__(2) raised', except_str(e))
    """

    print( '-----------------' )
    print( 'Testing __str__:' )
    try:
        evens = Double_List([2,4,6,8])
        print( 'str([2,4,6,8]) is:', evens )
    except Exception as e:
        print('(2, 4, 6, 8).__str__() raised', except_str(e))

    try:
        empty_list = Double_List()
        print( 'str([]) is:', empty_list)
    except Exception as e:
        print('().__str__() raised', except_str(e))

    print( '-----------------' )
    print( 'Testing __repr__:' )
    try:
        evens = Double_List([2,4,6,8])
        print( 'repr([2,4,6,8]) is:', repr(evens))
    except Exception as e:
        print('(2, 4, 6, 8).__repr__() raised', except_str(e))

if __name__ == '__main__':
    main()
