# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 3
# Description:
#   Parser class, to be used in hw3.py
#------------------------------------------

import mypl_error as error
import mypl_lexer as lexer
import mypl_token as token

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
    
    def parse(self):
        self.__advance() # None -> first token
        self.__stmts()
        self.__eat(token.EOS, "expecting EOS") # this could just be advance(), but it's here to be safe
    
    def __advance(self):
        self.current_token = self.lexer.next_token()
    
    def __eat(self, tokentype, error_msg):
        if self.current_token.tokentype == tokentype:
            self.__advance()
        else:
            self.__error(error_msg)
    
    def __error(self, error_msg):
        s = error_msg + ', found "' + self.current_token.lexeme + '" in parser'
        l = self.current_token.line
        c = self.current_token.column
        raise error.MyPLError(s, l, c)
    
    # beginning of recursive descent functions
    # each one will expect to be on the next token and not need to advance
    
    def __stmts(self):
        # print("stmts: " + str(self.current_token))
        if self.current_token.tokentype != token.EOS:
            self.__stmt()
            self.__stmts()
    
    def __bstmts(self):
        # print("bstmts: " + str(self.current_token))
        if (self.current_token.tokentype == token.VAR or # check for bstmt
                self.current_token.tokentype == token.SET or
                self.current_token.tokentype == token.IF or
                self.current_token.tokentype == token.WHILE or
                self.current_token.tokentype == token.RETURN or
                self.current_token.tokentype == token.STRINGVAL or # check for expr -> rvalue...
                self.current_token.tokentype == token.INTVAL or
                self.current_token.tokentype == token.BOOLVAL or
                self.current_token.tokentype == token.FLOATVAL or
                self.current_token.tokentype == token.NIL or
                self.current_token.tokentype == token.NEW or
                self.current_token.tokentype == token.ID or
                self.current_token.tokentype == token.LPAREN): # check for expr -> LPAREN
            self.__bstmt()
            self.__bstmts()
    
    def __stmt(self):
        # print("stmt: " + str(self.current_token))
        if self.current_token.tokentype == token.STRUCTTYPE:
            self.__sdecl()
        elif self.current_token.tokentype == token.FUN:
            self.__fdecl()
        else:
            self.__bstmt()
    
    def __bstmt(self):
        # print("bstmt: " + str(self.current_token))
        if self.current_token.tokentype == token.VAR:
            self.__vdecl()
        elif self.current_token.tokentype == token.SET:
            self.__assign()
        elif self.current_token.tokentype == token.IF:
            self.__cond()
        elif self.current_token.tokentype == token.WHILE:
            self.__while()
        elif self.current_token.tokentype == token.RETURN:
            self.__exit()
        else:
            self.__expr()
            self.__eat(token.SEMICOLON, 'expecting ";"')
    
    def __sdecl(self):
        # print("sdecl: " + str(self.current_token))
        self.__advance() # eat STRUCT (we already know from stmt)
        self.__eat(token.ID, 'expecting ID')
        self.__vdecls()
        self.__eat(token.END, 'expecting "end"')
    
    def __vdecls(self):
        # print("vdecls: " + str(self.current_token))
        if self.current_token.tokentype == token.VAR:
            self.__vdecl()
            self.__vdecls()
    
    def __fdecl(self):
        # print("fdecl: " + str(self.current_token))
        self.__advance() # eat FUN (we already know from stmt)
        if self.current_token.tokentype == token.NIL:
            self.__advance() # eat NIL (we already know from 1 line up)
        else:
            self.__type()
        self.__eat(token.ID, 'expecting ID')
        self.__eat(token.LPAREN, 'expecting "("')
        self.__params()
        self.__eat(token.RPAREN, 'expecting ")"')
        self.__bstmts()
        self.__eat(token.END, 'expecting "end"')
    
    def __params(self):
        # print("params: " + str(self.current_token))
        if self.current_token.tokentype == token.ID:
            self.__advance() # eat ID (we already know from 1 line up)
            self.__eat(token.COLON, 'expecting ":"')
            self.__type()
            while self.current_token.tokentype == token.COMMA:
                self.__advance() # eat COMMA (we already know from 1 line up)
                self.__eat(token.ID, 'expecting ID')
                self.__eat(token.COLON, 'expecting ":"')
                self.__type()
    
    def __type(self):
        # print("type: " + str(self.current_token))
        if (self.current_token.tokentype == token.ID or
                self.current_token.tokentype == token.INTTYPE or
                self.current_token.tokentype == token.FLOATTYPE or
                self.current_token.tokentype == token.BOOLTYPE or
                self.current_token.tokentype == token.STRINGTYPE):
            self.__advance() # eat (we already know from 1 line up)
        else:
            self.__error('expecting type')
    
    def __exit(self):
        # print("exit: " + str(self.current_token))
        self.__advance() # eat RETURN (we already know from bstmt)
        if (self.current_token.tokentype == token.STRINGVAL or # check for expr -> rvalue...
                self.current_token.tokentype == token.INTVAL or
                self.current_token.tokentype == token.BOOLVAL or
                self.current_token.tokentype == token.FLOATVAL or
                self.current_token.tokentype == token.NIL or
                self.current_token.tokentype == token.NEW or
                self.current_token.tokentype == token.ID or
                self.current_token.tokentype == token.LPAREN): # check for expr -> LPAREN
            self.__expr()
        self.__eat(token.SEMICOLON, 'expecting ";"')
    
    def __vdecl(self):
        # print("vdecl: " + str(self.current_token))
        self.__advance() # eat VAR (we already know from bstmt and vdecls)
        self.__eat(token.ID, 'expecting ID')
        self.__tdecl()
        self.__eat(token.ASSIGN, 'expecting "="')
        self.__expr()
        self.__eat(token.SEMICOLON, 'expecting ";"')
    
    def __tdecl(self):
        # print("tdecl: " + str(self.current_token))
        if self.current_token.tokentype == token.COLON:
            self.__advance() # eat COLON (we already know from 1 line up)
            self.__type()
    
    def __assign(self):
        # print("assign: " + str(self.current_token))
        self.__advance() # eat SET (we already know from bstmt)
        self.__lvalue()
        self.__eat(token.ASSIGN, 'expecting "="')
        self.__expr()
        self.__eat(token.SEMICOLON, 'expecting ";"')
    
    def __lvalue(self):
        # print("lvalue: " + str(self.current_token))
        self.__eat(token.ID, 'expecting ID')
        while self.current_token.tokentype == token.DOT:
            self.__advance() # eat DOT (we already know from 1 line up)
            self.__eat(token.ID, 'expecting ID')
    
    def __cond(self):
        # print("cond: " + str(self.current_token))
        self.__advance() # eat IF (we already know from bstmt)
        self.__bexpr()
        self.__eat(token.THEN, 'expecting "then"')
        self.__bstmts()
        self.__condt()
        self.__eat(token.END, 'expecting "end"')
    
    def __condt(self):
        # print("condt: " + str(self.current_token))
        if self.current_token.tokentype == token.ELIF:
            self.__advance() # eat ELIF (we already know this from 1 line up)
            self.__bexpr()
            self.__eat(token.THEN, 'expecting "then"')
            self.__bstmts()
            self.__condt()
        elif self.current_token.tokentype == token.ELSE:
            self.__advance() # eat ELSE (we already know this from 1 line up)
            self.__bstmts()
    
    def __while(self):
        # print("while: " + str(self.current_token))
        self.__advance() # eat WHILE (we already know from bstmt)
        self.__bexpr()
        self.__eat(token.DO, 'expecting "do"')
        self.__bstmts()
        self.__eat(token.END, 'expecting "end"')
    
    def __expr(self):
        # print("expr: " + str(self.current_token))
        if self.current_token.tokentype == token.LPAREN:
            self.__advance() # eat LPAREN (we already know from 1 line up)
            self.__expr()
            self.__eat(token.RPAREN, 'expecting ")"')
        else:
            self.__rvalue()
        
        if (self.current_token.tokentype == token.PLUS or # check for mathrel
                self.current_token.tokentype == token.MINUS or
                self.current_token.tokentype == token.DIVIDE or
                self.current_token.tokentype == token.MULTIPLY or
                self.current_token.tokentype == token.MODULO):
            self.__mathrel()
            self.__expr()
    
    def __mathrel(self):
        # print("mathrel: " + str(self.current_token))
        self.__advance() # eat (we already know from expr)
    
    def __rvalue(self):
        # print("rvalue: " + str(self.current_token))
        if (self.current_token.tokentype == token.STRINGVAL or
                self.current_token.tokentype == token.INTVAL or
                self.current_token.tokentype == token.BOOLVAL or
                self.current_token.tokentype == token.FLOATVAL or
                self.current_token.tokentype == token.NIL):
            self.__advance() # eat (we already know from 1 line up)
        elif self.current_token.tokentype == token.NEW:
            self.__advance()
            self.__eat(token.ID, 'expecting ID')
        else:
            self.__idrval()
    
    def __idrval(self):
        # print("idrval: " + str(self.current_token))
        self.__eat(token.ID, 'expecting ID')
        if self.current_token.tokentype == token.LPAREN:
            self.__advance() # eat LPAREN (we already know from 1 line up)
            self.__exprlist()
            self.__eat(token.RPAREN, 'expecting ")"')
        else:
            while self.current_token.tokentype == token.DOT:
                self.__advance() # eat DOT (we already know from 1 line up)
                self.__eat(token.ID, 'expecting ID')
    
    def __exprlist(self):
        # print("exprlist: " + str(self.current_token))
        if (self.current_token.tokentype == token.STRINGVAL or # check for expr -> rvalue...
                self.current_token.tokentype == token.INTVAL or
                self.current_token.tokentype == token.BOOLVAL or
                self.current_token.tokentype == token.FLOATVAL or
                self.current_token.tokentype == token.NIL or
                self.current_token.tokentype == token.NEW or
                self.current_token.tokentype == token.ID or
                self.current_token.tokentype == token.LPAREN): # check for expr -> LPAREN
            self.__expr()
            while self.current_token.tokentype == token.COMMA:
                self.__advance() # eat COMMA (we already know from 1 line up)
                self.__expr()
    
    def __bexpr(self):
        # print("bexpr: " + str(self.current_token))
        if self.current_token.tokentype == token.NOT:
            self.__advance() # eat NOT (we already know from 1 line up)
            self.__bexpr()
            self.__bexprt()
        elif self.current_token.tokentype == token.LPAREN:
            self.__advance() # eat LPAREN (we already know from 1 line up)
            self.__bexpr()
            self.__eat(token.RPAREN, 'expecting ")"')
            self.__bconnct()
        else:
            self.__expr()
            self.__bexprt()
    
    def __bexprt(self):
        # print("bexprt: " + str(self.current_token))
        if (self.current_token.tokentype == token.EQUAL or # check for boolrel
                self.current_token.tokentype == token.LESS_THAN or
                self.current_token.tokentype == token.GREATER_THAN or
                self.current_token.tokentype == token.LESS_THAN_EQUAL or
                self.current_token.tokentype == token.GREATER_THAN_EQUAL or
                self.current_token.tokentype == token.NOT_EQUAL):
            self.__boolrel()
            self.__expr()
        self.__bconnct()
    
    def __bconnct(self):
        # print("bconnct: " + str(self.current_token))
        if self.current_token.tokentype == token.AND:
            self.__advance() # eat AND (we already know from 1 line up)
            self.__bexpr()
        elif self.current_token.tokentype == token.OR:
            self.__advance() # eat OR (we already know from 1 line up)
            self.__bexpr()
    
    def __boolrel(self):
        # print("boolrel: " + str(self.current_token))
        self.__advance() # eat (we already know from bexprt)
