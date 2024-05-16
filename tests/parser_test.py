from unittest import TestCase
from typing import (
    cast,
    List
)
from lpp.lexer import Lexer
from lpp.parser import Parser
from lpp.ast import (
    LetStatement,
    Program
)

class ParserTest(TestCase):
    def test_parse_program(self) -> None:
        source: str = 'variable x =5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        
        program: Program = parser.parse_program()
        
        self.assertIsNotNone(program)
        self.assertIsInstance(program, Program)
    
    def test_let_statements(self) -> None:
        source: str = '''
            variable x = 5;
            variable y = 10;
            variable foo = 20;
        '''
        
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser (lexer)
        program: Program = parser.parse_program()
        
        self.assertEqual(len(program.statements), 3)
        
        for statement in program.statements:
            self.assertEqual(statement.token_literal(), 'variable')
            self.assertIsInstance(statement, LetStatement)
    
    def test_names_in_let_statements(self) -> None:
        source: str = '''
            variable x = 5;
            variable y = 10;
            variable foo = 20;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        names: List[str] = []
        for statement in program.statements:
            statement = cast(LetStatement, statement)
            assert statement.name is not None
            names.append(statement.name.value)

        expected_names: List[str] = ['x', 'y', 'foo']

        self.assertEqual(names, expected_names)
    
    def test_parse_errors(self) -> None:
        source: str = 'variable x 5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        program: Program = parser.parse_program()
        
        print(parser.errors)
    
        self.assertEqual(len(parser.errors), 2)