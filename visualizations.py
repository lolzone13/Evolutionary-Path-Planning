from path_map import Path_Map


map = Path_Map()
ll = map.generate_map()


def visualize_map(path_string):
    loc = map.start
    x = loc[0]
    y = loc[1]
    ll[x][y] = '#'


    for i in path_string:
        if (i == 'U'):
            if (x > 0):
                x-=1
        elif (i == 'R'):
            if (y < map.columns - 1):
                y+=1
        elif (i == 'L'):
            if (y > 0):
                y-=1
        elif (i == 'D'):
            
            if (x < map.rows - 1):
                x+=1
        if ([x, y] == map.end):
            ll[x][y] = 't'
            break
        
    

        ll[x][y] = '#'
    for row in ll:
        st = ""
        print(st.join([str(ele) for ele in row]), end="\n")

    

# just print it normally