import google.generativeai as genai

def correcao_codigo(chave, codigo):
    genai.configure(api_key=chave)

    modelo = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f''' Considerando o seguinte código fornecido identifique o erro caso exista
    e apresente a solução.
    
    # Código:
    {codigo}
    '''

    resposta = modelo.generate_content(prompt)

    return resposta.text

def conversao_codigo(chave, linguagem_atual, linguagem_conversao, codigo):
    genai.configure(api_key=chave)

    modelo = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f''' Você vai receber um código de programação na linguagem original {linguagem_atual} 
    e vai converter esse código para a linguagem {linguagem_conversao}.

    # Código:
    {codigo}
    '''

    resposta = modelo.generate_content(prompt)

    return resposta.text