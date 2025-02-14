class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def Create(self, array):
        if not array:
            return None
        nodes = []
        val = array.pop(0)
        self.root = Node(val)
        nodes.append(self.root)
        while len(array) > 0:
            curr = nodes.pop(0)
            left_val = array.pop(0)
            if left_val is not None:
                curr.left = Node(left_val)
                nodes.append(curr.left)
            if len(array) > 0:
                right_val = array.pop(0)
                if right_val is not None:
                    curr.right = Node(right_val)
                    nodes.append(curr.right)
        return self.root





    def printIN(self,array): # print the tree in in-order
        self.Create(array)
        self.helper_printIN(self.root)
    def helper_printIN(self, root):
        if root==None:
            return None
        self.helper_printIN(root.left)
        print(root.data, end=" ")
        self.helper_printIN(root.right)



    def printPOST(self,array): # print the tree in post-order
        self.Create(array)
        self.helper_printPOST(self.root)
    def helper_printPOST(self,root):
        if root is None:
            return None
        self.helper_printPOST(root.left)
        self.helper_printPOST(root.right)
        print(root.data, end=" ")



    def printPRE(self,array): # print the tree in pre-order
        self.Create(array)
        self.helper_printPRE(self.root)
    def helper_printPRE(self,root):
        if root==None:
            return None
        print(root.data, end=" ")
        self.helper_printPRE(root.left)
        self.helper_printPRE(root.right)



    def printLVL(self,array): # print the tree in level order
        self.Create(array)
        if not self.root:
            return None
        queue = [self.root]
        while queue:
            node = queue[0]
            queue = queue[1:]
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)



    def CountNodes(self,array): # count the nodes of a binary tree
        self.Create(array)
        return self.helper_CountNodes(self.root,0)
    def helper_CountNodes(self,root,count):
        if root==None:
            return count
        L = self.helper_CountNodes(root.left,count)
        R = self.helper_CountNodes(root.right,count)
        return 1+L+R



    def invert(self,array): # invert a binary tree
        self.Create(array)
        invROOT = self.helper_invert(self.root)
        if not invROOT:
            return None
        queue = [invROOT]
        while queue:
            node = queue[0]
            queue = queue[1:]
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    def helper_invert(self,root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.helper_invert(root.left)
        self.helper_invert(root.right)
        return root



    def MAXdepth(self,array): # count the maximum depth of a bianry tree
        self.Create(array)
        return self.helper_MAXdepth(self.root)
    def helper_MAXdepth(self,root):
        if not root:
            return 0
        return 1+self.MAX(self.helper_MAXdepth(root.left),
                     self.helper_MAXdepth(root.right))
    def MAX(self,left,right):
        if left>right:
            return left
        else:
            return right



    def MINdepth(self,array): # count the minimum depth of a binary tree
        self.Create(array)
        return self.helper_MINdepth(self.root)
    def helper_MINdepth(self,root):
        if root is None:
            return 0
        if root.left==None:
            return self.helper_MINdepth(root.right)+1
        if root.right==None:
            return self.helper_MINdepth(root.left)+1
        return self.MIN(self.helper_MINdepth(root.left),
                        self.helper_MINdepth(root.right))+1
    def MIN(self,left,right):
        if left<right:
            return left
        else:
            return right



    def getDiameter(self,array): # count diameter of a binary tree
        self.Create(array)
        return self.helper_getDiameter(self.root)
    def helper_getDiameter(self,root):
        if root==None:
            return 0
        L = self.helper_MAXdepth(root.left)
        R = self.helper_MAXdepth(root.right)
        dL = self.helper_getDiameter(root.left)
        dR = self.helper_getDiameter(root.right)
        return self.MAX(L+R,
                        self.MAX(dL,dR))



    def checkBalanced(self,array): # return boolean value if teh binary tree is balanced or not
        self.Create(array)
        return self.helper_checkBalanced(self.root)
    def helper_checkBalanced(self,root):
        if root==None:
            return True
        else:
            lH = self.helper_MAXdepth(root.left)
            rH = self.helper_MAXdepth(root.right)
            return (self.abslt(lH-rH)<=1
            and self.helper_checkBalanced(root.left)
            and self.helper_checkBalanced(root.right))
    def abslt(self,value):
        if value<0:
            return value * -1
        return value



    def checkSame(self,arrayA,arrayB): # check if two tree is same or not
        treeA = BinaryTree()
        treeB = BinaryTree()
        treeA.Create(arrayA)
        treeB.Create(arrayB)
        return self.helper_checkSame(treeA.root, treeB.root)
    def helper_checkSame(self,rootA, rootB):
        if not rootA and not rootB:
            return True
        if (rootA and not rootB) or (rootB and not rootA):
            return False
        else:
            return ((rootA.data==rootB.data)
            and self.helper_checkSame(rootA.left, rootB.left)
            and self.helper_checkSame(rootA.right, rootB.right))



    def isSUB(self,main,sub): # check if the tree is sub tree or not
        treeMAIN = BinaryTree()
        treeSUB = BinaryTree()
        treeMAIN.Create(main)
        treeSUB.Create(sub)
        return self.helper_isSUB(treeMAIN.root,treeSUB.root)
    def helper_isSUB(self,main,sub):
        if not sub:  
            return True
        if not main:  
            return False
        if main.data == sub.data:
            return self.helper_checkIDN(main,sub)
        return (self.helper_isSUB(main.left, sub) 
                or self.helper_isSUB(main.right, sub))

    

    def margeTREE(self,arrayA, arrayB): # marge two binary tree
        treeA = BinaryTree()
        treeB = BinaryTree()
        treeA.Create(arrayA)
        treeB.Create(arrayB)
        newROOT = self.helper_margeTREE(treeA.root,treeB.root)
        if not newROOT:
            return None
        queue = [newROOT]
        while queue:
            node = queue[0]
            queue = queue[1:]
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    def helper_margeTREE(self,root1, root2):
        if root1==None and root2==None:
            return None
        valueX = root1.data if root1 else 0
        valueY = root2.data if root2 else 0
        newROOT = Node(valueX+valueY)
        newROOT.left = self.helper_margeTREE(root1.left if root1 else None,
                                             root2.left if root2 else None)
        newROOT.right = self.helper_margeTREE(root1.right if root1 else None,
                                              root2.right if root2 else None)
        return newROOT



    def pathSUM(self,array,target): # calculate the path sum from root to target node
        self.Create(array)
        return self.helper_pathSUM(self.root,target,0)
    def helper_pathSUM(self,root,target,sum):
        if root==None:
            return None
        sum+=root.data
        if root.data==target:
            return sum
        sumL = self.helper_pathSUM(root.left,target,sum)
        if sumL!=None:
            return sumL
        sumR = self.helper_pathSUM(root.right,target,sum)
        if sumR!=None:
            return sumR
        return None



    def TpathSUM(self,array,target): # return the path/paths which is equal to sum
        self.Create(array)
        output = []
        self.helper_TpathSUM(self.root,target,0,[],output)
        return output
    def helper_TpathSUM(self,root,target,sum,result,output):
        if root==None:
            return None
        sum+=root.data
        result.append(root.data)
        if sum==target:
            output.append(result[:])
        self.helper_TpathSUM(root.left,target,sum,result,output)
        self.helper_TpathSUM(root.right,target,sum,result,output)
        result.pop()



    def MAXpathSUM(self,array): # maximum path sum of a binary tree
        self.Create(array)
        return self.helper_MAXpathSUM(self.root)[-1]
    def helper_MAXpathSUM(self,root):
        if not root:
            return 0, float('-inf')  
        left_sum, left_max = self.helper_MAXpathSUM(root.left)
        right_sum, right_max = self.helper_MAXpathSUM(root.right)
        path_sum = root.data + max(0, left_sum) + max(0, right_sum)
        max_sum_for_this_node = root.data + max(0, left_sum, right_sum)
        global_max = max(left_max, right_max, path_sum)
        return max_sum_for_this_node, global_max



    def leafSM(self,arrayA,arrayB): # check if the leaf nodes are same or not
        treeA = BinaryTree()
        treeB = BinaryTree()
        treeA.Create(arrayA)
        treeB.Create(arrayB)
        leafNODE_a = self.helper_leafSM_a(treeA.root,[])
        leafNODE_b = self.helper_leafSM_b(treeB.root,[])
        return leafNODE_a==leafNODE_b
    def helper_leafSM_a(self,root,leafNODE_A):
        if root==None:
            return None
        if root.left==None and root.right==None:
            leafNODE_A.append(root.data)
        self.helper_leafSM_a(root.left,leafNODE_A)
        self.helper_leafSM_a(root.right,leafNODE_A)
        return leafNODE_A
    def helper_leafSM_b(self,root,leafNODE_B):
        if root==None:
            return None
        if root.left==None and root.right==None:
            leafNODE_B.append(root.data)
        self.helper_leafSM_a(root.left,leafNODE_B)
        self.helper_leafSM_a(root.right,leafNODE_B)
        return leafNODE_B



    def rightV(self,array): # right side view of a binary tree
        self.Create(array)
        result = []
        self.helper_rightV(self.root,result,0)
        return result
    def helper_rightV(self,root,result,level):
        if root==None:
            return None
        if level == len(result):
            result.append(root.data)
        self.helper_rightV(root.right, result, level + 1)
        self.helper_rightV(root.left, result, level + 1)




    def leftV(self,array): # left side view of a binary tree
        self.Create(array)
        result = []
        self.helper_leftV(self.root,result,0)
        return result
    def helper_leftV(self,root,result,level):
        if root==None:
            return None
        if level==len(result):
            result.append(root.data)
        self.helper_leftV(root.left,result,level+1)
        self.helper_leftV(root.right,result,level+1)



    def topV(self,array): # top view of a binary tree
        self.Create(array)
        self.helper_topV(self.root)
    def helper_topV(self,root):
        if not root:
            return
        VIEWpoint = {}  
        queue = [(root, 0)]  
        while queue:
            node, hd = queue.pop(0)  
            if hd not in VIEWpoint:  
                VIEWpoint[hd] = node.data
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        keys = list(VIEWpoint.keys())
        keys.sort()  # Sort the keys manually
        for key in keys:
            print(VIEWpoint[key], end=" ")


    def bottomV(self,array): # bottom view of a binary tree
        self.Create(array)
        self.helper_bottomV(self.root)
    def helper_bottomV(self, root):
        if not root:
            return
        VIEWpoint = {}  
        queue = [(root, 0)]  
        while queue:
            node, hd = queue.pop(0)  
            VIEWpoint[hd] = node.data  
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        keys = list(VIEWpoint.keys())
        keys.sort() 
        for key in keys:
            print(VIEWpoint[key], end=" ")


    

    def checkSYM(self,array): # check symmetric tree
        self.Create(array)
        if self.root==None:
            return True
        return self.helper_checkSYM(self.root.left, self.root.right)
    def helper_checkSYM(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return ((left.data==right.data)
                and self.helper_checkSYM(left.left, right.right)
                and self.helper_checkSYM(left.right,right.left))



    def checkCOM(self,array): # check completeness of a binary tree
        self.Create(array)
        if self.root==None:
            return True
        queue = []
        queue.append(self.root)
        seen = False
        while queue:
            node = queue.pop(0)
            if not node:
                seen=True
            else:
                if seen:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True



    def MAXwidth(self,array): # check maximum width of a binary tree
        self.Create(array)
        if not self.root:
            return 0
        queue = [self.root]
        currentWIDE = 0
        while queue:
            currentWIDE = self.MAX(currentWIDE,len(queue))
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return currentWIDE



    def FlipEQ(self,arrayA, arrayB): # check flip equivalent binary tree
        treeA = BinaryTree()
        treeB = BinaryTree()
        treeA.Create(arrayA)
        treeB.Create(arrayB)
        return self.helper_FlipEQ(treeA.root,treeB.root)
    def helper_FlipEQ(self,root1,root2):
        if not root1 and not root2:
            return True
        if root1==None or root2==None or root1.data != root2.data:
            return False
        return ((self.helper_FlipEQ(root1.left, root2.left)
                    and self.helper_FlipEQ(root1.right, root2.right)) or
                        (self.helper_FlipEQ(root1.left, root2.right)
                    and self.helper_FlipEQ(root1.right, root2.left)))



    def FlipCLK(self,array): # flip a tree in clockwise
        self.Create(array)
        return self.helper_FlipCLK(self.root)
    def helper_FlipCLK(self,root):
        if not root or not root.left:
            return root
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        if not new_root:
            return None
        queue = [new_root]
        while queue:
            node = queue[0]
            queue = queue[1:]
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)



    def FlipACLK(self, array):  # Flip a tree in anti-clockwise
        self.Create(array)
        modROOT = self.helper_FlipACLK(self.root)
        if not modROOT:
            return None
        queue = [modROOT]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def helper_FlipACLK(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.helper_FlipACLK(root.left)
        self.helper_FlipACLK(root.right)
        return root

        



    def findLv(self,array): # find the largest value of a binary tree
        self.Create(array)
        MAX=float("-inf")
        return self.helper_findLv(self.root,MAX)
    def helper_findLv(self,root,MAX):
        if root==None:
            return MAX
        if root.data>MAX:
            MAX=root.data
        MAX = self.helper_findLv(root.left,MAX)
        MAX = self.helper_findLv(root.right,MAX)
        return MAX



    def findSv(self,array): # find the smallest value of a binary tree
        self.Create(array)
        MIN=float("inf")
        return self.helper_findSv(self.root,MIN)
    def helper_findSv(self,root,MIN):
        if root==None:
            return MIN
        if root.data<MIN:
            MIN=root.data
        MIN = self.helper_findSv(root.left,MIN)
        MIN = self.helper_findSv(root.right,MIN)
        return MIN

    def deleteNODE(self,array,target): # delete node from a binary tree
        self.Create(array)
        if not self.root:
            return None
        queue = [self.root]
        targetNODE = None
        lstNODE = None
        while queue:
            lstNODE = queue.pop(0)
            if lstNODE.data == target:
                targetNODE = lstNODE
            if lstNODE.left:
                queue.append(lstNODE.left)
            if lstNODE.right:
                queue.append(lstNODE.right)
        if not targetNODE:
            return None
        targetNODE.data = lstNODE.data
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.left == lstNODE:
                curr.left = None
                return
            elif curr.right == lstNODE:
                curr.right = None
                return
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)



    def addNODE(self,array,node): # add node in a binary tree
        self.Create(array)
        if not self.root:
            self.root = Node(node)
            return
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if not curr.left:
                curr.left = Node(node)
                return
            else:
                queue.append(curr.left)
            if not curr.right:
                curr.right = Node(node)
                return
            else:
                queue.append(curr.right)



    def Serialize(self,array): # serialize a binary tree
        self.Create(array)
        if not self.root:
            return []
        queue = [self.root]
        result = []
        while queue:
            curr = queue.pop(0)
            if curr:
                result.append(curr.data)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result



    def Deserialize(self,array): # deserialize a binary tree
        if not array:
            self.root = None
            return None

        self.root = Node(array[0])
        queue = [self.root]
        i = 1
        while i < len(array):
            curr = queue.pop(0)

            if i < len(array) and array[i] is not None:
                curr.left = Node(array[i])
                queue.append(curr.left)
            i += 1

            if i < len(array) and array[i] is not None:
                curr.right = Node(array[i])
                queue.append(curr.right)
            i += 1
        if not self.root:
            return None
        queue = [self.root]
        while queue:
            node = queue[0]
            queue = queue[1:]
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    def checkIDN(self,arrayA, arrayB): # check if two binary tree is identical or not
        treeA = BinaryTree()
        treeB = BinaryTree()
        treeA.Create(arrayA)
        treeB.Create(arrayB)
        return self.helper_checkIDN(treeA.root,treeB.root)
    def helper_checkIDN(self,root1,root2):
        if not root1 and not root2:
            return True
        if (root1 and root2) and (root1.data==root2.data):
            Ls = self.helper_checkIDN(root1.left,root2.left)
            Rs = self.helper_checkIDN(root1.right,root2.right)
            if Ls and Rs:
                return True
            return False



    def CLDsum(self,array): # children sum property
        self.Create(array)
        return self.helper_CLDsum(self.root)
    def helper_CLDsum(self,root):
        if not root or (root.left==None and root.right==None):
            return True
        Lv = 0
        Rv = 0
        if root.left:
            Lv = root.left.data
        if root.right:
            Rv = root.right.data
        if root.data==Lv+Rv:
            return (self.helper_CLDsum(root.left)
                and self.helper_CLDsum(root.right))
        return False



    def getCLD(self,array,target): # get all the children of a node
        self.Create(array)
        root = self.returnNODE(self.root,target)
        if root:
            return self.helper_getCLD(root,target)
    def helper_getCLD(self,root,target):
        result = []
        if root==None:
            return None
        if root.data==target:
            if root.left:
                result.append(root.left.data)
            if root.right:
                result.append(root.right.data)
        return result



    def KthNODE(self, array, K):  # fetch the kth away node
        self.Create(array)
        result = self.helper_KthNODE(self.root, K)
        print(result)
    def helper_KthNODE(self, root, K):
        if root is None:
            return None
        if K == 0:
            return root.data
        left_result = self.helper_KthNODE(root.left, K - 1)
        if left_result is not None:
            return left_result
        return self.helper_KthNODE(root.right, K - 1)




    def getLVL(self,array,target): # get the level of a node in bianry tree
        self.Create(array)
        return self.helper_getLVL(self.root,target,level=0)
    def helper_getLVL(self,root,target,level):
        if root==None:
            return-1
        if root.data==target:
            return level
        Ls = self.helper_getLVL(root.left,target,level+1)
        if Ls!=-1:
            return Ls
        return self.helper_getLVL(root.right,target,level+1)


    def checkFLD(self,array): # check if a binary tree is foldable or not
        self.Create(array)
        if self.root is None:
            return True
        return self.helper_checkFLD(self.root.left,self.root.right)
    def helper_checkFLD(self,left,right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        return (self.helper_checkFLD(left.left, right.right)
                and self.helper_checkFLD(left.right, right.left))



    def checkMIR(self,arrayA,arrayB): # check if two trees are mirror or not
        treeA = BinaryTree()
        treeB = BinaryTree()
        treeA.Create(arrayA)
        treeB.Create(arrayB)
        return self.helper_checkMIR(treeA.root,treeB.root)
    def helper_checkMIR(self,root1,root2):
        if root1==None and root2==None:
            return True
        if root1==None or root2==None:
            return False
        return ((root1.data==root2.data)
                and self.helper_checkMIR(root1.left, root2.right)
                and self.helper_checkMIR(root1.right, root2.left))



    def checkPRF(self,array): # check if a binary tree is perfect or not
        self.Create(array)
        DEPTH = self.depth(self.root)
        return self.helper_checkPRF(self.root,DEPTH)
    def helper_checkPRF(self,root,depth,level=0):
        if root.left==None and root.right==None:
            return depth==level+1
        if root.left==None or root.right==None:
            return False
        return (self.helper_checkPRF(root.left,depth,level+1)
                    and self.helper_checkPRF(root.right,depth,level+1))
    def depth(self,node):
        result = 0
        while node:
            result+=1
            node = node.left
        return result



    def checkCSN(self,array,node1,node2): # check if two nodes are cousin or not
        self.Create(array)
        return self.helper_checkCSN(self.root,node1,node2)
    def helper_checkCSN(self,root,node1,node2):
        lvlN1 = self.helper_getLVL(root,node1,level=0)
        lvlN2 = self.helper_getLVL(root,node2,level=0)
        prntN1 = self.helper_getPNT(root,node1)
        prntN2 = self.helper_getPNT(root,node2)
        return (lvlN1==lvlN2
                and prntN1!=prntN2)



    def LCA(self,array,node1,node2): # find the lowest common ancestor of a binary tree
        self.Create(array)
        return self.helper_LCA(self.root,node1,node2).data
    def helper_LCA(self,root,node1,node2):
        if root is None:
            return None
        if root.data==node1 or root.data==node2:
            return root
        Ls = self.helper_LCA(root.left,node1,node2)
        Rs = self.helper_LCA(root.right,node1,node2)
        if Ls and Rs:
            return root
        return Ls if Ls else Rs



    def printANC(self,array,target): # print all the ancestors of a node
        self.Create(array)
        result = []
        self.helper_printANC(self.root,target,result)
        return result
    def helper_printANC(self,root,target,result):
        if root is None:
            return False
        if root.data == target:
            return True
        Ls = self.helper_printANC(root.left, target, result)
        Rs = self.helper_printANC(root.right, target, result)
        if Ls or Rs:
            result.append(root.data)
            return True
        return False



    def printDANC(self,array,target): # print all the descendants of a node
        self.Create(array)
        root = self.returnNODE(self.root,target)
        result = []
        return self.helper_printDNC(root,result)
    def returnNODE(self,root,target):
        if root==None:
            return None
        if root.data==target:
            return root
        Lr = self.returnNODE(root.left,target)
        if Lr:
            return Lr
        return self.returnNODE(root.right,target)
    def helper_printDNC(self,root,result):
        if root==None:
            return None
        if root.left:
            result.append(root.left.data)
            self.helper_printDNC(root.left,result)
        if root.right:
            result.append(root.right.data)
            self.helper_printDNC(root.right,result)
        return result



    def findDST(self,array,node1,node2): # find the distance between two nodes
        self.Create(array)
        return self.helper_findDST(self.root,node1,node2)
    def helper_findDST(self,root,node1,node2):
        lca = self.helper_LCA(root,node1,node2)
        if not lca:
            return -1
        dstA = self.helper_getLVL(lca,node1,0)
        dstB = self.helper_getLVL(lca,node2,0)
        return dstA+dstB



    def checkFULL(self,array): # check if a binary tree is full binary tree or not
        self.Create(array)
        return self.helper_checkFULL(self.root)
    def helper_checkFULL(self,root):
        if root==None:
            return True
        if not root.left and not root.right:
            return True
        if root.left and root.right:
            return self.helper_checkFULL(root.left) and self.helper_checkFULL(root.right)



    def changeNODE(self,array,prev,new): # Update a node by value
        self.Create(array)
        update = self.helper_changeNODE(self.root,prev,new)
        if not update:
            return None
        queue = [update]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    def helper_changeNODE(self,root,prev,new):
        if root==None:
            return None
        if root.data==prev:
            root.data = new
        self.helper_changeNODE(root.left,prev,new)
        self.helper_changeNODE(root.right,prev,new)
        return root



    def findDNST(self,array): # find the density of a binary tree
        self.Create(array)
        height = self.helper_MAXdepth(self.root)
        totalNodes = self.helper_CountNodes(self.root,0)
        return totalNodes/height



    def getPNT(self,array,target): # get parent of a given node
        self.Create(array)
        return self.helper_getPNT(self.root,target)
    def helper_getPNT(self,root,target):
        if root==None or root.data==target:
            return None
        if root.left and root.left.data==target:
            return root.data
        if root.right and root.right.data==target:
            return root.data
        temp = self.helper_getPNT(root.left,target)
        if temp:
            return temp
        return self. helper_getPNT(root.right,target)



    def getSIB(self,array): # get all the siblings of a node in binary tree
        self.Create(array)
        result = {}
        if not self.root:
            return None
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left and node.right:
                result[node.left.data] = node.right.data
                result[node.right.data] = node.left.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result



    def checkAVL(self, array):  # Check if the tree is an AVL tree
        self.Create(array)
        return self.helper_checkAVL(self.root)[0]
    def helper_checkAVL(self, root):
        if root is None:
            return True, 0
        left_balanced, left_height = self.helper_checkAVL(root.left)
        if not left_balanced:
            return False, 0
        right_balanced, right_height = self.helper_checkAVL(root.right)
        if not right_balanced:
            return False, 0
        if abs(left_height - right_height) > 1:
            return False, 0
        return True, max(left_height, right_height) + 1



    def checkBST(self,array): # check the given tree is a bst or not
        self.Create(array)
        return self.helper_checkBST(self.root,float("-inf"),float("inf"))
    def helper_checkBST(self,root,MIN,MAX):
        if root==None:
            return True
        if not(MIN<root.data<MAX):
            return False
        return ((self.helper_checkBST(root.left,MIN,root.data))
                and (self.helper_checkBST(root.right,root.data,MAX)))



    def rTOn(self,array,target): # distance from root to node of a binary tree
        self.Create(array)
        return self.helper_rTOn(self.root,target)
    def helper_rTOn(self,root,target):
        if not root:
            return -1
        queue = [(root,0)]
        while queue:
            node,depth = queue.pop(0)
            if node.data==target:
                return depth
            if node.left:   
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))

