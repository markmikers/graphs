import os
import matplotlib
import matplotlib.pyplot as plt

directories = [x for x in os.listdir(os.getcwd()) if os.path.isdir(x) and (x[0] != '.')]
for directory in directories:
    system = directory[:2].replace('C', 'Cr').replace('M', 'Mn').replace('N', 'Ni').replace('F', 'Fe')
    fit_socket = open('./%s/fit.out' % directory)
    fit = [x.split(' ') for x in fit_socket.read().rstrip().split('\n')]
    for i in range(len(fit)):
        for j in range(len(fit[i])):
            fit[i][j] = float(fit[i][j])
    fit.sort(key=lambda x: x[-1])
    x = [k[-1] for k in fit]
    y = [k[3]*1000 for k in fit]
    z = [float(k[0]) for k in fit]

    font = {'family': 'sans',
            'size': 12}
    matplotlib.rc('font', **font)
    f, ax = plt.subplots(1,1,figsize=(7,3))
    ax.axhline(y=0, linewidth=1, color='gray', zorder=2)
    # plt.scatter(x,y,marker='x', zorder=3)
    ax.minorticks_on()
    ax.grid(which='major', color='lightgray', linestyle='--', linewidth=1, zorder=1)
    ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=1, zorder=1)
    cm = plt.cm.get_cmap('gnuplot')
    sc = plt.scatter(x, y, marker='x', c=z, s=35, cmap=cm, zorder=3)
    plt.ylabel('Eform difference, meV')
    plt.xlabel('Number of the structure')
    plt.text(x=x[-1]*1.07,y=max(y)*0.95,s='Concentration of %s' % system[:2],rotation='vertical')
    plt.text(x=0,y=max(y)*0.95,s=system)
    plt.colorbar(sc)
    plt.tight_layout()
    filename = './%s_fit_resid.png' % system
    # plt.show()
    # break
    plt.savefig(filename, bbox_inches='tight')