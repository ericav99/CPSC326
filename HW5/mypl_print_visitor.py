# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 5
# Description:
#   PrintVisitor class, used to print the AST nicely
#-----------------------------------------------------

import mypl_token as token
import mypl_ast as ast

# MyPL pretty print visitor
# visits a fully constructed MyPL AST and prints it out as code
class PrintVisitor(ast.Visitor):
    
    # init method
    def __init__(self, output_stream):
        self.indent = 0                     # to increase/decrease indent level
        self.output_stream = output_stream  # where to print
    
    # use in __write() to print the proper number of indents when necessary
    def __indent(self):
        return '    ' * self.indent # indent is 4 spaces
    
    # writes directly to the output stream (no newline)
    # better than print because it can write to any output stream
    # and not having a newline on the end really helps in this class
    def __write(self, msg):
        self.output_stream.write(msg)
    
    # beginning of print visitor methods
    
    # __indent() is only printed before calling sub-methods
    # ex. in the body of a function declaration or while-loop
    # before visiting the StmtList object and printing it out
    
    # prints the code of of a StmtList
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
    
    # prints the code of of an ExprStmt
    def visit_expr_stmt(self, expr_stmt):
        if type(expr_stmt.expr) is ast.ExprStmt:
            self.__write('(')
            expr_stmt.expr.accept(self)
            self.__write(')')
        else:
            expr_stmt.expr.accept(self)
    
    # prints the code of of a VarDeclStmt
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
    
    # prints the code of of an AssignStmt
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
    
    # prints the code of of a StructDeclStmt
    def visit_struct_decl_stmt(self, struct_decl):
        self.__write('\nstruct ' + struct_decl.struct_id.lexeme + '\n')
        self.indent += 1
        for var_decl in struct_decl.var_decls:
            self.__write(self.__indent())
            var_decl.accept(self)
        self.indent -= 1
        self.__write('end\n\n')
    
    # prints the code of of a FunDeclStmt
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
    
    # prints the code of of a ReturnStmt
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
    
    # prints the code of of a WhileStmt
    def visit_while_stmt(self, while_stmt):
        self.__write('while ')
        while_stmt.bool_expr.accept(self)
        self.__write(' do\n')
        self.indent += 1
        while_stmt.stmt_list.accept(self)
        self.indent -= 1
        self.__write(self.__indent())
        self.__write('end\n')
    
    # prints the code of of an IfStmt
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
    
    # prints the code of of a SimpleExpr
    def visit_simple_expr(self, simple_expr):
        simple_expr.term.accept(self)
    
    # prints the code of of a ComplexExpr
    def visit_complex_expr(self, complex_expr):
        # if the first part is complex, add parentheses
        if type(complex_expr.first_operand) is ast.ComplexExpr:
            self.__write('(')
        complex_expr.first_operand.accept(self)
        if type(complex_expr.first_operand) is ast.ComplexExpr:
            self.__write(')')
        
        self.__write(' ' + complex_expr.math_rel.lexeme + ' ')
        
        # if the second part is complex, add parentheses
        if type(complex_expr.rest) is ast.ComplexExpr:
            self.__write('(')
        complex_expr.rest.accept(self)
        if type(complex_expr.rest) is ast.ComplexExpr:
            self.__write(')')
    
    # prints the code of of a BoolExpr
    def visit_bool_expr(self, bool_expr):
        # if there are further Boolean expressions, we need parentheses around the whole thing
        if bool_expr.bool_connector != None and bool_expr.rest != None:
            self.__write('(')
        
        if bool_expr.negated:
            self.__write('not ')
        
        # if the current Boolean Expression is more than just one thing, we need parentheses around it
        if bool_expr.bool_rel != None and bool_expr.second_expr != None:
            self.__write('(')
        
        # do the main part
        bool_expr.first_expr.accept(self)
        
        # if the current Boolean Expression is more than just one thing, print the other things
        if bool_expr.bool_rel != None and bool_expr.second_expr != None:
            self.__write(' ' + bool_expr.bool_rel.lexeme + ' ')
            bool_expr.second_expr.accept(self)
            self.__write(')')
        
        # if there are further Boolean expressions, print them
        if bool_expr.bool_connector != None and bool_expr.rest != None:
            self.__write(' ' + bool_expr.bool_connector.lexeme + ' ')
            bool_expr.rest.accept(self)
            self.__write(')')
    
    # prints the code of of an LValue
    def visit_lvalue(self, lval):
        for i, token in enumerate(lval.path):
            if i == len(lval.path) - 1:
                self.__write(token.lexeme)
            else:
                self.__write(token.lexeme + '.')
    
    # prints the code of of a FunParam
    def visit_fun_param(self, fun_param):
        self.__write(fun_param.param_name.lexeme + ': ' +
                fun_param.param_type.lexeme)
    
    # prints the code of of a SimpleRValue
    def visit_simple_rvalue(self, simple_rvalue):
        if type(simple_rvalue.val.lexeme) is str and simple_rvalue.val.lexeme != 'nil':
            self.__write('"' + simple_rvalue.val.lexeme + '"')
        else:
            self.__write(str(simple_rvalue.val.lexeme)) # have to cast the lexeme because it might not be a string here
    
    # prints the code of of a NewRValue
    def visit_new_rvalue(self, new_rvalue):
        self.__write('new ' + new_rvalue.struct_type.lexeme)
    
    # prints the code of of a CallRValue
    def visit_call_rvalue(self, call_rvalue):
        self.__write(call_rvalue.fun.lexeme + '(')
        for i, expr in enumerate(call_rvalue.args):
            expr.accept(self)
            if i != len(call_rvalue.args) - 1:
                self.__write(', ')
        self.__write(')')
    
    # prints the code of of an IDRValue
    def visit_id_rvalue(self, id_rvalue):
        for i, token in enumerate(id_rvalue.path):
            if i == len(id_rvalue.path) - 1:
                self.__write(token.lexeme)
            else:
                self.__write(token.lexeme + '.')
