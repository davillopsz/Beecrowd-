# Uma das grandes áreas de estudo da Universidade do Sul é a Astrofísica Computacional. No mais recente trabalho em grupo, é preciso desvendar os mistérios de uma carta não muito conhecida, mas felizmente preservada pelo Museu de História da universidade:

# “27 de Abril de 1597

# Querido Galileu,

# Já faz um tempo que eu venho estudando alguns dos trabalhos de Nicolau Copérnico e eu encontrei uma anotação um tanto intrigante na margem de uma das últimas páginas do seu livro De revolutionibus orbium coelestium. Ele escreveu assim:

# Há uma quantidade enorme de corpos celestes exóticos orbitando o Sol, da mesma maneira que a Terra, e nós estamos em uma constante ameaça de colisão iminente. Tal evento poderia erradicar toda a vida em nosso planeta!

# Após ler tais palavras, eu comecei a tentar encontrar uma maneira de estimar a posição dos planetas ao longo do tempo. E eu consegui encontrar algumas fórmulas que podem ajudar! Mas ninguém acredita no modelo heliocêntrico, então eu tenho certeza que ninguém acreditará em nada disso também. Mas eu sei que você acredita. Você é o único que pode me ajudar agora, Galileu.

# Inicialmente, pode parecer que todo planeta percorre uma órbita circular ao redor do Sol. Mas como nos mostra a matemática, a nossa estrela é, na verdade, um dos focos da órbita elíptica que esses corpos descrevem (não se preocupe, como calcular essas anomalias angulares é parte da minha descoberta). Assim, eu nomeei periélio o ponto mais próximo que um objeto chega do Sol e afélio o mais distante. Sabendo essas duas coordenadas e o período orbital desses corpos, nós podemos seguir essas fórmulas e aproximar suas posições após um dado tempo desde o periélio! É bastante cálculo, mas eu sei que você é bom nisso e juntos nós podemos fazer isso tudo funcionar!

# Primeiramente, precisaremos da anomalia média M = n × t do corpo, onde t é a quantidade de dias desde o periélio e n é o seu deslocamento médio, dado por n = 2π / o. Aqui, o é o período orbital, também em dias, do corpo celeste. Depois disso, precisamos solucionar a equação para a qual eu carinhosamente dei meu nome (estou tendo bastante dificuldade em resolver essa, na verdade!): M = E − e × sen E, onde E é a anomalia excêntrica e e é a excentricidade da órbita. M é uma parametrização do tempo e E uma parametrização do ângulo polar. Essas anomalias relacionam-se com a posição em que o corpo estaria se ele tivesse uma órbita perfeitamente circular (bem excêntrico, mesmo)...

# De qualquer maneira, agora nós temos apenas que encontrar a distância r = a × (1 − e × cos E) do corpo até o Sol, sendo a o semieixo maior da órbita, e a anomalia verdadeira θ do corpo para obtermos sua coordenada polar (r, θ) em relação ao Sol. Para a anomalia verdadeira, temos que cos θ = (cos E − e) / (1 − e × cos E) e sen θ = (sen E × √(1 − e2)) / (1 − e × cos E).

# Bom... finalmente sabemos as coordenadas polares de cada planeta ao redor de nossa estrela e de um potencialmente catastrófico corpo celeste. O que nós queremos saber é se esse corpo está atualmente dentro ou sobre a fronteira de um triângulo formado por quaisquer outros três corpos do nosso Sistema Solar. O Sol e alguns dos nossos planetas são tão massivos que eles são capazes de alterar a órbita do corpo em questão e fazê-lo vir diretamente na nossa direção, se ele já não estava (ou mandá-lo para longe, mas quem é que garante?). Se ele estiver próximo o suficiente, estamos indiscutivelmente perdidos!

# Estou tão preocupado, Galileu... não queria que esse fosse o fim da linha para nós! O que podemos fazer, se isso é o que esse Mundi harmoniosamente caótico deseja? Se o pior acontecer, você passaria alguns dos seus últimos minutos comigo?

# Com amor, do sempre seu,
# Kepler”

