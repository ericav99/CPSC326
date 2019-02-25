# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 5
# Description:
#   SymbolTable class, used for type checking
#----------------------------------------------

# a symbol table consists of a stack of environments, 
# where each environment maps a (variable) name
# to its associated information
class SymbolTable(object):
    # init method
    def __init__(self):
        self.scopes = [] # list of {id_name: info}
    
    # returns first the environment where an identifier (name) is found
    def __environment(self, name):
        # search from last (most recent) to first environment
        for i in range(len(self.scopes)-1, -1, -1):
            if name in self.scopes[i]:
                return self.scopes[i]
    
    # returns whether or not an environment exists in the table
    def id_exists(self, identifier):
        return self.__environment(identifier) != None
    
    # TODO: documentation
    def add_id(self, identifier):
        if not self.scopes: # can't add if no environment
            return
        
        # add to the most recently added environment
        self.scopes[-1][identifier] = None
    
    # get info from an environment in the table
    def get_info(self, identifier):
        env = self.__environment(identifier)
        if env is not None:
            return env[identifier]
    
    # set info of an environment in the table
    def set_info(self, identifier, info):
        env = self.__environment(identifier)
        if env is not None:
            env[identifier] = info
    
    # push an environment to the table
    def push_environment(self):
        self.scopes.append({})
    
    # pop an environment from the table
    def pop_environment(self):
        if len(self.scopes) > 0:
            self.scopes.pop()
    
    # str method
    def __str(self):
        return str(self.scopes)
