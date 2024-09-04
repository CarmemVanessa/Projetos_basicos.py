perguntas = [
    {
        "pergunta": "01- Qual o maior planeta do sistema solar?",
        "opções": ["A- Marte", "B- Jupter", "C- Saturno", "D- Terra"],
        "resposta": "B"
    },
    {
        "pergunta": "02- Qual nome da galáxia onde a terra esta localizada?",
        "opções": ["A- Andromeda", "B- Sombrero", "C- Via Láctea", "D- Triangulo"],
        "resposta": "C"
    },
    {
        "pergunta": "03- Qual planeta é conhecido como planeta vermelho?",
        "opções": ["A- Marte", "B- Vênus", "C- Saturno", "D- Plutão"],
        "resposta": "A"
    },
    {
        "pergunta": "04- Qual é o satélite natural da terra?",
        "opções": ["A- Titã", "B- Europa", "C- Lua", "D- Ganimedes"],
        "resposta": "C"
    },
    {
        "pergunta": "05- O que é uma supernova?",
        "opções": ["A- Uma nova estrela", "B- A explosão de uma estrela", "C- Um buraco negro em formação", "D- Uma nebulosa"],
        "resposta": "B"
    },
    {
        "pergunta": "06- Qual planeta é o mais próximo do Sol?",
        "opções": ["A- Vênus", "B- Terra", "C- Marte", "D- Mércurio"],
        "resposta": "D"
    },
    {
        "pergunta": "07- Em que ano o homem pisou na Lua pela primeira vez?",
        "opções": ["A- 1959", "B- 1969", "C- 1979", "D- 1989"],
        "resposta": "B"
    
    },
    {
        "pergunta": "08- O que é um buraco negro?",
        "opções": ["A- Um grande buraco na galáxia", "B- Um cometa gigante", "C- Uma estrela que brilha intensamente", "D- Uma região onde a gravidade é extremamente forte"],
        "resposta": "D"
    },
    {
        "pergunta": "09- O que é um cometa?",
        "opções": ["a) Um planeta anão", "B- Um asteroide grande", "C- Um corpo celeste composto de gelo e poeira", "D- Uma estrela cadente"],
        "resposta": "C"
    },
    {
        "pergunta": "10- O que é uma constelação?",
        "opções": ["A- Um conjunto de planetas", "B- Um agrupamento de estrelas que formam um padrão no céu", "C- Um cinturão de asteroides", "Um grupo de cometas"],
        "resposta": "B"
    }
    
]


pontuação = 0

for pergunta in perguntas:
    print(pergunta["pergunta"])
    for opção in pergunta["opções"]:
        print(opção)
    
    resposta_usuario = input("escolha uma resposta: ").upper()
    
    if resposta_usuario == pergunta['resposta']:
        print("Resposta Correta!\n")
        pontuação += 1
    else:
        print("Resposta Errada.\n")
    

print(f"Você acertou {pontuação} de {len(perguntas)} perguntas.")
        
    