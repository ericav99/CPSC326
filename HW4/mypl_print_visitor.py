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
            self.__write(self.__indent())
            if type(stmt) is ast.ExprStmt:
                if type(stmt.expr) is ast.ComplexExpr:
                    self.__write('(')
                    stmt.accept(self)
                    self.__write(');\n')
                else:
                    stmt.accept(self)
                    self.__write(';\n')
            else: # else they can handle themselves
                stmt.accept(self)
    
    def visit_expr_stmt(self, expr_stmt):
        if type(expr_stmt.expr) is ast.ExprStmt:
            self.__write('(')
            expr_stmt.expr.accept(self)
            self.__write(')')
        else:
            expr_stmt.expr.accept(self)
    
    def visit_var_decl_stmt(self, var_decl):
        self.__write('var ' + var_decl.var_id.lexeme)
        if var_decl.var_type != None:
            self.__write(': ' + var_decl.var_type.lexeme)
        self.__write(' = ')
        if type(var_decl.var_expr) is ast.ComplexExpr:
            self.__write('(')
            var_decl.var_expr.accept(self)
            self.__write(')')
        else:
            var_decl.var_expr.accept(self)
        self.__write(';\n')
        
    def visit_assign_stmt(self, assign_stmt):
        self.__write('set ')
        assign_stmt.lhs.accept(self)
        self.__write(' = ')
        if type(assign_stmt.rhs) is ast.ComplexExpr:
            self.__write('(')
            assign_stmt.rhs.accept(self)
            self.__write(')')
        else:
            assign_stmt.rhs.accept(self)
        self.__write(';\n')
    
    def visit_struct_decl_stmt(self, struct_decl):
        self.__write('\nstruct ' + struct_decl.struct_id.lexeme + '\n')
        self.indent += 1
        for var_decl in struct_decl.var_decls:
            self.__write(self.__indent())
            var_decl.accept(self)
        self.indent -= 1
        self.__write('end\n\n')
    
    def visit_fun_decl_stmt(self, fun_decl):
        self.__write('\nfun ' + fun_decl.return_type.lexeme + ' ' +
                fun_decl.fun_name.lexeme + '(')
        for i, fun_param in enumerate(fun_decl.params):
            fun_param.accept(self)
            if i != len(fun_decl.params) - 1:
                self.__write(', ')
        self.__write(')\n')
        self.indent += 1
        fun_decl.stmt_list.accept(self)
        self.indent -= 1
        self.__write('end\n\n')
    
    def visit_return_stmt(self, return_stmt):
        self.__write('return') # this could use child return_token but there's no point
        if return_stmt.return_expr != None:
            self.__write(' ')
            if type(return_stmt.return_expr) is ast.ComplexExpr:
                self.__write('(')
                return_stmt.return_expr.accept(self)
                self.__write(')')
            else:
                return_stmt.return_expr.accept(self)
        self.__write(';\n')
    
    def visit_while_stmt(self, while_stmt):
        self.__write('while ')
        while_stmt.bool_expr.accept(self)
        self.__write(' do\n')
        self.indent += 1
        while_stmt.stmt_list.accept(self)
        self.indent -= 1
        self.__write(self.__indent())
        self.__write('end\n')
    
    def visit_if_stmt(self, if_stmt):
        self.__write('if ')
        if_stmt.if_part.bool_expr.accept(self)
        self.__write(' then\n')
        self.indent += 1
        if_stmt.if_part.stmt_list.accept(self)
        self.indent -= 1
        for basic_if in if_stmt.elseifs:
            self.__write(self.__indent())
            self.__write('elif ')
            basic_if.bool_expr.accept(self)
            self.__write(' then\n')
            self.indent += 1
            basic_if.stmt_list.accept(self)
            self.indent -= 1
        if if_stmt.has_else:
            self.__write(self.__indent())
            self.__write('else\n')
            self.indent += 1
            if_stmt.else_stmts.accept(self)
            self.indent -= 1
        self.__write(self.__indent())
        self.__write('end\n')
    
    def visit_simple_expr(self, simple_expr):
        simple_expr.term.accept(self)
    
    def visit_complex_expr(self, complex_expr):
        if type(complex_expr.first_operand) is ast.ComplexExpr:
            self.__write('(')
        complex_expr.first_operand.accept(self)
        if type(complex_expr.first_operand) is ast.ComplexExpr:
            self.__write(')')
        self.__write(' ' + complex_expr.math_rel.lexeme + ' ')
        if type(complex_expr.rest) is ast.ComplexExpr:
            self.__write('(')
        complex_expr.rest.accept(self)
        if type(complex_expr.rest) is ast.ComplexExpr:
            self.__write(')')
    
    def visit_bool_expr(self, bool_expr):
        if (bool_expr.bool_connector != None and bool_expr.rest != None):
            self.__write('(')
        if bool_expr.negated:
            self.__write('not ')
        if bool_expr.bool_rel != None and bool_expr.second_expr != None:
            self.__write('(')
        bool_expr.first_expr.accept(self)
        if bool_expr.bool_rel != None and bool_expr.second_expr != None:
            self.__write(' ' + bool_expr.bool_rel.lexeme + ' ')
            bool_expr.second_expr.accept(self)
        if bool_expr.bool_rel != None and bool_expr.second_expr != None:
            self.__write(')')
        if bool_expr.bool_connector != None and bool_expr.rest != None:
            self.__write(' ' + bool_expr.bool_connector.lexeme + ' ')
            bool_expr.rest.accept(self)
        if (bool_expr.bool_connector != None and bool_expr.rest != None):
            self.__write(')')
    
    def visit_lvalue(self, lval):
        for i, token in enumerate(lval.path):
            if i == len(lval.path) - 1:
                self.__write(token.lexeme)
            else:
                self.__write(token.lexeme + '.')
    
    def visit_fun_param(self, fun_param):
        self.__write(fun_param.param_name.lexeme + ': ' +
                fun_param.param_type.lexeme)
    
    def visit_simple_rvalue(self, simple_rvalue):
        if type(simple_rvalue.val.lexeme) is str and simple_rvalue.val.lexeme != 'nil':
            self.__write('"' + simple_rvalue.val.lexeme + '"')
        else:
            self.__write(str(simple_rvalue.val.lexeme)) # have to cast the lexeme because it might not be a string here
    
    def visit_new_rvalue(self, new_rvalue):
        self.__write('new ' + new_rvalue.struct_type.lexeme)
    
    def visit_call_rvalue(self, call_rvalue):
        self.__write(call_rvalue.fun.lexeme + '(')
        for i, expr in enumerate(call_rvalue.args):
            expr.accept(self)
            if i != len(call_rvalue.args) - 1:
                self.__write(', ')
        self.__write(')')
    
    def visit_id_rvalue(self, id_rvalue):
        for i, token in enumerate(id_rvalue.path):
            if i == len(id_rvalue.path) - 1:
                self.__write(token.lexeme)
            else:
                self.__write(token.lexeme + '.')
