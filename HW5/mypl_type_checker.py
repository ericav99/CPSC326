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

# a MyPL type checker visitor implementation
# regular IDs take the form: type_id -> 'type'
# struct types take the form: type_id -> {v1:t1, ..., vn:tn}
# function types take the form: fun_id -> [[t1, t2, ..., tn], return_type]
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
    
    # raises a descriptive MyPLError given a simple error_msg
    def __error(self, error_msg, error_token):
        s = error_msg + ', found "' + error_token.lexeme + '" in type checker'
        l = error_token.line
        c = error_token.column
        raise error.MyPLError(s, l, c)
    
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
    
    def visit_var_decl_stmt(self, var_decl): pass
        # TODO
    
    def visit_assign_stmt(self, assign_stmt):
        assign_stmt.rhs.accept(self)
        rhs_type = self.current_type
        assign_stmt.lhs.accept(self)
        lhs_type = self.current_type
        if rhs_type != token.NIL and rhs_type != lhs_type:
            msg = 'mismatched type in assignment'
            self.__error(msg, assign_stmt.lhs.path[0])
    
    def visit_simple_expr(self, simple_expr):
        simple_expr.term.accept(self)
    
    def visit_simple_rvalue(self, simple_rvalue):
        if simple_rvalue.val.tokentype == token.INTVAL:
            self.current_type = token.INTTYPE
        elif simple_rvalue.val.tokentype == token.FLOATVAL:
            self.current_type = token.FLOATTYPE
        elif simple_rvalue.val.tokentype == token.BOOLVAL:
            self.current_type = token.BOOLTYPE
        elif simple_rvalue.val.tokentype == token.STRINGVAL:
            self.current_type = token.STRINGTYPE
        elif simple_rvalue.val.tokentype == token.NIL:
            self.current_type = token.NIL
        else:
            msg = 'this should not happen'
            self.__error(msg, simple_rvalue.val)
    
    def visit_new_rvalue(self, new_rvalue):
        self.current_type = new_rvalue.struct_type.lexeme
    
    def visit_call_rvalue(self, call_rvalue): pass
        # TODO - get the function's return type
    
    def visit_id_rvalue(self, id_rvalue):
        if self.sym_table.id_exists(id_rvalue.path[0].lexeme):
            depth = len(id_rvalue.path)
            if depth > 1:
                self.visit_id_rvalue.helper(id_rvalue.path[1:], self.sym_table.get_info(id_rvalue.path[0]))
            else:
                self.current_type = self.sym_table.get_info(id_rvalue.path[0].lexeme)
        else:
            msg = 'id use before declaration'
            self.__error(msg, id_rvalue.path[0])
    
    def visit_id_rvalue_helper(self, path, current_dict):
        if path[0] in current_dict:
            depth = len(id_rvalue.path)
            if depth > 1:
                self.visit_id_rvalue.helper(path[1:], current_dict[path[0]])
            else:
                self.current_type = self.sym_table.get_info(path[0].lexeme)
        else:
            msg = 'id use before declaration'
            self.__error(msg, path[0].lexeme)
    
    def visit_complex_expr(self, complex_expr):
        complex_expr.first_operand.accept(self)
        left_type = self.current_type
        complex_expr.rest.accept(self)
        right_type = self.current_type
        if left_type == token.NIL or right_type == token.NIL:
            msg = 'nil type in expression'
            self.__error(msg, complex_expr.math_rel) # math rel b/c token needed
        elif left_type == token.INTTYPE and left_type == right_type:
            self.current_type = left_type
        elif (left_type == token.FLOATTYPE and left_type == right_type and
                (complex_expr.math_rel.tokentype == token.PLUS or
                complex_expr.math_rel.tokentype == token.MINUS or
                complex_expr.math_rel.tokentype == token.MULTIPLY or
                complex_expr.math_rel.tokentype == token.DIVIDE)):
            self.current_type = left_type
        elif (left_type == token.STRINGTYPE and left_type == right_type and
                complex_expr.math_rel.tokentype == token.PLUS):
            self.current_type = left_type
        elif left_type == token.BOOLTYPE or right_type == token.BOOLTYPE:
            msg = 'boolean in complex expression' # bools should be in boolexpr
            self.__error(msg, complex_expr.math_rel)
        else:
            msg = 'mismatched type in complex expression'
            self.__error(msg, complex_expr.math_rel)
    
    def visit_bool_expr(self, bool_expr):
        bool_expr.first_expr.accept(self)
        if bool_expr.bool_rel != None and bool_expr.second_expr != None:
            first_type = self.current_type
            bool_expr.second_expr.accept(self)
            second_type = self.current_type
            if (bool_expr.bool_rel.tokentype == token.EQUAL or
                    bool_expr.bool_rel.tokentype == token.NOT_EQUAL):
                if (first_type == token.NIL or second_type == token.NIL or
                        first_type == second_type):
                    self.current_type = token.BOOLTYPE
                else:
                    msg = 'mismatched type in boolean expression'
                    self.__error(msg, bool_expr.bool_rel) # bool rel b/c token needed
            elif (bool_expr.bool_rel.tokentype == token.GREATER_THAN or
                    bool_expr.bool_rel.tokentype == token.LESS_THAN or
                    bool_expr.bool_rel.tokentype == token.GREATER_THAN_EQUAL or
                    bool_expr.bool_rel.tokentype == token.LESS_THAN_EQUAL):
                if ((first_type == token.INTTYPE or
                        first_type == token.FLOATTYPE or
                        first_type == token.BOOLTYPE or
                        first_type == token.STRINGTYPE) and
                        (second_type == token.INTTYPE or
                        second_type == token.FLOATTYPE or
                        second_type == token.BOOLTYPE or
                        second_type == STRINGTYPE)):
                    if first_type == second_type:
                        self.current_type = token.BOOLTYPE
                    else:
                        msg = 'mismatched type in boolean expression'
                        self.__error(msg, bool_expr.bool_rel)
                else:
                    msg = 'invalid comparison type'
                    self.__error(msg, bool_expr.bool_rel)
        else:
            self.current_type = token.BOOLTYPE
        
        if bool_expr.bool_connector != None and bool_expr.rest != None:
            left_type = self.current_type
            bool_expr.rest.accept(self)
            right_type = self.current_type
            if (bool_expr.bool_connector.tokentype == token.AND or
                    bool_expr.bool_connector.tokentype == token.OR):
                if left_type == token.BOOLTYPE and left_type == right_type:
                    self.current_type = left_type
                else:
                    msg = 'mismatched type in boolean expression'
                    self.__error(msg, bool_expr.bool_connector)
            else:
                msg = 'this should not happen'
                self.__error(msg, bool_expr.bool_connector)
        else:
            self.current_type = token.BOOLTYPE
        
        if bool_expr.negated:
            if self.current_type != token.BOOLTYPE:
                msg = 'mismatched type in negation'
                # just need some nearby token I know exists for the error message
                if type(bool_expr.first_expr) is ast.SimpleExpr:
                    if type(bool_expr.first_expr.term) is ast.SimpleRValue:
                        self.__error(msg, bool_expr.first_expr.term.val)
                    elif type(bool_expr.first_expr.term) is ast.NewRValue:
                        self.__error(msg, bool_expr.first_expr.term.struct_type)
                    elif type(bool_expr.first_expr.term) is ast.CallRValue:
                        self.__error(msg, bool_expr.first_expr.term.fun)
                    else: # ast.IDRValue
                        self.__error(msg, bool_expr.first_expr.term.path[0])
                else: # ast.ComplexExpr
                    self.__error(msg, bool_expr.first_expr.math_rel)
    
    def visit_var_decl_stmt(self, var_decl_stmt):
        given_type = None
        if var_decl_stmt.var_type != None:
            if var_decl_stmt.var_type.tokentype == token.ID:
                given_type = var_decl_stmt.var_type.lexeme
            else:
                given_type = var_decl_stmt.var_type.tokentype
        var_decl_stmt.var_expr.accept(self)
        expr_type = self.current_type
        
        # if explicitly given type and nil expression
        if given_type != None and expr_type == token.NIL:
            # explicitly given type overrides nil expression
            if not self.sym_table.id_exists(var_decl_stmt.var_id.lexeme):
                self.sym_table.add_id(var_decl_stmt.var_id.lexeme)
            self.sym_table.set_info(var_decl_stmt.var_id.lexeme, given_type)
        # if explicitly given type and non-nil expression
        elif given_type != None and expr_type != token.NIL:
            # make sure they match
            if given_type == expr_type:
                if not self.sym_table.id_exists(var_decl_stmt.var_id.lexeme):
                    self.sym_table.add_id(var_decl_stmt.var_id.lexeme)
                self.sym_table.set_info(var_decl_stmt.var_id.lexeme, given_type)
            else:
                msg = 'type mismatch in var declaration'
                self.__error(msg, var_decl_stmt.var_type)
        # if no explicitly given type
        else: # given_type == None
            # make sure expression is non-nil
            if expr_type == token.NIL:
                msg = 'nil declaraction without explicit type'
                self.__error(msg, var_decl_stmt.var_id)
            else:
                if not self.sym_table.id_exists(var_decl_stmt.var_id.lexeme):
                    self.sym_table.add_id(var_decl_stmt.var_id.lexeme)
                self.sym_table.set_info(var_decl_stmt.var_id.lexeme, expr_type)
    
    def visit_assign_stmt(self, assign_stmt):
        depth = len(assign_stmt.lhs.path)
        current_dict = {}
        for i in range(depth):
            if i == 0:
                if i == depth - 1:
                    if self.sym_table.id_exists(assign_stmt.lhs.path[i].lexeme):
                        left_type = self.sym_table.get_info(assign_stmt.lhs.path[i].lexeme)
                        assign_stmt.rhs.accept(self)
                        right_type = self.current_type
                        if left_type == right_type or right_type == token.NIL:
                            self.sym_table.set_info(assign_stmt.lhs.path[i].lexeme, left_type)
                        else:
                            msg = 'type mismatch in assign statement'
                            self.__error(msg, assign_stmt.lhs.path[i])
                else:
                    if self.sym_table.id_exists(assign_stmt.lhs.path[i].lexeme):
                        current_dict = self.sym_table.get_info(assign_stmt.lhs.path[i].lexeme)
                    else:
                        msg = "variable doesn't exist"
                        self.__error(msg, assign_stmt.lhs.path[i])
            else:
                if i == depth - 1:
                    if assign_stmt.lhs.path[i].lexeme in current_dict:
                        left_type = self.sym_table.get_info(assign_stmt.lhs.path[i].lexeme)
                        assign_stmt.rhs.accept(self)
                        right_type = self.current_type
                        if left_type == right_type or right_type == token.NIL:
                            self.sym_table.set_info(assign_stmt.lhs.path[i].lexeme, left_type)
                        else:
                            msg = 'type mismatch in assign statement'
                            self.__error(msg, assign_stmt.lhs.path[i])
                    else:
                        msg = 'variable use before declaration'
                        self.__error(msg, assign_stmt.lhs.path[i])
                else:
                    if assign_stmt.lhs.path[i].lexeme in current_dict:
                        current_dict = assign_stmt.lhs.path[i]
                    else:
                        msg = "variable doesn't exist"
                        self.__error(msg, assign_stmt.lhs.path[i])
    
    def visit_if_stmt(self, if_stmt):
        self.visit_basic_if(if_stmt.if_part)
        for elseif in if_stmt.elseifs:
            self.visit_basic_if(elseif)
        if if_stmt.has_else:
            if_stmt.else_stmts.accept(self)
    
    # this is a helper, not an actual visitor method
    def visit_basic_if(self, basic_if):
        basic_if.bool_expr.accept(self)
        self.sym_table.push_environment()
        basic_if.stmt_list.accept(self)
        self.sym_table.pop_environment()
    
    def visit_while_stmt(self, while_stmt):
        while_stmt.bool_expr.accept(self)
        self.sym_table.push_environment()
        while_stmt.stmt_list.accept(self)
        self.sym_table.pop_environment()
    
    def visit_struct_decl_stmt(self, struct_decl_stmt):
        new_type = struct_decl_stmt.struct_id.lexeme
        self.sym_table.push_environment()
        struct_vars = {}
        for var_decl in struct_decl_stmt.var_decls:
            var_decl.accept(self)
            struct_vars[var_decl.var_id] = self.current_type
        self.sym_table.set_info(new_type, struct_vars)
    
    # TODO: function decls and calls
    
    def visit_fun_decl_stmt(self, struct_decl_stmt): pass
    
    def visit_return_stmt(self, return_stmt): pass
