import numpy as np
import matplotlib.pyplot as plt

#Definim dues funcions amb les modificacions que emprarem sovint a la representació gràfica

def style():
  plt.axvspan(0,0.365,facecolor='red',alpha=0.4)
  plt.axvspan(0.365,0.625,facecolor='green',alpha=0.4)
  plt.axvspan(0.625,1,facecolor='red',alpha=0.4)
  plt.axhspan(-10,0.020021,facecolor='white')
  plt.xlabel(r'$z/d$')
  plt.ylabel(r'$(T-T_0)\frac{2k}{V^2\sigma}$')
  plt.ylim(0,0.030)
  plt.xlim(0,1)
  plt.xticks(np.linspace(0,1,11))
  plt.legend()
def erstyle():
  plt.xlabel(r'$z/d$')
  plt.ylabel(r'$(T-T_{analítica})\frac{2k}{V^2\sigma}$')
  plt.xlim(0,1)
  plt.xticks(np.linspace(0,1,11))
  plt.legend()
  
  
  
  
 #Representació de la funció analítica amb error <1/1.000.000
  N=100                     #Nombre de talls que volem en z
tmax=0.025                #Temps que volem simulant
dz=1/N                    #Increment de z
z=np.linspace(0,1,N)      #Matriu de posicions z
F=np.zeros(N)             #Matriu on emmagatzemarem  els valors de T

for i in range(0,99):     #Loop corresponent al sumatori
  F=F+(4/np.pi**3)*np.sin((2*i+1)*np.pi*z)*(1-np.exp(-(2*i+1)**2*np.pi**2*tmax))/(2*i+1)**3
                          #^Terme i-éssim del sumatori
                          #Representem la funció.
plt.plot(z,F,color='black',label='Funció analítica')
style()
plt.text(0.02,0.028,'t='+str(tmax),bbox=dict(facecolor='white'))
plt.show()                #Assenyalem quin temps estem representant






#Euler Explícit
dt=0.25*(dz**2)           #Escollim el mallat
M=int(tmax/dt)+1          #Calculem el nombre de talls a t (+1 perquè un d'ells correspon a t=0)
T=np.zeros((N,M))         #Creem la matriu en què emmagatzemarem els valors de T

for j in range(0,M-1):    #Per a cada instant del mallat a partir de t=0
  for i in range(1,N-1):  #Per a cada posició en z
    T[i,j+1]=T[i,j]+(dt/dz**2)*(T[i+1,j]+T[i-1,j]-2*T[i,j])+dt
                          #^ Calculem la temperatura a l'instant següent segons l'equació discretitzada
T=np.transpose(T)         #Transposem la matriu per comoditat
                          #Representem la temperatura obtinguda a l'últim instant (l'última fila es M-1 pq la primera és 0!)
plt.plot(z,T[M-1],color='black',label='Resultat simulació')
style()
plt.text(0.02,0.028,'t='+str((M-1)*dt),bbox=dict(facecolor='white'))
plt.show()
                          #Representem la diferència entre el resultat analític i l'explícit (F-T)
plt.plot(z,F-T[M-1],color='black',label='Error')
erstyle()
plt.show()







#Euler Implícit (dt=dz)
tmax=0.030                #Canviem el temps màxim exclusivament per aquest mallat (millor arribar a 0.03 que quedar-se a 0.02)
dt=dz                     #Escollim el mallat

M=int(tmax/dt)+1          #Calculem el nombre de talls a t (+1 perquè un d'ells correspon a t=0)
T=np.zeros((N,M))         #Creem la matriu en què emmagatzemarem els valors de T

V=np.zeros(N)             #Definim un vector auxiliar en què realitzar els calculs sense modificar la matriu

for j in range(0,M-1):    #Per a cada instant de temps
  for k in range(0,1000): #Per a cada iteració
    for i in range(1,N-1):#Per a cada posició en z
      V[i]=(T[i,j]+(dt/dz**2)*(T[i+1,j+1]+T[i-1,j+1])+dt)/(1+2*dt/(dz**2))
                          #^ Calculem la següent iteració al vector auxiliar, i quan acabem
    T=np.transpose(T)   #Transposem per comoditat
    T[j+1]=V             #Substituim el vector al seu lloc corresponent
    T=np.transpose(T)   #Tornem a transposar

