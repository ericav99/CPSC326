# Author: Maxwell Sherman
# Course: CPSC 326, Spring 2019
# Assignment: 7
# Description:
#   SymbolTable class, used for type checking
#   and interpretation
#----------------------------------------------

# a symbol table consists of a stack of environments, 
# where each environment maps a (variable) name
# to its associated information
class SymbolTable(object):
    # init method
    def __init__(self):
        self.scopes = []   # list of {id_name: info}
        self.env_id = None # current environment in use
    
    # get the index of the current environment
    def __get_env_index(self):
        for i, scope in enumerate(self.scopes):
            if self.env_id == id(scope):
                return i
    
    # returns first the environment where an identifier (name) is found
    def __environment(self, name):
        # search from last (most recent) to first environment
        index = self.__get_env_index()
        for i in range(index, -1, -1):
            if name in self.scopes[i]:
                return self.scopes[i]
    
    # returns whether or not an environment exists in the table
    def id_exists(self, identifier):
        return self.__environment(identifier) != None
    
    # adds a variable ID to the most recent environment with no info
    def add_id(self, identifier):
        if not self.scopes: # can't add if no environment
            return
        
        # add to the most recently added environment
        self.scopes[self.__get_env_index()][identifier] = None
    
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
        new_scope = {}
        if len(self.scopes) == 0:
            self.scopes.append(new_scope)
        else:
            index = self.__get_env_index()
            if index == len(self.scopes) - 1:
                self.scopes.append(new_scope)
            else:
                self.scopes.insert(index + 1, new_scope)
        self.env_id = id(new_scope)
    
    # get current environment id
    def get_env_id(self):
        return self.env_id
    
    # set current environment id
    def set_env_id(self, env_id):
        self.env_id = env_id
    
    # pop an environment from the table
    def pop_environment(self):
        if len(self.scopes) > 0:
            return
        index = self.__get_env_index()
        del self.scopes[index]
        if index > 0:
            self.env_id = id(self.scopes[index - 1])
        else:
            self.env_id = None
    
    # str method
    def __str(self):
        s = ''
        for i, scope in enumerate(self.scopes):
            s += ' '*i + str(id(scope)) + ': ' + str(scope) + '\n'
        return s