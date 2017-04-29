import os
import matplotlib
import matplotlib.pyplot as plt
directories = [x for x in os.listdir(os.getcwd()) if (x[0] != '.') and (os.path.isdir(x))]

for i in directories:
    system = i[:2].replace('C', 'Cr').replace('M', 'Mn').replace('N', 'Ni').replace('F', 'Fe')
    eci_socket = open('./%s/eci.out' % i, 'rb')
    eci = [float(x)*1000 for x in eci_socket.read().rstrip().split('\n')[2:]]  # removing first two values because
                                                                          # they probably mean self-interation
    eci_socket.close()
    nbclusters_socket = open('./%s/nbclusters.in' % i, 'rb')
    nbclusters = [int(x) for x in nbclusters_socket.read().rstrip().split('\n')]
    nbclusters_socket.close()
    interaction = ['2N', '3N', '4N', '5N']

    font = {'family': 'sans',
            'size': 11}
    matplotlib.rc('font', **font)

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(7,3))
    ax1.bar([x + 1 for x in range(nbclusters[0])], eci[0:nbclusters[0]], hatch='x', capstyle='round', width=0.96, fill=False,
            edgecolor='black', zorder=2)
    # ax1.set_title('2-body')
    ax1.set_ylabel('ECI (J), meV')
    # ax2.set_title('3-body')
    ax2.bar([x + 1 for x in range(3)], [eci[-1], 0, 0], hatch='x', capstyle='round', width=0.96, fill=False,
            edgecolor='black', zorder=2)
    limit = max([abs(x) for x in eci])
    plt.ylim(-limit*1.1, limit*1.1)
    ax1.axhline(y=0, xmin=0, xmax=1, linewidth=1, color='black', zorder=1, linestyle='--')
    ax2.axhline(y=0, xmin=0, xmax=1, linewidth=1, color='black', zorder=1, linestyle='--')
    # plt.text(x=-1, y=0.5, s='ECI (J), meV', rotation='vertical')
    # plt.text(x=-0.5, y=limit, s='2-body')
    # plt.text(x=0.5, y=limit, s='3-body')
    plt.text(-0.45, limit*0.9, '2-body')
    plt.text(2.75, limit*0.9, '3-body')
    plt.text(0.5, limit*0.9, system)
    filename='./%s_eci_bars.png' % system
    plt.tight_layout(h_pad=0, w_pad=-0.5)

    # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    # plt.show()
    # break
    plt.savefig(filename, bbox_inches='tight')

