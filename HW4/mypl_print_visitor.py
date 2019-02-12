# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 4
# Description:
#   PrintVisitor class, used to print the AST nicely
#-----------------------------------------------------------------

import mypl_token as token
import mypl_ast as ast

class PrintVisitor(ast.Visitor):
    """An AST pretty printer"""
    
    def __init__(self, output_stream):
        self.indent = 0                     # to increase/decrease indent level
        self.output_stream = output_stream  # where to print
    
    def __indent(self):
        """Get default indent of 4 spaces"""
        return '    ' * self.indent
    
    def __write(self, msg):
        self.output_stream.write(msg)
    
    def visit_stmt_list(self, stmt_list):
        for stmt in stmt_list.stmts:
            stmt.accept(self)
    
    def visit_expr_stmt(self, expr_stmt):
        self.__write(self.__indent())
        expr_stmt.expr.accept(self)
        self.__write(';\n')
    
    # TODO: the rest
