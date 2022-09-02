import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio

path = 'C:/Users/HP/PycharmProjects/SignalProcess/MatFiles/CAS_S500Y_3.mat'


def spec(x):
    s = sio.loadmat(x)
    sig = s[list(s.keys())[3]]
    print(sig.shape)
    data = np.zeros((229, 1606))
    for i in range(sig.shape[1]):
        s = sig[:, i]
        f, t, z = signal.stft(s, noverlap=1, nperseg=10)
        data[:, i] = np.mean(z, axis=0)
    return data


S = spec(path)
print(S.shape)
plt.figure()
plt.imshow(S)
plt.axis('off')
plt.show()