T=np.transpose(T)       #Transposem per comoditat
                          #Representem:
plt.plot(z,T[M-1],color='black',label='Resultat simulació')
style()
plt.text(0.02,0.028,'t='+str((M-1)*dt),bbox=dict(facecolor='white'))
plt.show()

plt.plot(z,F-T[M-1],color='black',label='Error')
erstyle()
plt.show()








#Euler Implícit (dt=0.5dz)
tmax=0.025                #Tornem al temps habitual
dt=0.5*dz                     #Escollim el mallat

M=int(tmax/dt)+1          #Calculem el nombre de talls a t (+1 perquè un d'ells correspon a t=0)
T=np.zeros((N,M))         #Creem la matriu en què emmagatzemarem els valors de T

V=np.zeros(N)             #Definim un vector auxiliar en què realitzar els calculs sense modificar la matriu

for j in range(0,M-1):    #Per a cada instant de temps
  for k in range(0,1000): #Per a cada iteració
    for i in range(1,N-1):#Per a cada posició en z
      V[i]=(T[i,j]+(dt/dz**2)*(T[i+1,j+1]+T[i-1,j+1])+dt)/(1+2*dt/(dz**2))
                          #^ Calculem la següent iteració al vector auxiliar, i quan acabem
    T=np.transpose(T)   #Transposem per comoditat
    T[j+1]=V             #Substituim el vector al seu lloc corresponent
    T=np.transpose(T)   #Tornem a transposar

T=np.transpose(T)       #Transposem per comoditat
                          #Representem:
plt.plot(z,T[M-1],color='black',label='Resultat simulació')
style()
plt.text(0.02,0.028,'t='+str((M-1)*dt),bbox=dict(facecolor='white'))
plt.show()

plt.plot(z,F-T[M-1],color='black',label='Error')
erstyle()
plt.show()







#Temps òptim
tmax=0                      #Comencem amb un ansatz del temps
E=1                         #I de l'ordre de magnitud de l'error que estem cometent
Tmax=0.020021+0.444*(np.heaviside(z-0.375,1)-np.heaviside(z-0.625,1))
                            #^ Construim una matriu amb els valors de temperatura que no s'han d'excedir

while E<10:                 #Mentre l'ordre de magnitud de lerror sigui <10
  tmax=tmax+10**(-E)        #Sumem 1 a la posició decimal E del temps estudiat
                            #Executem el mètode explícit:
  dt=0.25*(dz**2)
  M=int(tmax/dt)+1
  T3=np.zeros((N,M))
  for j in range(0,M-1):
    for i in range(1,N-1):
      T3[i,j+1]=T3[i,j]+(dt/dz**2)*(T3[i+1,j]+T3[i-1,j]-2*T3[i,j])+dt
  T3=np.transpose(T3)

  check=T3[M-1]>=Tmax       #Fem una matriu que es 1 si ens hem passat, 0 si no
  if np.amax(check)==1:     #Si ens hem passat,
    tmax=tmax-10**(-E)      #Fem un pas enrere
    E=E+1                   #Passem a la següent posició decimal
                            #Quan trobem el temps òptim, calculem per a aquest
                            #(cal tornar a calcular pq el valor al loop era havent-nos passat!)
M=int(tmax/dt)+1
T3=np.zeros((N,M))
for j in range(0,M-1):
  for i in range(1,N-1):
    T3[i,j+1]=T3[i,j]+(dt/dz**2)*(T3[i+1,j]+T3[i-1,j]-2*T3[i,j])+dt
                            #I representem
T3=np.transpose(T3)

plt.plot(z,T3[M-1],color='black',label='Resultat simulació')
style()
plt.text(0.02,0.028,'t='+str((M-1)*dt),bbox=dict(facecolor='white'))
plt.show()







