from math import sqrt

# Variáveis gerais
pos = []              # Lista que salva as posições da bola
robo_x = float(input("Digite uma coordenada de x para o robô: "))
robo_y = float(input("Digite uma coordenada de y para o robô: "))
robo_x_i = robo_x     # Pos. do robô em x inicial (não se altera)
robo_y_i = robo_y     # Pos. do robô em y inicial (não se altera)
distancia = 1000000   # Distância genérica para futuro cálculo, sempre conseguir calcular menor distancia.
velocidade_x = 0      # Vel. do robô em x
velocidade_y = 0      # Vel. do robô em y
aceleracao = 2.3      # Aceleração do robô
raio = 0.1227         # Raio de interceptação
x_certo = False       # Variável para saber se chegou ao destino (x).
y_certo = False       # Variável para saber se chegou ao destino (y).

# Variáveis para o aprofundamento 1
aceleracoes_x = [0]   # Lista com as acelerações em x ponto-a-ponto.
aceleracoes_y = [0]   # Lista com as acelerações em y ponto-a-ponto.
velocidades_x = [0]   # Lista com as velocidades em x ponto-a-ponto.
velocidades_y = [0]   # Lista com as velocidades em y ponto-a-ponto.

# Variáveis para o gráfico 1
pos_robo_x = []       # Lista com as pos. do robô em x ponto-a-ponto.
pos_robo_y = []       # Lista com as pos. do robô em y ponto-a-ponto.
pos_bola_x = []       # Lista com as pos. da bola em x ponto-a-ponto.
pos_bola_y = []       # Lista com as pos. da bola em y ponto-a-ponto.

# Variáveis para o gráfico 2
tempos = []

# Variáveis para o gráfico 3
velocidades_bola = []

# Variáveis para o gráfico 4
aceleracoes_bola = []

# Variáveis para o gráfico 5
distancias = []

def roboFora():
  """Verifica se o robô está fora do campo, caso esteja, solicita uma coordenada válida."""
  global robo_x, robo_y, robo_x_i, robo_y_i
  while robo_x > 9 or robo_x < 0 or robo_y > 6 or robo_y < 0:
    robo_x = float(input("Digite uma coordenada válida de x para o robô: "))
    robo_y = float(input("Digite uma coordenada válida de y para o robô: "))
  robo_x_i = robo_x
  robo_y_i = robo_y

def saiuDoCampo():
  """Verifica se a bola saiu do campo, caso verdadeiro, retorna True."""
  global bola_x, bola_y
  if bola_x > 9 or bola_x < 0 or bola_y > 6 or bola_y < 0:
    return True

def calcDistancia(pos):
  """Recebe a lista de posições da bola e calcula a menor distância entre o robô e a bola."""
  global distancia, menor_pos, bola_x, bola_y, tempo_gasto, robo_x, robo_y
  for i in range(len(pos)):
    tempo = pos[i][0]
    bola_x = pos[i][1]
    bola_y = pos[i][2] 
    if (saiuDoCampo()):
      break
    else:
      conta_distancia = sqrt((bola_x - robo_x)**2 + (bola_y - robo_y)**2)
      if (conta_distancia < distancia and tempo >= 1):
        menor_pos = []
        menor_pos.append(tempo)
        menor_pos.append(bola_x)
        menor_pos.append(bola_y)
        distancia = conta_distancia
  print("Posiçao inicial do robô em X: %.2f metros\nPosiçao inicial do robô em Y: %.2f metros\n"% (robo_x, robo_y))
  print("--------------------------------------")
  print("Menor posiçao da bola relativa ao robô:")
  print("--------------------------------------")
  print("Menor posiçao da bola em X: %.2f metros\nMenor posiçao da bola em Y: %.2f metros\n"% (menor_pos[1], menor_pos[2]))