# Entrada
# Várias linhas compõem um caso de teste. A primeira contém um inteiro k representando o número de planetas (2 ≤ k ≤ 105). As próximas k linhas contêm a descrição de cada planeta: quatro números de ponto flutuante que correspondem às distâncias do periélio dph e afélio daf em quilômetros do Sol, ao período orbital o em dias e ao tempo t desde o último periélio, também em dias (0 < dph ≤ daf ≤ 1010; 0 < o ≤ 105; 0 ≤ t < o), respectivamente. A última linha contém a descrição do temido corpo celeste, no mesmo formato que um planeta. Considere coplanares todos os objetos da entrada. Todos os números de ponto flutuante terão no máximo 8 casas decimais.

# Saída
# A saída deve ser uma única linha contendo “Certus, Kepler!” se Kepler e Galileu passaram seus últimos minutos juntos ou “Harmonicus nihilominus!” caso contrário (sem as aspas).

# Exemplo de Entrada	Exemplo de Saída
# 9
# 46001272.0 69817079.0 87.96926 14.2
# 107476000.0 108941850.0 224.7008 47.98
# 147098074.0 152097701.0 365.25636 115.23
# 206644545.0 249228730.0 686.97959 421.444449
# 740742600.0 816081460.0 4332.8201 2.1024
# 1349467000.0 1503983000.0 10755.699 10075
# 2735555030.0 3006389400.0 30687.153 27699.43434343
# 4459631500.0 4536874300.0 60190.03 60190
# 4420000000.0 7375927900.0 90553.017 73117.017
# 87661080.0 5248238950.0 27509.1291 0

# Exemplo de Saída

# Certus, Kepler!

import math

def calcula_anomalia_excentrica(M, e, precisao=1e-8):
    E = M  
    while True:
        E_prox = E - (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        if abs(E_prox - E) < precisao:
            break
        E = E_prox
    return E

def calcula_posicao(dph, daf, o, t):
    e = (daf - dph) / (daf + dph)
    a = (daf + dph) / 2
    
    n = 2 * math.pi / o
    M = n * t
    
    E = calcula_anomalia_excentrica(M, e)
    
    r = a * (1 - e * math.cos(E))
    
    cos_theta = (math.cos(E) - e) / (1 - e * math.cos(E))
    sin_theta = (math.sin(E) * math.sqrt(1 - e**2)) / (1 - e * math.cos(E))
    
    theta = math.atan2(sin_theta, cos_theta)
    
    return r, theta

def ponto_dentro_triangulo(xp, yp, x1, y1, x2, y2, x3, y3):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)
    
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(xp, yp, x2, y2, x3, y3)
    A2 = area(x1, y1, xp, yp, x3, y3)
    A3 = area(x1, y1, x2, y2, xp, yp)
    
    return A == A1 + A2 + A3

k = int(input())
planetas = []

for _ in range(k):
    dph, daf, o, t = map(float, input().split())
    planetas.append((dph, daf, o, t))

dph_c, daf_c, o_c, t_c = map(float, input().split())

r_c, theta_c = calcula_posicao(dph_c, daf_c, o_c, t_c)
x_c = r_c * math.cos(theta_c)
y_c = r_c * math.sin(theta_c)

encontrado = False

for i in range(k):
    for j in range(i+1, k):
        for l in range(j+1, k):

            r1, theta1 = calcula_posicao(*planetas[i])
            r2, theta2 = calcula_posicao(*planetas[j])
            r3, theta3 = calcula_posicao(*planetas[l])
            
            x1, y1 = r1 * math.cos(theta1), r1 * math.sin(theta1)
            x2, y2 = r2 * math.cos(theta2), r2 * math.sin(theta2)
            x3, y3 = r3 * math.cos(theta3), r3 * math.sin(theta3)
            
            if ponto_dentro_triangulo(x_c, y_c, x1, y1, x2, y2, x3, y3):
                encontrado = True
                break
        if encontrado:
            break
    if encontrado:
        break

if encontrado:
    print("Certus, Kepler!")
else:
    print("Harmonicus nihilominus!")
