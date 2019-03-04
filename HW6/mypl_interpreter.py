# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 6
# Description:
#   Interprets the AST to run the MyPL code
#---------------------------------------------------

import mypl_token as token
import mypl_ast as ast
import mypl_error as error
import mypl_symbol_table as sym_tbl

# a MyPL visitor implementation
class Interpreter(ast.Visitor):
    # init method
    def __init__(self):
        # initialize symbol table (for ids -> values)
        self.sym_table = sym_tbl.SymbolTable()
        # holds the value of the last expression
        self.current_value = None
    
    # raises a descriptive error given a simple message and token
    def __error(self, msg, the_token):
        raise error.MyPLError(msg, the_token.line, the_token.column)
    
    # beginning of interpreter visitor methods
    
    def visit_stmt_list(self, stmt_list):
        self.sym_table.push_environment()
        for stmt in stmt_list.stmts:
            stmt.accept(self)
        self.sym_table.pop_environment()
    
    def visit_expr_stmt(self, stmt):
        stmt.expr.accept(self)
    
    def visit_simple_expr(self, simple_expr):
        simple_expr.term.accept(self)
    
    def visit_simple_rvalue(self, simple_rvalue):
        if simple_rvalue.val.tokentype == token.NIL:
            self.current_value = None
        elif simple_rvalue.val.tokentype == token.INTVAL:
            self.current_value = int(simple_rvalue.val.lexeme)
        elif simple_rvalue.val.tokentype == token.FLOATVAL:
            self.current_value = float(simple_rvalue.val.lexeme)
        elif simple_rvalue.val.tokentype == token.BOOLVAL:
            if simple_rvalue.val.lexeme == 'true':
                self.current_value = True
            else: # 'false'
                self.current_value = False
        else: # stringval
            self.current_value = simple_rvalue.val.lexeme
    
    # structs not currently supported
    def visit_new_rvalue(self, new_rvalue): pass
    
    # user-defined functions not currently supported
    def visit_call_rvalue(self, call_rvalue):
        # call_rvalue.fun.tokentype should be ID
        if call_rvalue.fun.lexeme == 'print':
            if len(call_rvalue.args) != 1:
                msg = 'incorrect number of args'
                self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
            else:
                call_rvalue.args[0].accept(self)
                print(call_rvalue.args[0], end='')
        elif call_rvalue.fun.lexeme == 'length':
            if len(call_rvalue.args) != 1:
                msg = 'incorrect number of args'
                self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
            else:
                call_rvalue.args[0].accept(self)
                if type(self.current_value) != str:
                    msg = 'this type has no length'
                    self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
                else:
                    self.current_value = len(self.current_calue)
        elif call_rvalue.fun.lexeme == 'get':
            if len(call_rvalue.args) != 2:
                msg = 'incorrect number of args'
                self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
            else:
                call_rvalue.args[0].accept(self)
                arg1 = self.current_value
                call_rvalue.args[1].accept(self)
                if type(self.current_value) is not str:
                    msg = 'this type cannot be indexed'
                    self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
                elif type(arg1) is not int:
                    msg = 'invalid index for get'
                    self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
                else:
                    self.current_value = self.current_value[call_rvalue.args[0]]
        elif call_rvalue.fun.lexeme == 'reads':
            if len(call_rvalue.args) != 0:
                msg = 'this function takes no arguments'
                self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
            else:
                self.current_value = input()
        elif call_rvalue.fun.lexeme == 'readi':
            if len(call_rvalue.args) != 0:
                msg = 'this function takes no arguments'
                self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
            else:
                self.current_value = int(input())
        elif call_rvalue.fun.lexeme == 'readf':
            if len(call_rvalue.args) != 0:
                msg = 'this function takes no arguments'
                self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
            else:
                self.current_value = float(input())
        elif call_rvalue.fun.lexeme == 'itof':
            if len(call_rvalue.args) != 1:
                msg = 'incorrect number of args'
                self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
            else:
                call_rvalue.args[0].accept(self)
                if type(self.current_value) is not int:
                    msg = 'argument not of type int'
                    self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
                else:
                    self.current_value = float(self.current_value)
        elif call_rvalue.fun.lexeme == 'itos':
            if len(call_rvalue.args) != 1:
                msg = 'incorrect number of args'
                self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
            else:
                call_rvalue.args[0].accept(self
                if type(self.current_value) is not int:
                    msg = 'argument not of type int'
                    self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
                else:
                    self.current_value = str(self.current_value)
        elif call_rvalue.fun.lexeme == 'ftos':
            if len(call_rvalue.args) != 1:
                msg = 'incorrect number of args'
                self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
            else:
                call_rvalue.args[0].accept(self)
                if type(self.current_value) is not float:
                    msg = 'argument not of type float'
                    self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
                else:
                    self.current_value = str(self.current_value)
        else:
            msg = 'user-defined functions not currently supported'
            self.__error(msg, call_rvalue.fun.line, call_rvalue.fun.column)
    
    # sub-variables not supported because structs not currently supported
    def visit_id_rvalue(self, id_rvalue):
        if len(id_rvalue.path) > 1:
            msg = 'structs not currently supported'
            self.__error(msg, id_rvalue.path[1].line, call_rvalue.path[1].column)
        else:
            self.current_value = self.sym_table[id_rvalue.path[0]]
    
    def visit_complex_expr(self, complex_expr):
        complex_expr.first_operand.accept(self)
        left_value = self.current_value
        math_rel = complex_expr.math_rel.lexeme
        complex_expr.rest.accept(self)
        right_value = self.current_value
        
        if math_rel == '+':
            self.current_value = left_value + right_value
        elif math_rel == '-':
            self.current_value = left_value - right_value
        elif math_rel == '*':
            self.current_value = left_value * right_value
        elif math_rel == '/':
            self.current_value = left_value / right_value
        else: '%'
            self.current_value = left_value % right_value
