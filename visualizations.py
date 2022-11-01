from path_map import Path_Map


map = Path_Map()
ll = map.generate_map()
for i in range(map.rows):
    
    for j in range(map.columns):
        print(ll[i][j], end=" ")
    

# just print it normally