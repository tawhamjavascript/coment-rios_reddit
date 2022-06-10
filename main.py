import requests # importando a biblioteca requests
import json # importando a biblioteca json


string_de_busca = "depressão, ansiedade, suicídio" # string de busca
subreddit = "desabafos" # subreddit que será buscado
quantidade_de_posts = 10  # O máximo permitido é 500 comentários
tipo_de_busca = "submission" # pode procurar por post ou por comentário
ordenacao_dos_comentarios = "asc" # do comentário mais antigo para novo

base_url = f"https://api.pushshift.io/reddit/search/{tipo_de_busca}/?q={string_de_busca}&subreddit={subreddit}&sort={ordenacao_dos_comentarios}&size={quantidade_de_posts}"
requisicao = requests.get(base_url)

with open("comentarios.json", "w", encoding="utf-8") as arquivo:
    json.dump(requisicao.json(), arquivo, indent=4, ensure_ascii=False)