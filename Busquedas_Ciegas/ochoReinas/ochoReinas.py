import time
def queens(n):
    result = []
    def backtrack(queens, xy_diff, xy_sum):
        #print(f"Reinas: {queens}\n xy_dif: {xy_diff}\n xy_sum: {xy_sum}")
        #time.sleep(2.3)
        if not result:
            i = len(queens)
            if i == n:
                result.append(queens)
                return
            for j in range(n):
            
                
                if j not in queens and i-j not in xy_diff and i+j not in xy_sum:
                    backtrack(queens+[j], xy_diff+[i-j], xy_sum+[i+j])
    backtrack([0], [], [])
    return result

# Ejemplo de uso:
solutions = queens(8)
print(solutions)
