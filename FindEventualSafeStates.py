class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        l = len(g)
        v=[None]*l
        u=[0]*l


        for i in range(l):
            if(u[i]==0):
                v[i]=True
                self.DFS(i,v,g,u)
                v[i]=False
        
        ans=[]

        for i in range(len(u)):
            if(u[i]==1):
                ans.append(i)
        
        return ans



    def DFS(self, node: int, v: List[bool], g: List[List[int]], u: List[int]) -> bool:


        safe =True

        for i in g[node]:
            if(v[i] or u[i] ==2):
                safe=False
                break

            if(u[i]==1):
                continue
            v[i]=True
            if not self.DFS(i,v,g,u):
                safe = False
            v[i]=False
        if(safe):
            u[node]=1
        else:
            u[node]=2

        return safe 