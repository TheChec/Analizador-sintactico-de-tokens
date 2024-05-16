from enum import (
    auto,
    Enum,
    unique,
)
from typing import (
    NamedTuple,
    Dict    
)
#Estos sons los tipos de token que puede leer nuestro lenguaje
@unique
class TokenType(Enum):
    MINUS = auto()
    DIVIDE = auto()
    MULTIPLICATION = auto()
    NOT = auto()
    ASSIGN = auto()
    COMMA = auto()
    EOF = auto()
    FUNCTION = auto()
    IDENT = auto()
    ILLEGAL =  auto()
    INT = auto()
    STR = auto()
    IF = auto()
    LT = auto()
    MT = auto()
    EQ = auto()
    WHILE = auto()
    NOT_EQ = auto()
    LT_EQ = auto()
    MT_EQ = auto
    RETURN = auto()
    TRUE = auto()
    ELSE = auto()
    FALSE = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    PLUS = auto()
    RBRACE = auto()
    RPAREN = auto()
    SEMICOLON = auto()
    AND = auto()
    BOOL = auto()

class Token(NamedTuple):
    token_type: TokenType
    literal: str
    
    def __str__ (self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'


#Aquí se puede leer el nombre de las variables que tenemos asignadas
def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'funcion': TokenType.FUNCTION,
        'variable': TokenType.LET,
        'si': TokenType.IF,
        'sino': TokenType.ELSE,
        'falso': TokenType.FALSE,
        'verdadero': TokenType.TRUE,
        'retorna': TokenType.RETURN,
        'mientras': TokenType.WHILE,
        'entero': TokenType.INT,
        'texto': TokenType.STR,
        'bool': TokenType.BOOL
    }
    
    return keywords.get(literal, TokenType.IDENT)