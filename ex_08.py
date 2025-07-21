def my_order_class_name(*objs):
    ty_liste=[]
    type_dic={}
    li_fin=[]
    for obj in objs:
        ty_liste.append(type(obj).__name__)
    for typ in ty_liste:
        if len(typ) in type_dic:
            type_dic[len(typ)].append(typ)
        else:
            type_dic[len(typ)]=[]
            type_dic[len(typ)].append(typ)
    for key in type_dic:
        type_dic[key].sort(key=str.lower)
        type_dic[key]=list(dict.fromkeys(type_dic[key]))
        li_fin.append(type_dic[key])
    li_fin.sort(key=len)
    return li_fin

class MyClass: pass
args = [True, 76, False, 12.5, "Coucou !", [1,2,3], MyClass(), None]
print(my_order_class_name(*args))
