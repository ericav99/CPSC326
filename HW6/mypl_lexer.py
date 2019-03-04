# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 6
# Description:
#   Lexer class, to be used in hw6.py
#--------------------------------------

import mypl_token as token
import mypl_error as error

# MyPL lexical analyzer (source -> token sequence)
# reads a stream (input file) of MyPL source and returns valid tokens
# raises MyPLError exception when necessary
#
# all tokens and some exceptions return the column of the beginning of the lexeme
class Lexer(object):
    # init method
    def __init__(self, input_stream):
        self.line = 1
        self.column = 0
        self.input_stream = input_stream
    
    # peeks at the next character in the stream
    # returns the character while not advancing the position
    def __peek(self):
        pos = self.input_stream.tell()
        symbol = self.input_stream.read(1)
        self.input_stream.seek(pos)
        return symbol
    
    # reads the next character in the strema
    # returns the character and advances the position
    def __read(self):
        # update line and column numbers
        if self.__peek() == "\n":
            self.line += 1
            self.column = 0
        elif self.__peek() != "": # if not EOS
            self.column += 1
        
        return self.input_stream.read(1)
    
    # returns the next token in the stream
    def next_token(self):
        peekValue = self.__peek() # for efficiency purposes
        
        # check the next character and act from there
        
        # if EOS, return EOS token
        if peekValue == "":
            return token.Token(token.EOS, "", self.line, self.column)
        
        # if digit, determine if float or int, then return
        elif peekValue.isdigit():
            curr_lexeme = self.__read()
            # used to ensure a float only contains one decimal point
            isFloat = False
            
            # read until it's another important character in MyPL or whitespace because people might not put whitespace (ex. x=x+5; )
            # if there is a non-digit character, we'll raise an error in the loop
            while self.__peek() not in ';=+-*/%<>(),"' and not self.__peek().isspace():
                # if not digit or decimal, error
                if not self.__peek().isdigit() and self.__peek() != ".":
                    raise error.MyPLError('unexpected symbol "' + self.__peek() + '"', self.line, self.column)
                
                # if decimal point, ensure this is the first one and that the first half of the number is a valid intval
                elif self.__peek() == "." and not isFloat:
                    if len(curr_lexeme) == 1 or (curr_lexeme[0] != "0" and len(curr_lexeme) > 1):
                        isFloat = True
                    else:
                        raise error.MyPLError("float starts with invalid int", self.line, self.column - (len(curr_lexeme) - 1))
                elif self.__peek() == "." and isFloat:
                    raise error.MyPLError("two decimal points in one number", self.line, self.column)
                
                # if all is well, read the character
                curr_lexeme += self.__read()
            
            # after we have the whole number,
            # verify it's valid and return the corresponding token
            if isFloat:
                # if there is nothing after the decimal point
                if curr_lexeme[-1] == ".":
                    raise error.MyPLError("missing digit in float value", self.line, self.column) # +1 to column to show where digit needs to be
                else:
                    return token.Token(token.FLOATVAL, float(curr_lexeme), self.line, self.column - (len(curr_lexeme) - 1))
            else:
                # check if valid intval
                if len(curr_lexeme) == 1 or (curr_lexeme[0] != "0" and len(curr_lexeme) > 1):
                    return token.Token(token.INTVAL, int(curr_lexeme), self.line, self.column - (len(curr_lexeme) - 1))
                else:
                    # this happens if the number is longer than one digit
                    # and starts with 0
                    # the unexpected symbol will always be the second digit,
                    # even if it's also 0
                    raise error.MyPLError('unexpected symbol "' + curr_lexeme[1] + '"', self.line, self.column - (len(curr_lexeme) - 1))
        
        # if alpha, determine if ID or keyword and return accordingly
        elif peekValue.isalpha():
            curr_lexeme = self.__read()
            # expedites identification if the word has an underscore or digit
            isDefinitelyID = False
            
            # read until something that isn't alphanumeric or underscore
            while self.__peek().isalpha() or self.__peek().isdigit() or self.__peek() == "_":
                if self.__peek().isdigit() or self.__peek() == "_":
                    isDefinitelyID = True
                curr_lexeme += self.__read()
            
            # identify what keyword the token is, or if it's an ID
            if isDefinitelyID:
                return token.Token(token.ID, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "bool":
                return token.Token(token.BOOLTYPE, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "int":
                return token.Token(token.INTTYPE, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "float":
                return token.Token(token.FLOATTYPE, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "string":
                return token.Token(token.STRINGTYPE, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "struct":
                return token.Token(token.STRUCTTYPE, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "and":
                return token.Token(token.AND, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "or":
                return token.Token(token.OR, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "not":
                return token.Token(token.NOT, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "while":
                return token.Token(token.WHILE, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "do":
                return token.Token(token.DO, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "if":
                return token.Token(token.IF, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "then":
                return token.Token(token.THEN, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "else":
                return token.Token(token.ELSE, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "elif":
                return token.Token(token.ELIF, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "end":
                return token.Token(token.END, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "fun":
                return token.Token(token.FUN, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "var":
                return token.Token(token.VAR, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "set":
                return token.Token(token.SET, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "return":
                return token.Token(token.RETURN, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "new":
                return token.Token(token.NEW, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "nil":
                return token.Token(token.NIL, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            elif curr_lexeme == "true" or curr_lexeme == "false":
                return token.Token(token.BOOLVAL, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
            else: # must be ID by process of elimination
                return token.Token(token.ID, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1))
        
        # if whitespace, read past it without doing anything
        elif peekValue.isspace():
            self.__read()
            return self.next_token()
        
        # if semicolon... (first because it's extremely common)
        elif peekValue == ";":
            self.__read()
            return token.Token(token.SEMICOLON, ";", self.line, self.column)
        
        # if quotes, return stringval token
        # need to ensure the opening quotes are closed
        elif peekValue == '"':
            curr_lexeme = ""
            self.__read() # throw out opening quotes
            
            # read and stop before closing quotes or newline or EOS
            while self.__peek() != '"' and self.__peek() != "\n" and self.__peek() != "":
                curr_lexeme += self.__read()
            if self.__peek() == '"': # if it ended with closing quotes
                self.__read()
                return token.Token(token.STRINGVAL, curr_lexeme, self.line, self.column - (len(curr_lexeme) - 1) - 2) # -2 to account for quotes
            elif self.__peek() == "\n":
                raise error.MyPLError("reached newline reading string", self.line, self.column)
            elif self.__peek() == "":
                raise error.MyPLError("reached EOS reading string", self.line, self.column + 1) # +1 to column to show where the closing quotes should be
            else:
                raise error.MyPLError("something strange happened", self.line, self.column)
        
        # if comment, go until the end of the line/file without keeping anything
        elif peekValue == "#":
            while self.__peek() != "\n" and self.__peek() != "":
                self.__read()
            return self.next_token()
        
        # if any other recognized character in MyPL
        elif peekValue == "=":
            self.__read()
            if self.__peek() == "=": # if there is a second "="
                self.__read()
                return token.Token(token.EQUAL, "==", self.line, self.column - 1)
            else:
                return token.Token(token.ASSIGN, "=", self.line, self.column)
        elif peekValue == ",":
            # reading here instead of in the return
            # so that line and column update properly
            self.__read()
            return token.Token(token.COMMA, ",", self.line, self.column)
        elif peekValue == ":":
            self.__read()
            return token.Token(token.COLON, ":", self.line, self.column)
        elif peekValue == "/":
            self.__read()
            return token.Token(token.DIVIDE, "/", self.line, self.column)
        elif peekValue == ".":
            self.__read()
            # a dot will never have numbers after it unless it's a float
            # because IDs cannot start with numbers, and no keywords do either
            # so if we got here, a dot with numbers after is a malformed float
            if self.__peek().isdigit():
                raise error.MyPLError("missing intval before decimal point", self.line, self.column - 1)
            else:
                return token.Token(token.DOT, ".", self.line, self.column)
        elif peekValue == ">":
            self.__read()
            if self.__peek() == "=": # if the next character is "="
                self.__read()
                return token.Token(token.GREATER_THAN_EQUAL, ">=", self.line, self.column - 1)
            else:
                return token.Token(token.GREATER_THAN, ">", self.line, self.column)
        elif peekValue == "<":
            self.__read()
            if self.__peek() == "=": # if the next character is "="
                self.__read()
                return token.Token(token.LESS_THAN_EQUAL, "<=", self.line, self.column - 1)
            else:
                return token.Token(token.LESS_THAN, "<", self.line, self.column)
        elif peekValue == "!":
            self.__read()
            if self.__peek() == "=":
                self.__read()
                return token.Token(token.NOT_EQUAL, "!=", self.line, self.column - 1)
            else:
                raise error.MyPLError('unexpected symbol "!"', self.line, self.column - 1) # -1 to column to go back one since we read it already
        elif peekValue == "(":
            self.__read()
            return token.Token(token.LPAREN, "(", self.line, self.column)
        elif peekValue == ")":
            self.__read()
            return token.Token(token.RPAREN, ")", self.line, self.column)
        elif peekValue == "-":
            self.__read()
            return token.Token(token.MINUS, "-", self.line, self.column)
        elif peekValue == "%":
            self.__read()
            return token.Token(token.MODULO, "%", self.line, self.column)
        elif peekValue == "*":
            self.__read()
            return token.Token(token.MULTIPLY, "*", self.line, self.column)
        elif peekValue == "+":
            self.__read()
            return token.Token(token.PLUS, "+", self.line, self.column)
        
        # if we reach this point, there is something very strange in the source
        else:
            raise error.MyPLError('unexpected symbol "' + peekValue + '"', self.line, self.column)
