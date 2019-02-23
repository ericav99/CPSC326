# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 5
# Description:
#   Type Checker visitor class, to be used in hw5.py
#-----------------------------------------------------

import mypl_token as token
import mypl_ast as ast
import mypl_error as error
import mypl_symbol_table as symbol_table

# a MyPL type checker visitor implementation where struct types
# take the form: type_id -> {v1:t1, ..., vn:tn} and function types
# take the form: fun_id -> [[t1, t2, ..., tn], return_type]
class TypeChecker(ast.Visitor):
    # init method
    def __init__(self):
        # initialize the symbol table (for ids -> types)
        self.sym_table = symbol_table.SymbolTable()
        
        # current_type holds the type of the last expression type
        self.current_type = None
        
        # global env (for return)
        self.sym_table.push_environment()
        
        # set global return type to int
        self.sym_table.add_id('return')
        self.sym_table.set_info('return', token.INTTYPE)
        
        # load in built-in function types
        self.sym_table.add_id('print')
        self.sym_table.set_info('print', [[token.STRINGTYPE], token.NIL])
        
        # TODO: remaining function types
    
    # beginning of type checking visitor methods
    
    def visit_stmt_list(self, stmt_list):
        # add new block (scope)
        self.sym_table.push_environment()
        
        for stmt in stmt_list.stmts:
            stmt.accept(self)
        
        # remove new block
        self.sym_table.pop_environment
    
    def visit_expr_stmt(self, expr_stmt):
        expr_stmt.expr.accept(self)
    
    def visit_var_decl_stmt(self, var_decl):
        # TODO
    
    def visit_assign_stmt(self, assign_stmt):
        assign_stmt.rhs.accept(self)
        rhs_type = self.current_type
        assign_stmt.lhs.accept(self)
        lhs_type = self.current_type
        if rhs_type != token.NIL and rhs_type != lhs_type:
            msg = 'mismatched type in assignment'
            self.__error(msg, assign_stmt.lhs.path[0])
    
    # TODO: remaining visitor methods
