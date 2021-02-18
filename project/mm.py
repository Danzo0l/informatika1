class SKlass:

    def node(d, L = None, R = None) :
        newNode = SKlass ()
        newNode.data = d
        newNode.left = L
        newNode.right = R
        return newNode
    
    def makeTree (s) :
        k= lastOp(s)
        if k < 0:
            Tree = node(s)
        else:
            Tree = node(s[k])
            Tree.left = makeTree(s[:k])
            Tree.right = makeTree(s[k+1:])
        return Tree
    
    def calcTree(Tree) :
        if not Tree.left:
            return int(Tree.data)
        else:
            n1 = calcTree(Tree.left)
            n2 = calcTree(Tree.right)
            return n1+n2
    
    def oper(op, n1, n2) :
        if op == "+":
            return n1+n2
        elif op == "-":
            return n1-n2
        elif op == "*":
            return n1*n2
        else:
            return n1 // n2
    def priority(op) :
        if op in "+-":
            return 1
        if op in "*/":
            return 2
        return 100
    def lastOp(s) :
        minPrt = 50
        k=-1
        for i in range(len(s)) :
            if priority(s[i]) <=minPrt:
                minPrt = priority(s[i])
                k=i
        return k

    def prog():
        '''klkl'''
        print('Task 1')
        s=input('   input ')
        T=makeTree(s)
        print('   output ', calcTree(T))
    