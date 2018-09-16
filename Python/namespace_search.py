# put your python code here

def task1():
	#print("Function task1")
	list_global = []
	list_global.append('global')
	request = input().split()
	num_request = int(request[0])
	#print("Next %d cycles" % num_request)
	for i in range(num_request):
		request = input().split()
		#print("request -> comand %s\t namespace %s\t variable %s" % (request[0], request[1], request[2])) 
		if request[0] == 'get':
		    getVariableFromNamespace(list_global, request[1], request[2], list_global, 'global')
		elif request[0] == 'add':
		    addVariable(list_global, request[1], request[2], list_global)
		elif request[0] == 'create':
		    searchAndCreateNamespace(list_global, request[1], request[2], list_global)
	#print(list_global)
    
def searchAndCreateNamespace(search_in, namespace_parents, namespace_create, list_global):
    #print("Function addNamespace")
    for i in search_in:
        if type(search_in[0]) is not list and i == namespace_parents:
            name = str(namespace_create)
            namespace_create = []
            namespace_create.append(name)
            search_in.append(namespace_create)
            #print(list_global)
            return
        elif type(i) is list and i[0] == namespace_parents:
            temp = []
            temp.append(namespace_create)
            i.append(temp)
            #print(list_global)
            return			
        elif type(i) is list:
            searchAndCreateNamespace(i, namespace_parents, namespace_create, list_global)
                

def addVariable(search_in, namespace_for_add, variable, list_global):
    #print("Function addVariable")
    for i in search_in:
        #print("search %s in %s" % (i, search_in))
        if type(i) is not list and i == namespace_for_add:
            search_in.append(variable)
            #print(list_global)
            return
        elif type(i) is list and i[0] == namespace_for_add:
            i.append(variable)
            #print(list_global)
            return			
        elif type(i) is list:
            addVariable(i, namespace_for_add, variable, list_global)


def getVariableFromNamespace(search_in, namespace_variable, variable, list_global, backward_namespace = None):	
    #print("Function getVariable")
    for i in search_in:
        if type(i) is not list and i == namespace_variable:
            if search_in.count(variable) >= 1:
                print(search_in[0])
                return #search_in[0]
            elif search_in.count(variable) == 0:
                 if search_in[0] == 'global':
                     print("None")
                     return #None
                 else:
                     #print("Rename namespace_variable from %s to %s" % (namespace_variable, backward_namespace))
                     getVariableFromNamespace(list_global, backward_namespace, variable, list_global, 'global') 
        if type(i) is list:
            #print("recursia from %s to %s" % (search_in, i))
            getVariableFromNamespace(i, namespace_variable, variable, list_global, search_in[0])	
        

