import matplotlib.pyplot as plt


def pie_chart():
    labels = ["A","B","C"]
    values = [300,45,105]

    fig,ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('piechart.png')
    plt.close()