from unittest import TestCase
from typing import List

from lpp.token import(
    Token,
    TokenType
)
from lpp.lexer import Lexer

"""Comando para hacer los test
mypy . 
nose2
""" 
class LexerTest(TestCase):
    
    def test_illegal(self) -> None:
        source: str = '¡¿@'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())
            
        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '¡'),
            Token(TokenType.ILLEGAL, '¿'),
            Token(TokenType.ILLEGAL, '@'),
        ]
        
        self.assertEqual(tokens, expected_tokens)
        
    def test_one_character_operator(self) -> None:
        source: str = '=+-/*<>!'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())
            
        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.MINUS, '-'),
            Token(TokenType.DIVIDE, '/'),
            Token(TokenType.MULTIPLICATION, '*'),
            Token(TokenType.LT, '<'),
            Token(TokenType.MT, '>'),
            Token(TokenType.NOT, '!'),
        ]
        
        self.assertEqual(tokens, expected_tokens)
        
    def test_eof(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(len(source) + 1):
            tokens.append(lexer.next_token())
        
        expected_token: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, '')
        ]
        
        self.assertEqual(tokens, expected_token)
        
    def test_delimeters(self) -> None:
        source: str = '(){},;'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(len(source)):
            tokens.append(lexer.next_token())
            
        expected_token: List[Token] = [
            Token(TokenType.LPAREN, '('),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),
        ]
        
        self.assertEqual(tokens, expected_token)
    
    def test_assignment(self) -> None:
        source: str = 'variable cinco = 5;'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(5):
            tokens.append(lexer.next_token())
        
        expected_token: List[Token] = [
            Token(TokenType.LET, 'variable'),
            Token(TokenType.IDENT, 'cinco'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';')
        ]
        
        self.assertEqual(tokens, expected_token)
    
    def test_function_declaration(self) -> None:
        source: str = """
            variable suma = funcion (x, y){
                x + y;
            };
        """
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(16):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'variable'),
            Token(TokenType.IDENT, 'suma'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.FUNCTION, 'funcion'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.PLUS, '+'),
            Token (TokenType.IDENT, 'y'),
            Token (TokenType.SEMICOLON, ';'),
            Token (TokenType.RBRACE, '}'),
            Token (TokenType.SEMICOLON, ';')
        ]
        
        self.assertEqual(tokens, expected_tokens)
    
    def test_function_call(self) -> None:
        source: str = 'variable resultado = suma(dos, tres);'
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(10):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.LET, 'variable'),
            Token(TokenType.IDENT, 'resultado'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.IDENT, 'suma'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.IDENT, 'dos'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'tres'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.SEMICOLON, ';'),
        ]
        
        self.assertEqual(tokens, expected_tokens)
    
    def test_control_statement(self) -> None:
        source: str = '''
            si (5 < 10) {
                retorna verdadero;
            }sino{
                retorna falso;
            }
        '''
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(17):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.IF, 'si'),
            Token(TokenType.LPAREN, '('),
            Token(TokenType.INT, '5'),
            Token(TokenType.LT, '<'),
            Token(TokenType.INT, '10'),
            Token(TokenType.RPAREN, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'retorna'),
            Token(TokenType.TRUE, 'verdadero'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.ELSE, 'sino'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RETURN, 'retorna'),
            Token(TokenType.FALSE, 'falso'),
            Token(TokenType.SEMICOLON, ';'),
            Token(TokenType.RBRACE, '}'),
        ]
        
        self.assertEqual(tokens, expected_tokens)
        
    def test_two_character_operator(self) -> None:
        source: str = '''
            10 == 10;
            10 != 9;
        '''
        lexer: Lexer = Lexer(source)
        
        tokens: List[Token] = []
        for i in range(8):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.INT , '10'),
            Token(TokenType.EQ , '=='),
            Token(TokenType.INT , '10'),
            Token(TokenType.SEMICOLON , ';'),
            Token(TokenType.INT , '10'),
            Token(TokenType.NOT_EQ , '!='),
            Token(TokenType.INT , '9'),
            Token(TokenType.SEMICOLON , ';'),
        ]
        
        self.assertEqual(tokens, expected_tokens)