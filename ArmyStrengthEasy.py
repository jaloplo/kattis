"""
Solution to the problem Army Strength (Easy) in Kattis web page.
Link: https://open.kattis.com/problems/armystrengtheasy
"""
import sys

def get_source():
    """Set the source as a file readed from the console or
    the user input."""
    if len(sys.argv) > 1:
        return open(sys.argv[1])
    else:
        return sys.stdin

def solution():
    """Solution to the problem."""
    source = get_source()
    results = []
    for test in range(int(source.readline())):
        source.readline() # blank line
        g_soldiers, m_soldiers = [int(n) for n in source.readline().split()]
        g_army = sorted([int(s) for s in source.readline().split()][0:g_soldiers], reverse=True)
        m_army = sorted([int(s) for s in source.readline().split()][0:m_soldiers], reverse=True)

        while len(g_army) > 0 and len(m_army) > 0:
            if g_army[-1] >= m_army[-1]:
                m_army.pop()
            else:
                g_army.pop()

        results.append('Godzilla' if len(g_army) > len(m_army) else 'MechaGodzilla' if len(m_army) > len(g_army) else 'uncertain')
    
    print '\n'.join(results)

if __name__ == '__main__':
    solution()
