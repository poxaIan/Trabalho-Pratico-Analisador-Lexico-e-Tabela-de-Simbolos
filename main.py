import ply.lex as lex
from collections import defaultdict

# Definição dos tokens
tokens = (
    'IF', 'FOR', 'WHILE', 'NUMBER', 'OPERATOR', 'LETTER', 'SEMICOLON', 'PROGRAM',
    'ID', 'DECLARE', 'BEGIN', 'END', 'INTEGER', 'DECIMAL', 'THEN', 'ELSE', 'DO', 'TO',
    'READ', 'WRITE', 'OR', 'MOD', 'AND', 'COMMA', 'LPAREN', 'RPAREN', 'EQUAL', 'PERCENT',
    'COLON', 'DOUBLE_QUOTE', 'HASH', 'MINUS', 'GT', 'LT', 'DOLLAR', 'QUESTION', 'END_DOUBLE_QUOTE',
    'EXTRA_DOUBLE_QUOTE'
)

# Dicionário de palavras reservadas
reserved = {
    'if': 'IF', 'for': 'FOR', 'while': 'WHILE', 'program': 'PROGRAM', 'declare': 'DECLARE',
    'begin': 'BEGIN', 'end': 'END', 'integer': 'INTEGER', 'decimal': 'DECIMAL',
    'then': 'THEN', 'else': 'ELSE', 'do': 'DO', 'to': 'TO', 'read': 'READ', 'write': 'WRITE',
    'or': 'OR', 'mod': 'MOD', 'and': 'AND',
}

# Tabela de símbolos
symbol_table = defaultdict(list)

# Regras de expressão regular para os tokens
t_NUMBER = r'\d+'
t_OPERATOR = r'[+\-*/]'
t_LETTER = r'[a-zA-Z]'
t_SEMICOLON = r';'

# Expressões regulares para caracteres adicionais
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'='
t_PERCENT = r'%'
t_COLON = r':'
t_DOUBLE_QUOTE = r'[“”"]'  # Aspas Duplas "
t_HASH = r'\#'  # Sustenido #
t_MINUS = r'–'  # Sinal de Menos -
t_GT = r'>'  # Maior que >
t_LT = r'<'  # Menor que <
t_DOLLAR = r'\$'  # Sinal de Dólar $
t_QUESTION = r'\?'  # Interrogação ?
# t_END_DOUBLE_QUOTE = r'”'
# t_EXTRA_DOUBLE_QUOTE = r'"'

# Ignorar caracteres em branco e tabulações
t_ignore = ' \t'


# Função para rastrear o número da linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Função para identificar identificadores (palavras reservadas ou não)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verificar se é uma palavra reservada

    if t.type == 'ID':
        symbol_info = (t.lexer.lineno, t.type)  # Modifique esta linha para armazenar informações adicionais
        symbol_table[t.value].append(symbol_info)

    return t


# Lidar com erros léxicos
def t_error(t):
    print(f"--------------------------Caractere ilegal--------------------------: {t.value[0]!r}")
    t.lexer.skip(1)


lexer = lex.lex()

entrada = '''
Teste 9:

program teste9

declare

integer numero, divisivel;

begin

read(numero);

divisivel := numero % 2;

if (divisivel = 0) then
    write("O numero e divisivel por 2")
else
    write("O numero nao e divisivel por 2")
end

end
'''

lexer.input(entrada)

for tok in lexer:
    print(f'{tok.type}: {tok.value}')

print("\nTabela de Símbolos:")
for symbol, info in symbol_table.items():
    print(f'{symbol}: {info}')
