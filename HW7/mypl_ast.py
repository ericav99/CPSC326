# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 7
# Description:
#   Abstract Syntax Tree classes, used in the parser
#   to construct the AST
#-----------------------------------------------------

import mypl_token as token

# base class for AST
class ASTNode(object):
    def accept(self, visitor): pass

# base class for all statement nodes
class Stmt(ASTNode):
    def accept(self, visitor): pass

# consists of a list of statements
class StmtList(ASTNode):
    def __init__(self):
        self.stmts = [] # list of Stmt nodes
    
    def accept(self, visitor):
        visitor.visit_stmt_list(self)

# base class for all expression nodes
class Expr(ASTNode):
    def accept(self, visitor): pass

# simple statement that's just an expression
class ExprStmt(Stmt):
    def __init__(self):
        self.expr = None    # Expr node
    
    def accept(self, visitor):
        visitor.visit_expr_stmt(self)

# consists of a variable identifier, (optional) type, and initial value
class VarDeclStmt(Stmt):
    def __init__(self):
        self.var_id = None      # Token (ID)
        self.var_type = None    # Token (STRINGTYPE, ..., ID)
        self.var_expr = None    # Expr node
    
    def accept(self, visitor):
        visitor.visit_var_decl_stmt(self)

# Consists of an identifier and an expression
class AssignStmt(Stmt):
    def __init__(self):
        self.lhs = None # LValue node
        self.rhs = None # Expr node
    
    def accept(self, visitor):
        visitor.visit_assign_stmt(self)

# consists of an identifier and a list of variable declarations
class StructDeclStmt(Stmt):
    def __init__(self):
        self.struct_id = None   # Token (ID)
        self.var_decls = []     # [VarDeclStmt]
    
    def accept(self, visitor):
        visitor.visit_struct_decl_stmt(self)

# consists of an identifier, list of parameters (identifiers w/ types, 
# return type, and list of function body statements
class FunDeclStmt(Stmt):
    def __init__(self):
        self.fun_name = None        # Token (ID)
        self.params = []            # [FunParam]
        self.return_type = None     # Token
        self.stmt_list = StmtList() # StmtList node
    
    def accept(self, visitor):
        visitor.visit_fun_decl_stmt(self)

# consists of a return expression and the corresponding return token
# (for printing line and col numbers)
class ReturnStmt(Stmt):
    def __init__(self):
        self.return_expr = None     # Expr node
        self.return_token = None    # to keep track of location (ex. return;)
    
    def accept(self, visitor):
        visitor.visit_return_stmt(self)

# consists of a condition (Boolean expression) and statement list (body)
class WhileStmt(Stmt):
    def __init__(self):
        self.bool_expr = None       # BoolExpr node
        self.stmt_list = StmtList() # StmtList node
    
    def accept(self, visitor):
        visitor.visit_while_stmt(self)

# consists of a basic 'if' part, (possibly empty) list of elifs, and
# optional else part (represented as a statement list)
class IfStmt(Stmt):
    def __init__(self):
        self.if_part = BasicIf()        # BasicIf node
        self.elseifs = []               # [BasicIf]
        self.has_else = False           # whether or not there's an 'else'
        self.else_stmts = StmtList()    # StmtList node
    
    def accept(self, visitor):
        visitor.visit_if_stmt(self)

# consists of an rvalue
class SimpleExpr(Expr):
    def __init__(self):
        self.term = None    # RValue node
    
    def accept(self, visitor):
        visitor.visit_simple_expr(self)

# consists of an expression, math operator
# and another (possibly complex) expression
class ComplexExpr(Expr):
    def __init__(self):
        self.first_operand = None   # Expr node
        self.math_rel = None        # Token (PLUS, MINUS, etc.)
        self.rest = None            # Expr node
    
    def accept(self, visitor):
        visitor.visit_complex_expr(self)

# consists of an expression, optional Boolean relation and another expression,
# optional 'and'/'or' and additional Boolean expression (recursive)
# this entire thing can be negated, too
class BoolExpr(ASTNode):
    def __init__(self):
        self.first_expr = None      # Expr node
        self.bool_rel = None        # Token (GREATER_THAN, LESS_THAN, etc.)
        self.second_expr = None     # Expr node
        self.bool_connector = None  # Token (AND, OR)
        self.rest = None            # BoolExpr node
        self.negated = False        # whether or not it was negated
    
    def accept(self, visitor):
        visitor.visit_bool_expr(self)

# consists of a simple ID or path expression
class LValue(ASTNode):
    def __init__(self):
        self.path = []              # [Token (ID)] (just one implies a simple var)
    
    def accept(self, visitor):
        visitor.visit_lvalue(self)

# consists of a variable ID and type
class FunParam(Stmt):
    def __init__(self):
        self.param_name = None  # Token (ID)
        self.param_type = None  # Token (STRINGTYPE, INTTYPE, etc.)
    
    def accept(self, visitor):
        visitor.visit_fun_param(self)

# consists of a condition (Boolean expression) and list of statements (body)
class BasicIf(object):
    def __init__(self):
        self.bool_expr = None       # BoolExpr node
        self.stmt_list = StmtList() # StmtList() node

# base class for rvalue nodes
class RValue(ASTNode):
    def accept(self, visitor): pass

# consists of a single primitive value
class SimpleRValue(RValue):
    def __init__(self):
        self.val = None # Token (STRINGVAL, INTVAL, etc.)
    
    def accept(self, visitor):
        visitor.visit_simple_rvalue(self)

# consists of a struct name (ID)
class NewRValue(RValue):
    def __init__(self):
        self.struct_type = None # Token (ID)
    
    def accept(self, visitor):
        visitor.visit_new_rvalue(self)

# consists of a function name (ID) and list of args (expressions)
class CallRValue(RValue):
    def __init__(self):
        self.fun = None # Token (ID)
        self.args = []  # [Expr]
    
    def accept(self, visitor):
        visitor.visit_call_rvalue(self)

# consists of a path of 1+ identifiers
class IDRValue(RValue):
    def __init__(self):
        self.path = []  # [Token (ID)]
    
    def accept(self, visitor):
        visitor.visit_id_rvalue(self)

# base class for AST visitors
# everything here is defined in mypl_print_visitor.py
class Visitor(object):
    def visit_stmt_list(self, stmt_list): pass
    def visit_expr_stmt(self, expr_stmt): pass
    def visit_var_decl_stmt(self, var_decl): pass
    def visit_assign_stmt(self, assigm_stmt): pass
    def visit_struct_decl_stmt(self, struct_decl): pass
    def visit_fun_decl_stmt(self, fun_decl): pass
    def visit_return_stmt(self, return_stmt): pass
    def visit_while_stmt(self, while_stmt): pass
    def visit_if_stmt(self, if_stmt): pass
    def visit_simple_expr(self, simple_expr): pass
    def visit_complex_expr(self, complex_expr): pass
    def visit_bool_expr(self, bool_expr): pass
    def visit_lvalue(self, lval): pass
    def visit_fun_param(self, fun_param): pass
    def visit_simple_rvalue(self, simple_rvalue): pass
    def visit_new_rvalue(self, new_rvalue): pass
    def visit_call_rvalue(self, call_rvalue): pass
    def visit_id_rvalue(self, id_rvalue): pass
