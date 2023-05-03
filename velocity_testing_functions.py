def plot_10_cycles(distance_data):
    data_in_order = [abs(i - distance_data[0]) for i in distance_data]   
    cycle1 = []
    cycle2 = []
    cycle3 = []
    cycle4 = []
    cycle5 = []
    cycle6 = []
    cycle7 = []
    cycle8 = []
    cycle9 = []
    cycle10 = []

    for i in data_in_order:
        if i < 10:
            cycle1.append(i)
        elif i < 20:
            cycle2.append(i)
        elif i < 30:
            cycle3.append(i)
        elif i < 40:
            cycle4.append(i)
        elif i < 50:
            cycle5.append(i)
        elif i < 60:
            cycle6.append(i)
        elif i < 70:
            cycle7.append(i)
        elif i < 80:
            cycle8.append(i)
        elif i < 90:
            cycle9.append(i)
        elif i < 100:
            cycle10.append(i)
        else:
            pass
        
    return [cycle1, cycle2, cycle3, cycle4, cycle5, cycle6, cycle7, cycle8, cycle9, cycle10]


def zero_cycle(cycle):
    return [i - cycle[0] for i in cycle]