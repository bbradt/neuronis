import numpy as np
import euler as e
import seaborn as sb
import matplotlib.pyplot as plt

def plot_integrate():
    '''
        Test the Integrate Method from Euler PYX.

    '''
    T=4
    H=0.0001

    y, history = e.integrate(1, T, h=H, record=True)
    gt = np.exp(T)
    plt.plot(history)
    plt.plot([0,len(history)], [gt, gt],'b--')
    plt.errorbar(len(history), y,gt-y)
    plt.text(len(history)/2,y/2, "Error=%.2f" % (gt-y))
    plt.show()

def plot_leaky_integrate():
    '''Test the Leaky Integrate and Fire Model'''
    E_L = -65
    R_m = 90
    I_e = 1
    V_th = -50
    tau = 30
    V_0 = -65
    H = 0.0001
    T = 10000

    y, history = e.leaky_integrate_fire(V_0, T, V_th=V_th, tau=tau, E_L=E_L,
                                R_m=R_m, I_e=I_e, h=H, record=True)
    plt.plot(history)
    plt.show()

def plot_leaky_rate():
    '''And then compute the firing rate for a number of repeats'''
    E_L = -65
    R_m = 90
    I_e = 1
    V_th = -50
    tau = 30
    V_0 = -65
    H = .01
    T = 500
    I_e_min = 0
    I_e_max = 2
    I_e_rate = 0.1
    r_isi = []
    t_s = []
    g_s = []

    for I_e in np.arange(I_e_min, I_e_max, I_e_rate):
        if R_m*I_e <= V_th - E_L:
            r_isi.append(0)
            g_s.append(0)
            t_s.append(0)
            continue
        guess = 1/(tau*np.log((R_m*I_e+E_L-V_0)/(R_m*I_e+E_L-V_th)))
        g_s.append(guess)
        y, history, spikes = e.sig_integrate_fire(V_0, T, V_th=V_th, tau=tau, E_L=E_L,
                                R_m=R_m, I_e=I_e, h=H)
        t_isi = len(history)/np.sum(spikes)

        print(I_e, guess, np.sum(spikes), 1/t_isi, t_isi)
        if t_isi > 0:
            r_isi.append(1/t_isi)
        else:
            r_isi.append(0)
    # Renormalize
    r_isi = np.array(r_isi)/H
    plt.plot(np.arange(I_e_min, I_e_max, I_e_rate), np.array(r_isi))
    plt.plot(np.arange(I_e_min, I_e_max, I_e_rate), g_s, 'b--')
    plt.show()

if __name__=='__main__':
    plot_leaky_rate()