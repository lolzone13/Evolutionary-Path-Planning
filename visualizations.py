from path_map import Path_Map


map = Path_Map()
ll = map.generate_map()


def visualize_map(path_string):
    loc = map.start
    x = loc[0]
    y = loc[1]
    ll[x][y] = '#'

    n = len(path_string)

    for i in path_string:
        if (i == 'U'):
            y-=1
        elif (i == 'R'):
            x+=1
        elif (i == 'L'):
            x-=1
        elif (i == 'D'):
            y+=1

        ll[x][y] = '#'
    

    for row in ll:
        st = ""
        print(st.join([str(ele) for ele in row]), end="\n")

    

# just print it normally