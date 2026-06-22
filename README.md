# Processador de NFe - Aplicação Web

Uma aplicação web Flask que processa arquivos XML de NFe e gera planilhas Excel automaticamente.

## Funcionalidades

- ✅ Upload de múltiplos arquivos XML de NFe
- ✅ Processamento automático dos dados das notas fiscais
- ✅ Geração de planilha Excel com dados estruturados
- ✅ Interface web moderna e responsiva
- ✅ Download automático da planilha gerada

## Como executar a aplicação

### 1. Navegue até o diretório da aplicação
```bash
cd nfe-web-app
```

### 2. Ative o ambiente virtual
```bash
source venv/bin/activate
```

### 3. Execute a aplicação
```bash
python src/main.py
```

### 4. Acesse no navegador
Abra seu navegador e acesse: `http://localhost:5000`

## Como usar

1. **Upload de arquivos**: Clique na área de upload ou arraste seus arquivos XML de NFe
2. **Processamento**: Clique em "Processar Arquivos" para gerar a planilha
3. **Download**: Após o processamento, clique no link "📥 Baixar Planilha" para fazer o download

## Estrutura dos dados na planilha

A planilha gerada contém as seguintes colunas:

### Dados da Nota Fiscal
- `chNFe` - Chave da NFe
- `nNF` - Número da NFe
- `dhEmi` - Data de emissão
- `UF` - Estado
- `CRT` - Regime tributário

### Dados dos Produtos
- `xProd` - Descrição do produto
- `NCM` - Código NCM
- `CEST` - Código CEST
- `CFOP` - Código CFOP
- `qCom` - Quantidade comercial
- `vUnCom` - Valor unitário comercial

### Dados Fiscais
- `vFrete` - Valor do frete
- `vSeg` - Valor do seguro
- `vDesc` - Valor do desconto
- `vOutro` - Outros valores
- `vBC` - Base de cálculo do ICMS
- `vIPI` - Valor do IPI
- `orig` - Origem da mercadoria
- `CST` - Código de Situação Tributária
- `pICMS` - Percentual de ICMS
- `vICMS` - Valor do ICMS
- `vBCST` - Base de cálculo do ICMS ST
- `vICMSST` - Valor do ICMS ST
- `pMVAST` - Percentual da margem de valor agregado do ICMS ST

## Tecnologias utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Processamento XML**: minidom
- **Geração Excel**: openpyxl
- **Interface**: Design responsivo com gradientes modernos

## Arquivos importantes

- `src/main.py` - Arquivo principal da aplicação Flask
- `src/routes/nfe.py` - Rotas para processamento de NFe
- `src/nfe_processor.py` - Lógica de processamento dos arquivos XML
- `src/static/index.html` - Interface web da aplicação
- `requirements.txt` - Dependências do projeto

## Observações

- A aplicação suporta múltiplos arquivos XML simultaneamente
- Os arquivos processados são salvos temporariamente e removidos após o processamento
- A planilha gerada fica disponível para download na pasta `src/downloads/`
- A aplicação roda em modo debug por padrão (adequado para desenvolvimento)

