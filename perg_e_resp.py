perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'Quanto é 2+2?',
        'respostas' : {'a' : '1', 'b': '5', 'c' : '4'},
        'resposta_certa' : 'c'
    },
    'Pergunta 2' : {
        'pergunta' : 'Quanto é 5+9?',
        'respostas' : {'a' : '7', 'b': '14', 'c' : '9'},
        'resposta_certa' : 'b'
    },
    'Pergunta 3' : {
        'pergunta' : 'Quanto é 5 X 4?',
        'respostas' : {'a' : '20', 'b': '22', 'c' : '16'},
        'resposta_certa' : 'a'
    },
    'Pergunta 4' : {
        'pergunta' : 'Quanto é 32 / 2?',
        'respostas' : {'a' : '16', 'b': '22', 'c' : '19'},
        'resposta_certa' : 'a'
    },
    'Pergunta 5' : {
        'pergunta' : 'Quanto é raiz de 81?',
        'respostas' : {'a' : '8', 'b': '10', 'c' : '9'},
        'resposta_certa' : 'c'
    },
    
}

for perg_laço, perg_cont in perguntas.items():
    print(f'{perg_laço}: {perg_cont["pergunta"]}')
    for perg_laço_alt, perg_cont_resp in perg_cont['respostas'].items():
        print(f'{perg_laço_alt}: {perg_cont_resp}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario in perg_cont['resposta_certa']:
        print(' CORRETO')
    else:
        print('ERRADO')