def moverRobo(menor_pos):
  """Recebe a menor posição calculada e move o robô até ela."""
  global robo_x, robo_y, velocidade_x, velocidade_y, aceleracao, x_certo, y_certo, raio, pos_robo_x, pos_robo_y
  contador_x = 0
  contador_y = 0
  if (menor_pos[1] > robo_x + raio and x_certo == False):
    while (robo_x + raio < menor_pos[1]):
      # Velocidade instantânea
      contador_x += 1
      aceleracao = 2.3
      velocidade_x = velocidade_x + (aceleracao * 0.02)
      robo_x = robo_x + velocidade_x * 0.02 + (aceleracao*0.02**2)/2
      aceleracoes_x.append(aceleracao)
      velocidades_x.append(velocidade_x)
      pos_robo_x.append(robo_x)
      pos_robo_y.append(robo_y)
    x_certo = True

  if (menor_pos[1] < robo_x - raio and x_certo == False):
    while (robo_x - raio > menor_pos[1]):
      # Velocidade instantânea
      contador_x += 1
      aceleracao = -2.3
      velocidade_x = velocidade_x + (aceleracao * 0.02)
      robo_x = robo_x + velocidade_x * 0.02 + ((aceleracao)*0.02**2)/2
      aceleracoes_x.append(aceleracao)
      velocidades_x.append(velocidade_x)
      pos_robo_x.append(robo_x)
      pos_robo_y.append(robo_y)
    x_certo = True
      
  if(menor_pos[2] > robo_y + raio and y_certo == False):    
    while (robo_y + raio < menor_pos[2]):
      # Velocidade instantânea
      contador_y += 1
      aceleracao = 2.3
      velocidade_y = velocidade_y + (aceleracao * 0.02)
      robo_y = robo_y + velocidade_y * 0.02 + (aceleracao*0.02**2)/2
      aceleracoes_y.append(aceleracao)
      velocidades_y.append(velocidade_y)
      pos_robo_x.append(robo_x)
      pos_robo_y.append(robo_y)
    y_certo = True

  if (menor_pos[2] < robo_y - raio and y_certo == False):
    while (robo_y - raio > menor_pos[2]):
      # Velocidade instantânea
      contador_y += 1
      aceleracao = -2.3
      velocidade_y = velocidade_y + (aceleracao * 0.02)
      robo_y = robo_y + velocidade_y * 0.02 + (aceleracao*0.02**2)/2
      aceleracoes_y.append(aceleracao)
      velocidades_y.append(velocidade_y)
      pos_robo_x.append(robo_x)
      pos_robo_y.append(robo_y)
    y_certo = True
  tempo_gasto = abs(contador_x*0.02 + contador_y*0.02)
  print("---------------- O robô achou a Bola !!! ---------------- \n\nPosiçao do robô em X no encontro com a bola: %.2f metros\nPosiçao do robô em Y no encontro com a bola %.2f metros\nTempo de chegada do robô nas coordenadas: %.2f segundos\n" % (robo_x, robo_y, tempo_gasto))

# Faz a leitura do arquivo e salva as posições na lista 'pos'
with open("trajetoria.dat", "r") as f:
  for p in f.readlines():
    l = []
    for k in p.replace(",", ".").split():
      try:
        l.append(float(k))
      except:
        l.append(k)
    pos.append(l)
pos.pop(0) # Exclui a 1a linha do arquivo

roboFora()
calcDistancia(pos)
moverRobo(menor_pos)

print()
import apf4
apf4.moverRobo(menor_pos, robo_x_i, robo_y_i)
print("\n")

while (len(aceleracoes_x) < len(aceleracoes_y)):
  aceleracoes_x.append(0)
while (len(aceleracoes_x) > len(aceleracoes_y)):
  aceleracoes_y.append(0)
while (len(velocidades_x) < len(velocidades_y)):
  velocidades_x.append(0)
while (len(velocidades_x) > len(velocidades_y)):
  velocidades_y.append(0)

if (aceleracoes_x[-1] != 0 or aceleracoes_y[-1] != 0):
  aceleracoes_x.append(0)
  aceleracoes_y.append(0)
if (velocidades_x[-1] != 0 or velocidades_y[-1] != 0):
  velocidades_x.append(0)
  velocidades_y.append(0)

#---------------- MatPlotLib ----------------#
print("---------------- Aprofundamento 1 ----------------\nIntroduzir vetores que representam a velocidade e a aceleração do robô e da bola no gráfico das trajetórias de seu programa\n\n--> Para este aprofundamento, criamos dois gráficos, um para a velocidade, e um para a aceleração.\n")

import matplotlib.pyplot as plt

# Gráfico apf1: velocidades
plt.plot(velocidades_x, linewidth=2.0, color="blue")
plt.plot(velocidades_y, linewidth=2.0, color="red")
plt.title("Gráfico de Velocidades em X e Y")
plt.xlabel("Velocidade (m/s)")
plt.ylabel("Variação em relação à velocidade inicial (m/s)")
plt.legend(['Velocidade_x = azul', 'Velocidade_y = vermelho'], bbox_to_anchor=(0, 0), loc='upper left')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.savefig("grafico_apf_1_velocidades.png")
plt.close()

