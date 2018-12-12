
########################################
#
# Nome: Jeferson
# Matricula:
# E­mail:
#
# Nome: Lucas Brabec Barreto Santana
# Matricula: 201420014919
# E­mail: lucasbbs@dcomp.ufs.br
#
########################################

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import math

def nchannels(imagem):
    dimensoes = imagem.shape
    ultimo = len(dimensoes) - 1
    return dimensoes[ultimo]

# Questão 11 para RGB com falha
def hist(img, canais):
    color = ('b', 'g', 'r')
    for channel, col in enumerate(color):
        hist, bins = np.histogram(img, canais, None, 256, [0,256])
    return hist

# Questão 11 para escala de cinza OK!
def hist(img):
    hist, bins = np.histogram(img, 256, [0,256])
    return hist

# Questão 12
def showhist(hist):
    plt.hist(hist)
    plt.ylabel('No of times')
    plt.show()

# Questão 13
def showhist2(hist, bin=1):
    numero = math.trunc(bin)
    plt.hist(hist, bins = numero)
    plt.ylabel('No of times')
    plt.show()

def toRBG(image):
    return image[:,:,0:3]

def imread(nomeArquivo):
    imagem = plt.imread(nomeArquivo)
    if imagem.dtype == 'float32':
    	imagem.dtype = np.uint8
    	imagem * 255
    if nchannels(imagem) > 3: #trata caso em que imagens tem mais que 3 canais
        return toRBG(imagem)
    return imagem

def histeq(img, number_bins=256):
    histograma, bins = np.histogram(img.flatten(), number_bins)
    dist_cumulativa = histograma.cumsum()
    # normaliza
    dist_cumulativa = 255 * dist_cumulativa / dist_cumulativa[-1]
    img_equalizada = np.interp(img.flatten(), bins[:-1], dist_cumulativa)
    return img_equalizada.reshape(img.shape), dist_cumulativa

def convole(img, mask):
    return convolution

def maskBlur():
    return  np.array([[1/16, 2/16, 1/16], [2/16, 4/16, 2/16], [1/16, 2/16, 1/16]])

def convolve(img, mask):
    img_nova = img.reshape(img.shape[0], img.shape[1], 1)
    print(img_nova.shape)
    # return np.convolve(img, mask)


def blur(img):
    return convolve(img, maskBlur())

# showhist2(hist(),20.4)]
# print(maskBlur().shape)
# print(maskBlur().shape)
img = imread("h.png")
print(img.shape)
x = img.shape[0]
y = img.shape[1]
print(x, y)
img_nova = img.flatten()
convolve(img_nova, maskBlur())
# print(img_nova.shape)
# print(blur(img.reshape()))
# print(histeq(img))
# print(img.shape[2])
# print(convolve(img, maskBlur()))
