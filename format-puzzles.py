text_test = '''
Beginner 1
29
2glns9
2g gl

Beginner 2
1z
1blmnxz
1b lm nx

Beginner 3
cx
fpcrix
fp cr pr

Beginner 4
49
4afcrse9
4r af ce

Beginner 5
uy
fpugrijty
pu pr

Beginner 6
56
5fkumeot6
5u ku km

Beginner 7
38
3kugvhrdseo8
3k ku uv vg

Beginner 8
4d
4kuqhwdnjt
4q qt tj

Beginner 9
1z
1aglvcwdnsyz
1a ac

Beginner 10
5z
5fuqhrjyz
5u fu fh hr

Intermediate 11
28
2fpcrweo8
2f fp cr eo

Intermediate 12
29
2akgvwins9
2g gv vw

Intermediate 13
fx
fblqhrdnxjt
fh ln qr

Intermediate 14
cw
gqcmwsejt
cm qs ej

Intermediate 15
47
4fpbqhret7
4p fp et

Intermediate 16
39
3publhrnxejy9
3l be ej

Intermediate 17
3z
3apcmwdsz
3m ac cm ps

Intermediate 18
27
2fugqhwit7
2f fu uw

Intermediate 19
bx
3bgvhmsxet7z
bg 3m h7

Intermediate 20
58
5fkpmrwixj8
kp 5w rw

Advanced 21
26
2fpucmwdoty6
2f fp uw

Advanced 22
Bu
Kubqhrnet78
Bq qr hr h7 78 8n

Advanced 23
A9
3agqmwdsjy689
Ad qs jy 68

Advanced 24
4z
4apgqcmwjoz
4p ac gq gj

Advanced 25
38
3fulqhmsxet8
3l lq qs st et

Advanced 26
Ae
Apgvmisxet78z
Ap i7 m8 st xz

Advanced 27
38
3akubqhrwnjy8
3k ak hr jy

Advanced 28
Ay
Apublymdsy689v
Ap uv s9

Advanced 29
B8
134fubqmisxeo8
34 fu be qs mo

Advanced 30
48
4fublqmwisejy8
4q lm be ij

Expert 31
Cw
124kpgcmwsjo69
1c kp gj s9

Expert 32
27
24akugvcrdnxjt7
2g 4r uv dn

Expert 33
49
4afbqhwdnxjt9
Af 4q bq nx

Expert 34
15
15fubqcmwisot7z
1b bq qs ot wz

Expert 35
Cy
134fugqcrinjy68
C6 68 8n ni ij

Expert 36
3 7
135fubqcmwixet7
13 bq ce et xw

Expert 37
17
1235fublhwdseoy7
1b 23 hw ds eo

Expert 38
18
145fkugqcrwnjy8
1c fk 4q gJ wy

Expert 39
48
4akbqmwdixjt8
4q qt jt ij

Expert 40
U6
234akubgqcmrixot69
Ak gi ux ot qr
'''

'''
Field:
6789z
ejoty
dinsx
chmrw
bglqv
afkpu
12345
'''


charmap = '6789zejotydinsxchmrwbglqvafkpu12345'


def conv_letter_to_coord(c):
    # print(c)
    i = charmap.index(c.lower())
    return i % 5, i // 5


def read(text):
    res = []
    puzzle = []
    for line in text.split('\n'):
        if not line:
            if puzzle:
                res.append(puzzle)
                puzzle = []
            continue

        if not puzzle:
            puzzle.append(line)
            continue

        st = [conv_letter_to_coord(c) for c in line if c != ' ']
        puzzle.append(st)

    if puzzle:
        res.append(puzzle)

    return res


print(read(text_test))


def get_positions(start, finish, nodes, planks):
    max_x = max(x[0] for x in nodes)
    max_y = max(x[1] for x in nodes)
    start_finish = str(max_x+1)+ str(max_y+1) + str(start[0])+str(start[1])+str(finish[0])+str(finish[1])
    planks = [str(a[0])+str(a[1]) for a in planks]

    return start_finish + ''.join(planks)


def get_nodes(nodes):

    print(nodes)

    max_y = max(x[1] for x in nodes)

    lines = [[] for _ in range(max_y+1)]

    for node in nodes:
        lines[node[1]].append(node[0])

    res = []
    for i, line in enumerate(lines):
        res.append(len(line))
        for j in line:
            res.append(j)

    return ''.join(str(a) for a in res)


def conv(text):
    m = read(text)[1:]
    res = ['Planks format 1']
    start, finish = m[0]
    res.append("Positions = \"" + get_positions(start, finish, m[1], m[2]) + "\"")

    res.append("Nodes = \"" + get_nodes(m[1]) + "\"")

    return '\n'.join(res)


# <x-plank-puzzle name='Beginner 1' fmt='1' positions = "750163011111212151" nodes = '040125214412560'></x-plank-puzzle>
def conv_arr(text):
    puzzles = read(text)

    res = []
    for m in puzzles:
        name = m[0]
        start, finish = m[1]
        positions = get_positions(start, finish, m[2], m[3])
        nodes = get_nodes(m[2])
        puzzle_str = f'<x-plank-puzzle name="{name}" fmt="1" positions = "{positions}" nodes = "{nodes}"></x-plank-puzzle>'
        res.append(puzzle_str)


    return '\n'.join(res)


print(conv_arr(text_test))

