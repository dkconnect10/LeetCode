class Solution:
    def nearestDrone(self, drones, target) :
        best_dist = float('inf')
        answer = -1

        for i in range(len(drones)):
            dist = abs(drones[i][0]-target[0])+abs(drones[i][1]-target[1])
            if dist<=drones[i][2]:
                if dist < best_dist:
                    best_dist = dist
                    answer =i
        return answer        
            
        