import csv

def extrair(caminho):
    with open(caminho, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def transformar(dados):
    dados_transformados = []
    for linha in dados:
        try:
            valor = float(linha['valor_venda'])
            qtd = int(linha['quantidade'])

            if qtd == 0:
                continue

            produto = linha['produto'].strip().title()
            categoria = linha['categoria'].strip().title()
            total = valor * qtd
            imposto = total * 0.10
            lucro = total - imposto

            dados_transformados.append({
                'id': linha['id'],
                'produto': produto,
                'categoria': categoria,
                'valor_unitario': round(valor, 2),
                'quantidade': qtd,
                'total_venda': round(total, 2),
                'imposto': round(imposto, 2),
                'lucro': round(lucro, 2)
            })

        except ValueError:
            # Pula linhas com valor de venda inválido
            continue

    return dados_transformados

def carregar(dados, caminho_saida):
    campos = ['id', 'produto', 'categoria', 'valor_unitario', 'quantidade', 'total_venda', 'imposto', 'lucro']
    with open(caminho_saida, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(dados)

def executar_etl():
    entrada = 'Dados/vendas_raw.csv'
    saida = 'Dados/vendas_processadas.csv'

    bruto = extrair(entrada)
    processado = transformar(bruto)
    carregar(processado, saida)
    print(f'{len(processado)} registros processados com sucesso.')

if __name__ == '__main__':
    executar_etl()
