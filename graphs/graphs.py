import matplotlib.pyplot as plt
f = open("priceCMShops.txt", "r")
prices = {'Taiwangun': [], 'Gunfire': [], 'Azteko': [], 'Redberet': [], 'Taniemilitaria': []}
colors = {'Taiwangun': 'black', 'Gunfire': '#f35500', 'Azteko': '#99840e', 'Redberet': 'red', 'Taniemilitaria': 'green'}
if f:
    i = 1
    dates = []
    for line in f:
        if i in range(1, 500, 6):
            x = line[0:19]
            dates.append(x)
            i += 1
        elif i in range(2, 500, 6):
            prices['Taiwangun'].append(float(line[15:21]))
            i += 1
        elif i in range(3, 500, 6):
            prices['Gunfire'].append(float(line[15:21]))
            i += 1
        elif i in range(4, 500, 6):
            prices['Azteko'].append(float(line[15:21]))
            i += 1
        elif i in range(5, 500, 6):
            prices['Redberet'].append(float(line[15:21]))
            i += 1
        elif i in range(6, 500, 6):
            prices['Taniemilitaria'].append(float(line[15:21]))
            i += 1

    for key in prices:
        plt.plot(dates, prices[key], label=key, color=colors[key])
        plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Product')
    plt.legend()
    plt.tight_layout()
    plt.savefig('Product.pdf')


else:
    print("No file")
