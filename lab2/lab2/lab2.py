import unittest

from domain.HashTable import HashTable

if __name__ == '__main__':
    st = HashTable(5)
    st.add('dsf')
    st.add('dsffsad')
    st.add('dfs')
    st.add('fsd')
    st.add('dsfsdrklf')
    st.add('dsffkld')
    st.add('dsfklrr')

    st.remove('dfs')
    print(st)
    print(st.getPos('dfs'))