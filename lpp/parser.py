from lpp.ast import (
    Program,
    Identifier,
    LetStatement,
    Statement
)
from lpp.lexer import Lexer
from typing import (
    Optional,
    List,
)
from lpp.token import (
    Token,
    TokenType
)

class Parser:
    def __init__(self, lexer: Lexer) -> None:
        self._lexer = lexer
        self._current_token: Optional[Token] = None
        self._peek_token: Optional[Token] = self._lexer.next_token()
        self._errors: List[str] = []
        
        self._advance_tokens() 
        self._advance_tokens() 
        
    @property
    def errors(self) -> List[str]:
        return self._errors
        
    def parse_program(self) -> Program:
        program: Program = Program(statements = [])
        
        assert self._current_token is not None
        
        while self._current_token.token_type != TokenType.EOF:
            statement = self._parse_statement()
            if statement is not None:
                program.statements.append(statement)
            
            self._advance_tokens()
        
        return program
    
    def _advance_tokens(self) -> None:
        self._current_token = self._peek_token
        self._peek_token = self._lexer.next_token()
    
    def _expected_tokens(self, token_type: TokenType) -> bool:
        assert self._peek_token is not None
        if self._peek_token.token_type == token_type:
            self._advance_tokens()
            
            return True
        
        self._expected_token_error(token_type)
        return False
    
    def _expected_token_error(self, token_type: TokenType) -> None:
        assert self._peek_token is not None
        error = f'Error esperado en: {token_type} ' + \
            f'Pero se obtuvo {self._peek_token.token_type}'
        
        self._errors.append(error)
    
    def _parse_let_statement(self) -> Optional[LetStatement]:
        assert self._current_token is not None
        let_statement = LetStatement(token = self._current_token)
        
        if not self._expected_tokens(TokenType.IDENT):
            return None
        
        let_statement.name = Identifier(token = self._current_token, value = self._current_token.literal)
        
        if not self._expected_tokens(TokenType.ASSIGN):
            return None
        
        #Terminar cuando expresiones
        
        while self._current_token.token_type != TokenType.SEMICOLON and self._current_token.token_type != TokenType.EOF:
            self._advance_tokens()
        
        return let_statement

    def _parse_statement(self) -> Optional[Statement]:
        assert self._current_token is not None
        if self._current_token.token_type == TokenType.LET:
            return self._parse_let_statement()
        else:
            return None