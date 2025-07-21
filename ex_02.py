def my_create_map(*arrays):
    dic={}
    for array in arrays:
        if len(array)<2:
            print ("The given argulents aren't valid")
            return None
        else:
            dic[array[0]]=array[1]
    return dic
