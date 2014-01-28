import itertools
import matplotlib.pyplot as plt
from numpy import *
from pylab import *
from matplotlib import rc, rcParams
from matplotlib.pyplot import *
from lmfit import minimize, Parameters, Parameter, report_fit
import numpy as np  
from numpy import *
from pylab import *
import matplotlib.pyplot as mpl

rc('text', usetex=True)
rc('font', family='serif')
rc('font', serif='palatino')
rc('font', weight='medium')
rc('mathtext', default='sf')
rc("lines", markeredgewidth=2)
rc("lines", linewidth=3)
rc('axes', labelsize=18) #24
rc("axes", linewidth=2) #2)
rc('xtick', labelsize=14)
rc('ytick', labelsize=14)
rc('legend', fontsize=13) #16
rc('xtick.major', pad=8) #8)
rc('ytick.major', pad=8) #8)
rc('xtick.major', size=13)
rc('ytick.major', size=13)
rc('xtick.minor', size=7)
rc('ytick.minor', size=7)
rcParams['text.latex.preamble']=[r"\usepackage{color}"]
rcParams['text.latex.preamble']=[r"\usepackage{xcolor}"]
rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
# create data to be fitted

dat=np.loadtxt("/home/davidvartanyan/Desktop/ws5sigma.dat")
x= log(dat[:,1])
y= dat[:,7]


plot(x,y,'ro')

xlabel(r'log $\sigma_*/ \mathrm{km\, s}^{-1}$')
ylabel(r'log $M_{BH}/M_{\odot}$')

savefig('/home/davidvartanyan/Desktop/ws5afig.png')

show()