# Gráfico apf1: acelerações
plt.plot(aceleracoes_x, linewidth=2.0, color="blue")
plt.plot(aceleracoes_y, linewidth=2.0, color="red")
plt.title("Gráfico de Acelerações em X e Y")
plt.xlabel("Aceleração (m/s)")
plt.ylabel("Variação em relação à aceleração inicial (m/s)")
plt.legend(['Aceleracao_x = azul', 'Aceleracao_y = vermelho'], bbox_to_anchor=(0, 0), loc='upper left')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.savefig("grafico_apf_1_aceleracoes.png")
plt.close()
 
def preencherPosBola(menor_pos, pos):
  """Preenche a lista de posições da bola que é utilizada pelo gráfico 1."""
  global pos_bola_x, pos_bola_y
  i = 0
  while pos[i][0] <= menor_pos[0]:
    tempos.append(pos[i][0])
    pos_bola_x.append(pos[i][1])
    pos_bola_y.append(pos[i][2])
    i += 1

preencherPosBola(menor_pos, pos)

def igualaTamanho():
  global pos_robo_x, pos_robo_y, pos_bola_x, pos_bola_y, robo_x, robo_y
  while len(pos_robo_x) < len(pos_bola_x):
    pos_robo_x.append(robo_x)
  while len(pos_robo_y) < len(pos_bola_y):
    pos_robo_y.append(robo_y)
  while len(pos_bola_x) < len(pos_robo_x):
    pos_bola_x.append(pos_bola_x[-1])
  while len(pos_bola_y) < len(pos_robo_y):
    pos_bola_y.append(pos_bola_y[-1])
  
def igualaTamanhoVelo():
  global velocidades_x, velocidades_y, tempos
  while len(velocidades_x) < len(tempos):
    velocidades_x.append(0)
  while len(velocidades_y) < len(tempos):
    velocidades_y.append(0)

def igualaTamanhoDistancias():
  global velocidades_x, velocidades_y, distancias
  while len(distancias) < len(velocidades_x):
    distancias.append(0)
  while len(distancias) < len(velocidades_y):
    distancias.append(0)

def igualaTamanhoAcele():
  global aceleracoes_x, aceleracoes_y, tempos
  while len(aceleracoes_x) < len(tempos):
    aceleracoes_x.append(0)
  while len(aceleracoes_y) < len(tempos):
    aceleracoes_y.append(0)

def igualaTamanhoTempos():
  global aceleracoes_x, aceleracoes_y, tempos
  while len(tempos) < len(aceleracoes_x):
    tempos.append(tempos[-1])
  while len(tempos) < len(aceleracoes_y):
    tempos.append(tempos[-1])

def igualaTamanhoVeloPos():
  global velocidades_x, velocidades_y, pos_robo_x, pos_robo_y, pos_bola_x, pos_bola_y
  while len(pos_robo_x) < len(velocidades_x):
    pos_robo_x.append(pos_robo_x[-1])
  while len(pos_robo_y) < len(velocidades_y):
    pos_robo_y.append(pos_robo_y[-1])
  while len(pos_bola_x) < len(velocidades_x):
    pos_bola_x.append(pos_bola_x[-1])
  while len(pos_bola_y) < len(velocidades_y):
    pos_bola_y.append(pos_bola_y[-1])

def igualaDistTempo():
  global distancias, tempos
  while len(tempos) < len(distancias):
    tempos.append(float(tempos[-1])+float(0.02))

def igualaVeloTempo():
  global velocidades_x, velocidades_y, tempos
  while len(velocidades_x) < len(tempos):
    velocidades_x.append(0)
  while len(velocidades_y) < len(tempos):
    velocidades_y.append(0)

def igualaAceleTempo():
  global aceleracoes_x, aceleracoes_y, tempos
  while len(aceleracoes_x) < len(tempos):
    aceleracoes_x.append(0)
  while len(aceleracoes_y) < len(tempos):
    aceleracoes_y.append(0)

igualaTamanho()
igualaTamanhoVelo()
igualaTamanhoAcele()
igualaTamanhoTempos()
igualaTamanhoVeloPos()

