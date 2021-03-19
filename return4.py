def menu(day):
    if day=="Monday":
        return "butter chicken"
    elif day=="Tuesday":
        return "chole bhature"
    else:
        return "mutton chaap"
    print("kya main print ho payungi")
mon_menu=menu("Monday")
print(mon_menu)
tues_menu=menu("Tuesday")
print(tues_menu)
fri_menu=menu("friday")
print(fri_menu)