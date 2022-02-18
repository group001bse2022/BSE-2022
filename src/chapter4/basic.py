while true:
    data=input('Enter water units to buy:')
    try:
        water=float(data)
        print("units" , water +2)
    except ValueError:
