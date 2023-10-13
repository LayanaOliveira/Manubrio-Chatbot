import pandas as pd
import telebot
import numpy as np

ChaveAPI = '6222617519:AAETPKInm5xP-oJwLETLFyH0CcClKEkwY_E'
bot = telebot.TeleBot(ChaveAPI)
#ALTURA E PESO - CADASTRO

@bot.message_handler(commands='Cadastro')
def altura(mensagem):
    bot.send_message(mensagem.chat.id, "📏 Informe sua altura em metros, como no exemplo: 1.76")
    bot.register_next_step_handler(mensagem, registroAltura)

def registroAltura(mensagem):
    global alt
    alt = float(mensagem.text)
    bot.reply_to(mensagem, 'A sua altura foi registrada! Agora, informe seu peso ⚖️ como no exemplo: 60')
    bot.register_next_step_handler(mensagem, registroPeso)
    
    
#CALCULO DO IMC

def registroPeso(mensagem):
    global pes
    pes = float(mensagem.text)
    imc = pes / (alt ** 2)
    
    if imc < 18.5:
        situaçao = 'Magreza'
    elif 18.5 <= imc < 25:
        situaçao = 'Peso normal'
    elif 25 <= imc < 30:
        situaçao = 'Sobrepeso'
    elif 30 <= imc < 35:
        situaçao = 'Obesidade grau 1'
    elif 35 <= imc < 40:
        situaçao = 'Obesidade Severa'
    else:
        situaçao = 'Obesidade Mórbida'
    
    bot.reply_to(mensagem, f'''Excelente 😃! O resultado do seu imc é %.1f, o que significa: {situaçao}. 
    
    O que você deseja fazer agora:
    🍎 Qual a minha /Dieta adequada?
    🤸‍♀️ Quais /Exercicios devo praticar?
    
Além disso, você pode descobrir como sua /Saude_Mental é afetada através do seu estilo de vida.
    '''%(imc))    
    

#DIETA

@bot.message_handler(commands=['Dieta'])
def dieta(mensagem):
    bot.reply_to(mensagem, '''Para isso, é necessário que você selecione a sua situação descrita no item anterior:
    
    /Magreza
    /Normal
    /Sobrepeso
    /Obesidade_grau_1
    /Obesidade_Severa
    /Obesidade_Morbida
    
    /MENU_INICIAL''')

@bot.message_handler(commands=['Magreza'])
def magreza(mensagem):
    bot.reply_to(mensagem, '''
Engordar de forma saudável é mais do que apenas comer mais alimentos ou ingerir alimentos com muitas calorias. A seguir, temos algumas dicas para te ajudar nesse processo:
    

    •Nunca pule refeições: faça ao menos 6 refeições fracionadas ao longo do dia

    •Não se entupir de besteiras: evite alimentos industrializados e fast foods, além de darem a sensação de estufamento, não contribuem para a nutrição

    •Não consumir bebidas alcoólicas com frequência

    •Inclua oleaginosas na dieta: amêndoas, castanhas e nozes são lanches práticos, boas fontes de gordura e com alto valor nutritivo

    •Preste atenção no preparo dos alimentos: dê preferência à alimentos frescos e preparados da maneira mais natural possível, evite frituras e processados

    •Consumir bastante água.
    
    /MENU_INICIAL
    ''')
    
@bot.message_handler(commands=['Normal'])
def normal(mensagem):
    bot.reply_to(mensagem, '''Alimentos indicados para o manter o peso ideal:

Bons carboidratos a serem incluídos tanto nas dietas de perda quanto nas de ganho de peso devem sempre equilibrar quantidades e valores calóricos adequados para cada pessoa e seus objetivos físicos. Dê preferência às fontes de vitaminas, minerais e fibras. Veja uma lista dos alimentos indicados para esse processo:
- Carnes Magras: Frango, peixe (assados, cozidos, grelhados).

- Ovos (sem óleo) e leguminosas (feijões).

- Leite e seus derivados (queijo branco, iogurte).

- Bons carboidratos: Arroz integral, batata doce, inhame, pão integral, tapioca.

- Vegetais crus (no mínimo 3 tipos).

- Vegetais cozidos (1 a 2 tipos diferentes).

- Frutas (em torno de 2 a 3 porções/ unidades, ao dia. Dê preferência às frutas da estação).

- Boas gorduras: Azeite e castanhas.


/MENU_INICIAL

''')

@bot.message_handler(commands=['Sobrepeso'])
def sobrepeso(mensagem):
    bot.reply_to(mensagem, ''' Combine uma alimentação equilibrada, composta por alimentos frescos e naturais. Sempre opte por alimentos obtidos diretamente de plantas ou de animais ou então aqueles que foram submetidos a processos que não envolvam agregação de sal, açúcar, óleos, gorduras ou outras substâncias como: 
    -verduras
    -frutas
    -legumes
    -leite,
    -iogurte natural
    -feijões
    -cereais
    -raízes
    -tubérculos
    -ovos
    -castanhas
    -frutas secas
    -sucos naturais
    -chá, café e água potável. 
Controle o consumo de alimentos de origem animal. Utilize óleos, gorduras, sal e açúcar em pequenas quantidades.

Isso vai colaborar com o funcionamento intestinal, prevenir a obesidade e outras doenças, além de ajudar na perda e manutenção de peso saudável.
    
    
/MENU_INICIAL''')

@bot.message_handler(commands=['Obesidade_grau_1'])
def obesidade(mensagem):
    bot.reply_to(mensagem, '''
    7 dicas de ouro para tratar e prevenir a obesidade
VARIAR: sempre os alimentos;
EVITAR: alimentos ricos em gordura;
INGERIR: alimentos ricos em fibras;
EVITAR: o consumo de refrigerantes;
EVITAR: consumo de bebidas alcoólicas (OBS: o álcool é um dos componentes mais calóricos de qualquer dieta, com 7 calorias para cada grama, perdendo apenas para as gorduras, que contém 9 calorias por grama, enquanto proteínas e carboidratos contém 4 calorias por grama);
COMER: em horários regulares (pelo menos 3 a 4 refeições ao dia);
REALIZAR: atividades físicas regularmente, sempre que possível com a orientação de profissionais capacitados, como fisioterapeutas e educadores físicos.
    
    
/MENU_INICIAL''')
    
@bot.message_handler(commands=['Obesidade_Severa'])
def severa(mensagem):
    bot.reply_to(mensagem, '''
    
A dieta deve ser personalizada, de modo a abranger todas as necessidades e dificuldades do indivíduo, de acordo com seu peso, sua idade, suas comorbidades e suas atividades físicas e diárias. É importante lembrar que nem toda dieta que funciona bem para uma pessoa vai funcionar para as outras, cada organismo é único e responde de formas diferentes a um mesmo estímulo. Geralmente, é rica em fibras e proteínas, enquanto limita a ingestão de carboidratos refinados e gorduras saturadas. Alimentos recomendados incluem:

- frutas
- legumes
- verduras
- feijões
- cereais integrais
- carnes magras
- ovos
- laticínios com baixo teor de gordura
- nozes
- sementes.

No entanto, é importante limitar o consumo de carboidratos refinados, como açúcar branco e pão branco. As recomendações gerais para controlar a obesidade de grau 2 incluem uma combinação de dieta saudável, atividade física regular, redução do estresse e, se necessário, tratamento medicamentoso ou cirurgia bariátrica. É importante procurar a orientação nutricional realizada por um profissional especializado e capacitado, preferencialmente um nutricionista ou um médico especializado nesta área. Ele pode ajudar a desenvolver um plano de alimentação personalizado e fornecer suporte contínuo para o controle do peso a longo prazo. O acompanhamento nutricional deve ser frequente e a dieta deve ser revisada conforme necessário.
    
    
/MENU_INICIAL''')
    
@bot.message_handler(commands=['Obesidade_Morbida'])
def morbida(mensagem):
    bot.reply_to(mensagem, '''
    Dentre as diversas formas de orientação dietética, a mais aceita cientificamente é a dieta hipocalórica balanceada, na qual o paciente receberá uma dieta calculada com quantidades calóricas dependentes de sua atividade física.
    
-› Não são recomendadas dietas muito restritas (com menos de 800 calorias, por exemplo), já que são restrições drásticas que tem pequena aderência do paciente e de difícil manutenção em longo prazo.

-› Dietas somente com alguns alimentos (dieta do abacaxi, por exemplo) ou somente com líquidos (dieta da água) também não são recomendadas, por apresentarem vários problemas. Dietas com excesso de gordura e proteína também são bastante discutíveis, uma vez que pioram as alterações de gordura do paciente além de aumentarem a deposição de gordura no fígado e outros órgãos.

-› Estabelecer um consumo diário de água com média de 3L/dia.

É de extrema necessidade consultar um profissional nutricionista para que o preocesso ocorra de maneira saudável.

/MENU_INICIAL
    ''')

    
    
#EXERCICIOS

@bot.message_handler(commands=['Exercicios'])
def exercicios(mensagem):
    bot.reply_to(mensagem, '''Primeiro, qual objetivo você deseja alcançar?
    🏃 /Perder peso
    🤸‍♂️ /Manter o peso
    🏋 /Ganhar massa muscular
    
    
    /MENU_INICIAL
    ''')

@bot.message_handler(commands=['Perder'])
def perder(mensagem):
    bot.reply_to(mensagem, ''''
PERDER MASSA 

Para emagrecer, é necessário que se entre em déficit calórico, ou seja, você deve gastar mais calorias do que ingere no dia.
A seguir, temos algumas práticas selecionadas para você alcalçar seu objetivo:

    Musculação
    proporciona um aumento da massa muscular, da resistência, da força e da flexibilidade, ela contribui  para a perda de peso, pois quanto maior a massa muscular, maior é a capacidade da pessoa de gastar calorias, inclusive em repouso.
    
    Aeróbico continuo
    Andar de bicicleta é um ótimo exercícios aeróbico para quem quer emagrecer
    
    Pular corda
    A corda é um exercício intenso e de fácil execução, podendo ser realizado em qualquer lugar. O ideal é que você faça o máximo de repetições que conseguir para aumentar o gasto calorico

    
    /MENU_INICIAL''')
    
@bot.message_handler(commands=['Manter'])
def manter(mensagem):
    bot.reply_to(mensagem, '''
EXERCÍCIOS PARA MANTER O PESO

Para manter o peso é importante manter uma dieta balanceada, não basta apenas a prática de exercícios. Como também  devem ser avaliados peso, idade, composição corporal, presença de doenças e/ou comorbidades. Mas lembre-se cada corpo é único com necessidades únicas, sempre consulte um especialista antes de realizar qualquer atividade física ou dieta.   

1. Ioga e Pilates
A flexibilidade e o equilíbrio são os principais benefícios destas práticas, além de que procuram igualmente a harmonia entre o aspeto físico e o mental. Ajudam no alívio das dores, fortalecem os músculos, aumentam a flexibilidade e diminuem o stress.

2. Caminhadas
É a atividade física que pode começar a fazer já. Uma hora por dia é suficiente para diminuir os riscos de doenças cardiovasculares, melhorar a coordenação motora e dar início a uma alteração de hábitos de vida sedentários para outros mais saudáveis.

3. Minigolfe
Sendo um exercício em que o peso do corpo é suportado na totalidade, é excelente para a saúde dos músculos e dos ossos. Sabe-se que este tipo de exercício regular ajuda a promover a manutenção da massa isenta de gordura (músculos), que ajuda a suportar um esqueleto forte. Este tipo de exercício físico ajuda, também, a prevenir a degeneração da massa óssea, incluindo a osteoporose.
    
/MENU_INICIAL''')

@bot.message_handler(commands=['Ganhar'])
def ganhar(mensagem):
    bot.reply_to(mensagem, '''
GANHAR MASSA MUSCULAR

O segredo está em aumentar de peso através do ganho de massa muscular. Para isso, é necessário praticar exercícios físicos que provoquem um grande esforço e desgaste do músculo. Veja a seguir alguns exemplos de exercícios, Mas lembre se cada corpo é único com necessidades únicas, sempre consulte um especialista antes de realizar qualquer atividade física.

1. Agachamento
Considerado um dos exercícios de maior poder em gerar ganho de massa muscular, o agachamento é o principal exercício para membros inferiores, sendo quadríceps e glúteo os principais músculos recrutados. 
2. Levantamento terra
Os principais músculos trabalhados neste exercício são os isquiotibiais e glúteos, porém latíssimos do dorso, eretores da espinha e trapézio também são recrutados no levantamento terra. Este exercício além de ser essencial para aqueles que desejam ganhar massa muscular e força, também beneficia no fortalecimento dos músculos posteriores e auxiliam a melhorar a postura e evitar lesões, além de ser extremamente funcional.
3. Flexão tradicional
Faça flexões tradicionais durante 30 segundos, mantendo os braços afastados à largura dos ombros e descendo até formar um ângulo de 90º com o cotovelo. Durante este exercício é muito importante manter o abdominal contraído para que as costas fiquem sempre alinhadas, evitando lesões

/MENU_INICIAL
''')
    
    
    
#SAÚDE MENTAL
                 
@bot.message_handler(commands=['Saude_Mental'])
def mental(mensagem):
    bot.reply_to(mensagem, '''
O estilo de vida pode ter um impacto significativo na saúde mental. Aqui estão alguns exemplos de como o estilo de vida pode afetar a saúde mental:

Dieta: Uma dieta equilibrada e saudável pode ajudar a manter um estado de espírito positivo e reduzir o risco de depressão e ansiedade.

Exercício: O exercício regular pode melhorar o humor, reduzir o estresse e a ansiedade, aumentar a autoestima e promover o bem-estar emocional. A falta de exercício pode ter o efeito oposto.

Sono: A qualidade e quantidade de sono podem afetar a saúde mental. A falta de sono pode causar irritabilidade, fadiga, ansiedade e depressão.

Conexões sociais: A solidão e o isolamento social podem levar a problemas de saúde mental, incluindo depressão e ansiedade. Ter conexões sociais saudáveis pode ajudar a melhorar o humor e a reduzir o estresse.

Trabalho: O estresse relacionado ao trabalho pode afetar a saúde mental. O excesso de trabalho, a pressão, o conflito e a falta de autonomia podem causar problemas de saúde mental.
    
    
/MENU_INICIAL
''')

#PRIMEIROS SOCORROS
@bot.message_handler(commands=['Primeiros_Socorros'])
def primeirosSocorros(mensagem):
    bot.reply_to(mensagem, '''
💉 Selecione o procedimento para obter suas informações:
/Desengasgo
/Massagem_Cardiaca
/Hemorragias
/Queimaduras

/MENU_INICIAL
    ''')
    
@bot.message_handler(commands=['Desengasgo'])
def desengasgo(mensagem):
    bot.reply_to(mensagem, '''
Nessa situação será preciso abraçar a pessoa por trás e, na altura do umbigo, pressionar repetidas vezes até que a vítima cuspa o objeto que está obstruindo a passagem de ar.

Assista o vídeo para saber mais: 
https://youtu.be/nVztTfKBT6M
    ''')
    
@bot.message_handler(commands=['Massagem_Cardiaca'])
def massagemCardiaca(mensagem):
    bot.reply_to(mensagem, '''
Ligue para o 192 e chame uma ambulância;

Mantenha a pessoa de barriga para cima e numa superfície dura;

Posicione as mãos sobre o peito da vítima, entrelaçando os dedos, entre os mamilos;

Empurre as suas mãos com força contra o peito, mantendo os braços esticados e utilizando o peso do próprio corpo, contando, no mínimo, 2 empurrões por segundo até a chegada do serviço de resgate. É importante deixar que o tórax do paciente volte a posição normal entre cada empurrão.

Assista o vídeo para saber mais: 
https://youtu.be/nCNJOOyMbVM
    ''')
    
@bot.message_handler(commands=['Hemorragias'])
def hemorragia(mensagem):
    bot.reply_to(mensagem, '''
Limpe a ferida, mas não internamente. Faça pressão contínua por cerca de 20 minutos para estancar o sangramento. Lembre-se de pressionar e de não parar a pressão para verificar se o sangramento parou, pois isso pode fazer com que ele volte.

Assista o vídeo para saber mais: 
https://youtu.be/_xICY4VBTfw
    ''')


@bot.message_handler(commands=['Queimaduras'])
def queimaduras(mensagem):
    bot.reply_to(mensagem, '''
O primeiro passo é afastar a vítima do agente causador da queimadura.

Em seguida, lave a área com água corrente limpa e caso haja uma vestimenta em contato com a queimadura ela pode ser retirada nesse momento, desde que não intensifique a lesão.

Não utilize gelo ou água fria no local e busque proteger a região com um pano limpo, mantendo-a mais elevada que o restante do corpo para evitar inchaço. Em seguida, encaminhe a vítima para um atendimento médico profissional, mantendo-a calma.

Assista o vídeo para saber mais: 
https://youtu.be/caj6gOD1tPc
    ''')
    
    

    
#EXAMES

@bot.message_handler(commands=['Exames'])
def exames(mensagem):
    bot.reply_to(mensagem, '''
Selecione o tipo de exame para verificar suas taxas:

/Triglicerideos
/Glicemia
/Colesterol_total
/Ureia
/Creatinina

Lembre-se que a avaliação médica é indispensável, os resultados são apenas para fins informativos e classificam apenas adultos. 😉
    ''')

    
@bot.message_handler(commands='Triglicerideos')
def triglicerideos(mensagem):
    bot.send_message(mensagem.chat.id, "🩸 Informe o resultado do seu exame")
    bot.register_next_step_handler(mensagem, registroTri)