def calcDistanciaPontoaPonto(pos_bola_x, pos_bola_y, pos_robo_x, pos_robo_y):
  global distancias
  for i in range(len(pos_bola_x)):
    distancia = sqrt((pos_bola_x[i] - pos_robo_x[i])**2 + (pos_bola_y[i] - pos_robo_y[i])**2)
    distancias.append(distancia)

calcDistanciaPontoaPonto(pos_bola_x, pos_bola_y, pos_robo_x, pos_robo_y)

def calcVelocidadeAceleracao(tempos, distancias, velocidades_bola, aceleracoes_bola):
  for i in range(len(distancias)):
    if (i == len(distancias)-1 or i == 0):
      velocidades_bola.append(0)
    else:
      if tempos[i] == 0:
        velocidade = (distancias[i+1] - distancias[i])
        velocidades_bola.append(velocidade)
      else:
        velocidade = (distancias[i+1] - distancias[i]) / (tempos[i+1]-tempos[i])
        velocidades_bola.append(velocidade)
  for i in range(len(velocidades_bola)):
    if (i == len(velocidades_bola)-1 or i == 0):
      aceleracoes_bola.append(0)
    else:
      if tempos[i] == 0:
        aceleracao = (velocidades_bola[i+1] - velocidades_bola[i])
        aceleracoes_bola.append(aceleracao)
      else:
        aceleracao = (velocidades_bola[i+1] - velocidades_bola[i]) / (tempos[i+1]-tempos[i])
        aceleracoes_bola.append(aceleracao)

igualaDistTempo()
igualaVeloTempo()
igualaAceleTempo()
calcVelocidadeAceleracao(tempos, distancias, velocidades_bola, aceleracoes_bola)
igualaTamanhoDistancias()

#---------------- Parte Obrigatória dos gráficos ----------------#

# Gráfico 1: trajetórias do robô (x,y)
plt.plot(pos_robo_x, pos_robo_y, linewidth=2.0, color="blue")
plt.plot(pos_bola_x, pos_bola_y, linewidth=2.0, color="red")
plt.title("Trajetória do robô e da bola até o ponto de interceptação")
plt.xlabel("Pos. em x (m)")
plt.ylabel("Pos. em y (m)")
plt.legend(['Posicao_robo = azul', 'Posicao_bola = vermelho'], bbox_to_anchor=(0.5, 0), loc=3)
plt.savefig("grafico_1.png")
plt.close()

# Gráfico 2: Pos. do robô e da bola x Tempo
plt.plot(tempos, pos_bola_x)
plt.plot(tempos, pos_bola_y)
plt.plot(tempos, pos_robo_x)
plt.plot(tempos, pos_robo_y)
plt.title("Pos. do robô e da bola     x      Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.legend(['Posicao_x_bola = azul', 'Posicao_y_bola = laranja', 'Posicao_x_robo = verde ', 'Posicao_y_robo = vermelho'], bbox_to_anchor=(0.5, 0), loc=3)
plt.savefig("grafico_2.png")
plt.close()

# Gráfico 3: Velocidades do robô e da bola x Tempo
plt.plot(tempos, velocidades_x)
plt.plot(tempos, velocidades_y)
plt.plot(tempos, velocidades_bola)
plt.title("Velocidades do robô e da bola     x     Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.legend(['Velocidade_robo_x = azul', 'Velocidade_robo_y = laranja', 'Velocidade_bola = verde'], bbox_to_anchor=(0.5, 0), loc=3)
plt.savefig("grafico_3.png")
plt.close()

# Gráfico 4: Acelerações do robô e da bola x Tempo
plt.plot(tempos, aceleracoes_x)
plt.plot(tempos, aceleracoes_y)
plt.plot(tempos, aceleracoes_bola)
plt.title("Acelerações do robô e da bola     x     Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleracao (m/s²)")
plt.legend(['Aceleracao_robo_x = azul', 'Aceleracao_robo_y = laranja', 'Aceleracao_bola = verde'], bbox_to_anchor=(0.5, 0), loc=3)
plt.savefig("grafico_4.png")
plt.close()

# Gráfico 5: Distância relativa entre o robô e bola x Tempo
plt.plot(tempos, distancias)
plt.title("Distância relativa entre o robô e bola   x   Tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Distância (m)")
plt.legend(['Distancia D = azul'], bbox_to_anchor=(0.5, 0), loc=3)
plt.savefig("grafico_5.png")
plt.close()
