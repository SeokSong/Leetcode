class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for classes in prerequisites:
            graph[classes[0]].append(classes[1])

        visited  = set()

        def hasCycle(curr, stack):
            if curr in visited:
                if curr in stack:
                    return True
                return False
            
            visited.add(curr)
            stack.append(curr)

            for newCurr in graph[curr]:
                if hasCycle(newCurr, stack):
                    return True
            
            stack.pop()
            return False


        
        for i in range(numCourses):
            if hasCycle(i, []):
                return False
        return True
            

# given a int n numCourses and 2d array prerequisites where prerequisites [i] -> [A_i, B_i] where class B_i is a prereq for class A_i

# This is a directional graph 

# return True if you can finish all course and return False if you cannot finish all classes.

# When can you not finish all classes

# [A_1, B_2] [B_2, A_1]

# This represented in graph form is A_1 <-> B_2
# The reason this is not valid is because the classes are prereq of each other. Another way of staying this is this is a cycle, its easier to visualize with 1 more node

# [A_1, C_2] [C_2, B_2], [B_2, A_2]

# A_1 -> C_2
# <-
# 	B_2

# Now we can see the cycle a little easier with 3 nodes

# Now that we know this is a cycle detection question. We must think how to implement 


#  First we have a make a graph from the prerequisites (adj list) so that we can implement cycle detection as it is much easier on a graph vs a adj list

# For each course we must check for a cycle

# How will we check for a cycle?

# We will have a global visited and a stack that represents a “local visited”. Just like many other graph questions we need a base case, in this case it will be able if we have seen the node before. Fist have we seen it in the global visited? If we have seen the node before, we need to first check if we saw it globally or locally. If we have only seen it globally, then we can return since we know this node previously didnt have a cycle so we can assume it still doesnt have a cycle. If the node is seen in the local visited, then this is a cycle. Now whenever we havent seen the node globally or locally, then we will add this to global and local visited and look at that nodes adj nodes. Once we go through all the adj nodes we pop this from the local since we have confirmed this node does not create any cycles. The text highlighted in green is what allows this code to run O(n). DP questions are fast because they have a cache in order to not recalculate values, the global visited is treated like our cache, once its in global and not in local, it tells us that this if we have not seen a cycle by now, this new node is guaranteed to not create a cycle. 