def registroTri(mensagem):
    global tri
    tri = float(mensagem.text)

    if tri <= 150:
        situaçao = 'o valor do seu triglicerídeos está ideal'
    elif tri > 150 and tri <= 200:
        situaçao = '''seu estado é: limítrofe. 
        Deve-se tomar medidas para garantir sua saúde. Acesse /Dieta e/ou /Exercicios para saber mais.'''
    else:
        situaçao= '''seu estado é de risco. 
        Deve-se tomar medidas para garantir sua saúde. Acesse /Dieta e/ou /Exercicios para saber mais.
        '''
    
    bot.reply_to(mensagem, f'''Seu exame com resutado: {tri} mg/dL, indica que {situaçao}
    
    /MENU_INICIAL''')



    
@bot.message_handler(commands='Glicemia')
def glicose(mensagem):
    bot.send_message(mensagem.chat.id, "🩸 Informe o resultado do seu exame")
    bot.register_next_step_handler(mensagem, registroGli)

def registroGli(mensagem):
    global gli
    gli = float(mensagem.text)

    if gli < 70:
        situaçao = 'HIPOGLICEMIA'
    elif gli >= 70 and gli <= 99:
        situaçao = '''normalidade da glicemia em jejum'''
    elif gli >99 and gli< 125:
        situação = '''pré-diabetes.
 Deve-se tomar medidas para garantir sua saúde. Acesse /Dieta e/ou /Exercicios para saber mais. 
        '''
    else:
        situaçao= '''DIABETES. 
        Deve-se tomar medidas para garantir sua saúde. Acesse /Dieta e/ou /Exercicios para saber mais.
        '''
    
    bot.reply_to(mensagem, f'''Seu exame com resutado: {gli} mg/dl indica {situaçao}
    
    /MENU_INICIAL''')
    
    

@bot.message_handler(commands='Colesterol_total')
def colesterol(mensagem):
    bot.send_message(mensagem.chat.id, "🩸 Informe o resultado do seu exame")
    bot.register_next_step_handler(mensagem, registroCole)

def registroCole(mensagem):
    global col
    col = float(mensagem.text)

    if col < 190:
        situaçao = 'desejável'
    else:
        situaçao= '''dislipidemia. 
        Deve-se tomar medidas para garantir sua saúde. Acesse /Dieta e/ou /Exercicios para saber mais.
        '''
    
    bot.reply_to(mensagem, f'''Seu exame com resutado: {col} mg/dL indica {situaçao}
    
    /MENU_INICIAL''')


    
@bot.message_handler(commands='Ureia')
def ureia(mensagem):
    bot.send_message(mensagem.chat.id, "🩸 Informe o resultado do seu exame")
    bot.register_next_step_handler(mensagem, registroUreia)

def registroUreia(mensagem):
    global ureia
    ureia = float(mensagem.text)

    if ureia >= 13 and ureia <= 43:
        situaçao = 'desejável'
    else:
        situaçao= '''Alterado. Deve-se tomar medidas para garantir sua saúde.'''
    
    bot.reply_to(mensagem, f'''Seu exame com resutado: {ureia} mg/dL indica {situaçao}
    
    /MENU_INICIAL''')
    
    
    
    
@bot.message_handler(commands='Creatinina')
def creatina(mensagem):
    bot.send_message(mensagem.chat.id, "🩸 Informe o resultado do seu exame")
    bot.register_next_step_handler(mensagem, registroCreatina)

def registroCreatina(mensagem):
    global cre
    cre = float(mensagem.text)

    if cre >= 0.6 and cre <= 1.2:
        situaçao = 'desejável'
    else:
        situaçao= '''Alterado. Deve-se tomar medidas para garantir sua saúde.'''
    
    bot.reply_to(mensagem, f'''Seu exame com resutado: {cre} mg/dL indica {situaçao}
    
    /MENU_INICIAL''')
    
    
    

#MENSAGEM INICIAL
def verificar(mensagem):
    if mensagem.text == "/MENU_INICIAL" or mensagem.text == "/start":
        return True
    else:
        return False

@bot.message_handler(func=verificar)
def inicio(mensagem):
    bot.reply_to(mensagem, '''
Olá! 😄 Sou a Semilunar, fui projetada para te ajudar a monitorar seu bem-estar e auxiliar em técnicas de primeiros socorros. 

        👨‍⚕️ Se você deseja consultar a sua saúde física digite /Cadastro para responder algumas perguntas.
        
        🩺 Para consultar técnicas de primeiros socorros digite /Primeiros_Socorros.
        
        💉 Para avaliação e classificação de exames de rotina digite /Exames.
        
    ''')

    
bot.polling()