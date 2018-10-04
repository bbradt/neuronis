import numpy as np

def sig_integrate_fire(f0, T, V_th=1, tau=1, E_L=1,
                             R_m=1, I_e=1, h=1):
    '''
        Simple leaky integrate and fire model. Perform Eulerian
        integration up to time T with step-size h.
    '''
    V = f0
    history = []
    spikes = []
    c = 0
    while np.sum(spikes) < T:
        history.append(V)
        c += 1
        V = V + (h/tau) * (-V + E_L + R_m*I_e)
        if V >= V_th:
            V = f0
            spikes.append(1)
            continue

    return V, history, spikes

def leaky_integrate_fire(f0, T, V_th=1, tau=1, E_L=1,
                             R_m=1, I_e=1, h=1):
    '''
        Simple leaky integrate and fire model. Perform Eulerian
        integration up to time T with step-size h.
    '''
    V = f0
    history = []
    spikes = []
    for t in np.arange(0, T, h):
        history.append(V)
        V = V + (h/tau) * (-V + E_L + R_m*I_e)
        if V >= V_th:
            V = f0
            spikes.append(1)
            continue
    return V, history, spikes

def integrate(f0, T, h=1, record=False):
    y = f0
    history = []
    for t in np.arange(0,T,h):
        if record:
            history.append(y)
        y = y + h*y
    if record:
        return y, history
    return y
