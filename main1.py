import matplotlib.pyplot as plt

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ax.scatter(x=[1, 2, 3], y=[3, 2, 1])
    plt.savefig('figure1.png')
    plt.show()

