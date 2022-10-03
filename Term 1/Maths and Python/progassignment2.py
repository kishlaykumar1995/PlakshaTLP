import random
import matplotlib.pyplot as plt
import seaborn as sns

def find_minima():
    alpha=-10
    decrement=1.0

    d_alpha_1=50*(alpha)**2-142*(alpha)+101
    toggle=0

    while True:
        if toggle==0:
            alpha=alpha+decrement
        elif toggle==1:
            alpha=alpha-decrement
        
        d_alpha_2=50*(alpha)**2-142*(alpha)+101

        if d_alpha_1<d_alpha_2:
            decrement=decrement/2
            if toggle==1:
                toggle=0
            else:
                toggle=1
            
        if decrement<0.0001:
            break

        d_alpha_1 = d_alpha_2

    print(alpha)


def distribution_plot():
    plot_bucket = []
    for j in range(1000):                      # 1000 samples
        head_count = 0
        for i in range(1000):                   # 100 coin tosses
            head_count+=random.randint(0,1)    # Consider 1 as head and 0 as tails and count the number of heads
        plot_bucket.append(head_count)

    sns.set_style('darkgrid')
    sns.histplot(plot_bucket)
    plt.show()

find_minima()
distribution_plot()