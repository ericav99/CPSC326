# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 6
# Description:
#   Parser class, creates an AST
#   and performs some semantic analysis
#----------------------------------------

import mypl_error as error
import mypl_lexer as lexer
import mypl_token as token
import mypl_ast as ast

# MyPL Parser (runs through token sequence matching it to the MyPL grammar)
# reads a stream (lexer.next_token()) of MyPL tokens
# and stops when there is a syntax problem, raising a MyPLError
class Parser(object):
    # init method
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
    
    # recursively descends the MyPL grammar with each new token
    def parse(self):
        self.__advance() # None -> first token
        # passing in a StmtList node because __stmts() recurses with a StmtList parameter
        stmt_list_node = self.__stmts(ast.StmtList())
        self.__eat(token.EOS, "expected EOS") # this could just be advance(), but it's here to be safe
        return stmt_list_node
    
    # moves to the next token without checking
    def __advance(self):
        self.current_token = self.lexer.next_token()
    
    # moves to the next token if it matches tokentype, else raises an error
    def __eat(self, tokentype, error_msg):
        if self.current_token.tokentype == tokentype:
            self.__advance()
        else:
            self.__error(error_msg)
    
    # raises a descriptive MyPLError given a simple error_msg
    def __error(self, error_msg):
        s = error_msg + ', found "' + self.current_token.lexeme + '" in parser'
        l = self.current_token.line
        c = self.current_token.column
        raise error.MyPLError(s, l, c)
    
    # beginning of recursive descent methods
    # each one will expect to be on the next token and not need to advance
    
    # methods hardly receive arguments
    # this is usually just for recursion
    
    # returns a StmtList node
    def __stmts(self, stmt_list_node):
        # print("stmts: " + str(self.current_token))
        if self.current_token.tokentype != token.EOS:
            stmt_list_node.stmts.append(self.__stmt()) # append Stmt to StmtList node
            self.__stmts(stmt_list_node) # recurse
        return stmt_list_node
    
    # returns a StmtList node
    def __bstmts(self, stmt_list_node):
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
            stmt_list_node.stmts.append(self.__bstmt()) # get the current Stmt node
            stmt_list_node = self.__bstmts(stmt_list_node) # get all the next Stmt node
        return stmt_list_node
    
    # returns any kind of Stmt node
    def __stmt(self):
        # print("stmt: " + str(self.current_token))
        if self.current_token.tokentype == token.STRUCTTYPE:
            return self.__sdecl() # return StructDeclStatement node
        elif self.current_token.tokentype == token.FUN:
            return self.__fdecl() # return FunDeclStmt node
        else:
            return self.__bstmt() # return a different kind of Stmt node
    
    # returns any kind of Stmt node
    def __bstmt(self):
        # print("bstmt: " + str(self.current_token))
        if self.current_token.tokentype == token.VAR:
            return self.__vdecl() # return VarDeclStmt node
        elif self.current_token.tokentype == token.SET:
            return self.__assign() # return AssignStmt node
        elif self.current_token.tokentype == token.IF:
            return self.__cond() # return IfStmt node
        elif self.current_token.tokentype == token.WHILE:
            return self.__while() # return WhileStmt node
        elif self.current_token.tokentype == token.RETURN:
            return self.__exit() # return ReturnStmt node
        else:
            expr_stmt_node = ast.ExprStmt()
            expr_stmt_node.expr = self.__expr()
            self.__eat(token.SEMICOLON, 'expected ";"')
            return expr_stmt_node # return ExprStmt node
    
    # returns a StructDeclStmt node
    def __sdecl(self):
        # print("sdecl: " + str(self.current_token))
        self.__advance() # eat STRUCT (we already know from stmt)
        struct_decl_stmt_node = ast.StructDeclStmt()
        struct_decl_stmt_node.struct_id = self.current_token # StructDeclStmt ID
        self.__eat(token.ID, 'expected ID')
        # passing in an empty list because __vdecls() recurses with a list parameter
        struct_decl_stmt_node.var_decls = self.__vdecls([]) # StructDeclStmt [VarDeclStmt]
        self.__eat(token.END, 'expected "end"')
        return struct_decl_stmt_node
    
    # returns a list of VarDeclStmt nodes
    def __vdecls(self, var_decl_list):
        # print("vdecls: " + str(self.current_token))
        if self.current_token.tokentype == token.VAR:
            var_decl_list.append(self.__vdecl()) # append VarDeclStmt to list
            self.__vdecls(var_decl_list) # recurse
        return var_decl_list
    
    # returns a FunDeclStmt node
    def __fdecl(self):
        # print("fdecl: " + str(self.current_token))
        self.__advance() # eat FUN (we already know from stmt)
        fun_decl_stmt_node = ast.FunDeclStmt()
        fun_decl_stmt_node.return_type = self.current_token # FunDeclStmt return type
        if self.current_token.tokentype == token.NIL:
            self.__advance() # eat NIL (we already know from 1 line up)
        else:
            self.__type()
        fun_decl_stmt_node.fun_name = self.current_token # FunDeclStmt function name
        self.__eat(token.ID, 'expected ID')
        self.__eat(token.LPAREN, 'expected "("')
        fun_decl_stmt_node.params = self.__params()
        self.__eat(token.RPAREN, 'expected ")"')
        # passing in a StmtList node because __bstmts() recurses with a StmtList parameter
        fun_decl_stmt_node.stmt_list = self.__bstmts(ast.StmtList())
        self.__eat(token.END, 'expected "end"')
        return fun_decl_stmt_node
    
    # returns a list of FunParam nodes
    def __params(self):
        # print("params: " + str(self.current_token))
        fun_param_list = []
        if self.current_token.tokentype == token.ID:
            fun_param = ast.FunParam()
            fun_param.param_name = self.current_token
            self.__advance() # eat ID (we already know from 2 lines up)
            self.__eat(token.COLON, 'expected ":"')
            fun_param.param_type = self.__type()
            fun_param_list.append(fun_param) # add first FunParam node to list (if it exists)
            while self.current_token.tokentype == token.COMMA:
                self.__advance() # eat COMMA (we already know from 1 line up)
                fun_param = ast.FunParam() # need to reset fun_param or the objects in the list are connected
                fun_param.param_name = self.current_token
                self.__eat(token.ID, 'expected ID')
                self.__eat(token.COLON, 'expected ":"')
                fun_param.param_type = self.__type()
                fun_param_list.append(fun_param) # add following FunParam nodes to list
        return fun_param_list
    
    # returns a type Token
    def __type(self):
        # print("type: " + str(self.current_token))
        if (self.current_token.tokentype == token.ID or
                self.current_token.tokentype == token.INTTYPE or
                self.current_token.tokentype == token.FLOATTYPE or
                self.current_token.tokentype == token.BOOLTYPE or
                self.current_token.tokentype == token.STRINGTYPE):
            type_token = self.current_token
            self.__advance() # eat (we already know from 1 line up)
            return type_token
        else:
            self.__error('expected type')
    
    # returns a ReturnStmt node
    def __exit(self):
        # print("exit: " + str(self.current_token))
        return_stmt_node = ast.ReturnStmt()
        # the next line just contains the 'return' keyword
        return_stmt_node.return_token = self.current_token # this is useless but part of the documentation
        self.__advance() # eat RETURN (we already know from bstmt)
        if (self.current_token.tokentype == token.STRINGVAL or # check for expr -> rvalue...
                self.current_token.tokentype == token.INTVAL or
                self.current_token.tokentype == token.BOOLVAL or
                self.current_token.tokentype == token.FLOATVAL or
                self.current_token.tokentype == token.NIL or
                self.current_token.tokentype == token.NEW or
                self.current_token.tokentype == token.ID or
                self.current_token.tokentype == token.LPAREN): # check for expr -> LPAREN
            return_stmt_node.return_expr = self.__expr()
        self.__eat(token.SEMICOLON, 'expected ";"')
        return return_stmt_node
    
    # returns VarDeclStmt node
    def __vdecl(self):
        # print("vdecl: " + str(self.current_token))
        self.__advance() # eat VAR (we already know from bstmt and vdecls)
        var_decl_stmt_node = ast.VarDeclStmt()
        var_decl_stmt_node.var_id = self.current_token # VarDeclStmt ID token
        self.__eat(token.ID, 'expected ID')
        var_decl_stmt_node.var_type = self.__tdecl() # VarDeclStmt type token
        self.__eat(token.ASSIGN, 'expected "="')
        var_decl_stmt_node.var_expr = self.__expr() # VarDeclStmt expr token
        self.__eat(token.SEMICOLON, 'expected ";"')
        return var_decl_stmt_node
    
    # returns a type Token, or None if there isn't one
    def __tdecl(self):
        # print("tdecl: " + str(self.current_token))
        if self.current_token.tokentype == token.COLON:
            self.__advance() # eat COLON (we already know from 1 line up)
            return self.__type() # return 
        else:
            return None
    
    # returns an AssignStmt node
    def __assign(self):
        # print("assign: " + str(self.current_token))
        self.__advance() # eat SET (we already know from bstmt)
        assign_stmt_node = ast.AssignStmt()
        assign_stmt_node.lhs = self.__lvalue() # AssignStmt lhs
        self.__eat(token.ASSIGN, 'expected "="')
        assign_stmt_node.rhs = self.__expr() # AssignStmt rhs
        self.__eat(token.SEMICOLON, 'expected ";"')
        return assign_stmt_node
    
    # returns an LValue node
    def __lvalue(self):
        # print("lvalue: " + str(self.current_token))
        lvalue_node = ast.LValue()
        lvalue_node.path.append(self.current_token) # add first lvalue
        self.__eat(token.ID, 'expected ID')
        while self.current_token.tokentype == token.DOT:
            self.__advance() # eat DOT (we already know from 1 line up)
            lvalue_node.path.append(self.current_token) # add following lvalues if they exist
            self.__eat(token.ID, 'expected ID')
        return lvalue_node
    
    # returns an IfStmt node
    def __cond(self):
        # print("cond: " + str(self.current_token))
        self.__advance() # eat IF (we already know from bstmt)
        if_stmt_node = ast.IfStmt()
        if_stmt_node.if_part.bool_expr = self.__bexpr() # IfStmt node -> BasicIf node -> Boolean expression
        self.__eat(token.THEN, 'expected "then"')
        if_stmt_node.if_part.stmt_list = self.__bstmts(ast.StmtList()) # IfStmt node -> BasicIf node -> statement list
        if_stmt_node = self.__condt(if_stmt_node)
        self.__eat(token.END, 'expected "end"')
        return if_stmt_node
    
    # returns a complete IfStmt node given one with a completed "if part"
    def __condt(self, if_stmt_node):
        # print("condt: " + str(self.current_token))
        if self.current_token.tokentype == token.ELIF:
            self.__advance() # eat ELIF (we already know this from 1 line up)
            new_basic_if_node = ast.BasicIf()
            new_basic_if_node.bool_expr = self.__bexpr()
            self.__eat(token.THEN, 'expected "then"')
            new_basic_if_node.stmt_list = self.__bstmts(ast.StmtList())
            if_stmt_node.elseifs.append(new_basic_if_node)
            return self.__condt(if_stmt_node)
        elif self.current_token.tokentype == token.ELSE:
            self.__advance() # eat ELSE (we already know this from 1 line up)
            if_stmt_node.has_else = True
            if_stmt_node.else_stmts = self.__bstmts(ast.StmtList())
            return if_stmt_node
        else:
            return if_stmt_node
    
    # returns a WhileStmt node
    def __while(self):
        # print("while: " + str(self.current_token))
        self.__advance() # eat WHILE (we already know from bstmt)
        while_stmt_node = ast.WhileStmt()
        while_stmt_node.bool_expr = self.__bexpr() # WhileStmt boolean expression
        self.__eat(token.DO, 'expected "do"')
        while_stmt_node.stmt_list = self.__bstmts(ast.StmtList()) # WhileStmt statement list
        self.__eat(token.END, 'expected "end"')
        return while_stmt_node
    
    # returns any kind of Expr node
    def __expr(self):
        # print("expr: " + str(self.current_token))
        first_expr = None # declare here so it can be used in the next conditional block
        if self.current_token.tokentype == token.LPAREN:
            self.__advance() # eat LPAREN (we already know from 1 line up)
            first_expr = self.__expr() # first Expr node
            self.__eat(token.RPAREN, 'expected ")"')
        else:
            first_expr = self.__rvalue() # first Expr node
        
        if (self.current_token.tokentype == token.PLUS or # check for mathrel
                self.current_token.tokentype == token.MINUS or
                self.current_token.tokentype == token.DIVIDE or
                self.current_token.tokentype == token.MULTIPLY or
                self.current_token.tokentype == token.MODULO):
            complex_expr_node = ast.ComplexExpr()
            complex_expr_node.first_operand = first_expr # first Expr node from the block above
            complex_expr_node.math_rel = self.__mathrel() # mathrel Token
            complex_expr_node.rest = self.__expr() # second Expr node from recursion right here
            return complex_expr_node
        else:
            simple_expr_node = ast.SimpleExpr()
            simple_expr_node.term = first_expr # first Expr node form the block above
            return simple_expr_node
    
    # returns a mathrel Token
    def __mathrel(self):
        # print("mathrel: " + str(self.current_token))
        mathrel_token = self.current_token
        self.__advance() # eat (we already know from expr)
        return mathrel_token
    
    # returns any kind of RValue node
    def __rvalue(self):
        # print("rvalue: " + str(self.current_token))
        if (self.current_token.tokentype == token.STRINGVAL or
                self.current_token.tokentype == token.INTVAL or
                self.current_token.tokentype == token.BOOLVAL or
                self.current_token.tokentype == token.FLOATVAL or
                self.current_token.tokentype == token.NIL):
            simple_rvalue_node = ast.SimpleRValue()
            simple_rvalue_node.val = self.current_token
            self.__advance() # eat (we already know from 3-7 lines up)
            return simple_rvalue_node # return SimpleRValue node
        elif self.current_token.tokentype == token.NEW:
            self.__advance() # eat NEW (we already know from 1 line up)
            new_rvalue_node = ast.NewRValue()
            new_rvalue_node.struct_type = self.current_token
            self.__eat(token.ID, 'expected ID')
            return new_rvalue_node # return NewRValue node
        else:
            return self.__idrval() # return a different kind of RValue node
    
    # returns a CallRValue or IDRvalue node
    def __idrval(self):
        # print("idrval: " + str(self.current_token))
        rvalue_id = self.current_token # save this for later in the method
        self.__eat(token.ID, 'expected ID')
        if self.current_token.tokentype == token.LPAREN: # parentheses -> function -> CallRValue node
            call_rvalue = ast.CallRValue()
            call_rvalue.fun = rvalue_id
            self.__advance() # eat LPAREN (we already know from 1 line up)
            call_rvalue.args = self.__exprlist()
            self.__eat(token.RPAREN, 'expected ")"')
            return call_rvalue # return CallRValue
        else: # no parentheses (and maybe dots) -> ID -> IDRValue
            id_rvalue = ast.IDRValue()
            id_rvalue.path.append(rvalue_id) # add first ID to list
            while self.current_token.tokentype == token.DOT:
                self.__advance() # eat DOT (we already know from 1 line up)
                id_rvalue.path.append(self.current_token) # add following IDs to list
                self.__eat(token.ID, 'expected ID')
            return id_rvalue # return IDRValue
    
    # returns a list of Expr nodes
    def __exprlist(self):
        # print("exprlist: " + str(self.current_token))
        expr_list = []
        if (self.current_token.tokentype == token.STRINGVAL or # check for expr -> rvalue...
                self.current_token.tokentype == token.INTVAL or
                self.current_token.tokentype == token.BOOLVAL or
                self.current_token.tokentype == token.FLOATVAL or
                self.current_token.tokentype == token.NIL or
                self.current_token.tokentype == token.NEW or
                self.current_token.tokentype == token.ID or
                self.current_token.tokentype == token.LPAREN): # check for expr -> LPAREN
            expr_list.append(self.__expr())
            while self.current_token.tokentype == token.COMMA:
                self.__advance() # eat COMMA (we already know from 1 line up)
                expr_list.append(self.__expr())
        return expr_list
    
    # returns a BoolExpr node
    def __bexpr(self):
        # print("bexpr: " + str(self.current_token))
        bool_expr_node = ast.BoolExpr()
        if self.current_token.tokentype == token.NOT:
            bool_expr_node.negated = True
            self.__advance() # eat NOT (we already know from 2 lines up)
            bool_expr_node.first_expr = self.__bexpr()
            bool_expr_node = self.__bexprt(bool_expr_node)
        elif self.current_token.tokentype == token.LPAREN:
            self.__advance() # eat LPAREN (we already know from 1 line up)
            bool_expr_node.first_expr = self.__bexpr()
            self.__eat(token.RPAREN, 'expected ")"')
            # fine to not fill bool_rel and second_expr, they're optional
            bool_expr_node = self.__bconnct(bool_expr_node)
        else:
            bool_expr_node.first_expr = self.__expr()
            bool_expr_node = self.__bexprt(bool_expr_node)
        return bool_expr_node
    
    # returns a complete BoolExpr node given one with a completed "first_expr" and "negated"
    # "negated" is optional
    def __bexprt(self, bool_expr_node):
        # print("bexprt: " + str(self.current_token))
        if (self.current_token.tokentype == token.EQUAL or # check for boolrel
                self.current_token.tokentype == token.LESS_THAN or
                self.current_token.tokentype == token.GREATER_THAN or
                self.current_token.tokentype == token.LESS_THAN_EQUAL or
                self.current_token.tokentype == token.GREATER_THAN_EQUAL or
                self.current_token.tokentype == token.NOT_EQUAL):
            bool_expr_node.bool_rel = self.__boolrel()
            bool_expr_node.second_expr = self.__expr()
        # fine to not fill bool_rel and second_expr, they're optional
        bool_expr_node = self.__bconnct(bool_expr_node)
        return bool_expr_node
    
    # returns a complete BoolExpr node given one with a completed "first_expr", "bool_rel", "second_expr", and "negated"
    # "bool_rel", "second_expr", and "negated" are optional
    def __bconnct(self, bool_expr_node):
        # print("bconnct: " + str(self.current_token))
        if self.current_token.tokentype == token.AND:
            bool_expr_node.bool_connector = self.current_token
            self.__advance() # eat AND (we already know from 1 line up)
            bool_expr_node.rest = self.__bexpr()
        elif self.current_token.tokentype == token.OR:
            bool_expr_node.bool_connector = self.current_token
            self.__advance() # eat OR (we already know from 1 line up)
            bool_expr_node.rest = self.__bexpr()
        # fine to not fill connector or rest, they're optional
        return bool_expr_node
    
    # returns a boolrel token
    def __boolrel(self):
        # print("boolrel: " + str(self.current_token))
        bool_rel_token = self.current_token
        self.__advance() # eat (we already know from bexprt)
        return bool_rel_token
