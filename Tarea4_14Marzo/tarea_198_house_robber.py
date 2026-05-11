"""
Tarea – Programación dinámica
Ejercicio 1: House Robber (LeetCode 198)
https://leetcode.com/problems/house-robber/

No puedes robar dos casas adyacentes; maximiza la suma robada.
"""

from typing import List



# Subproblema:
#   Sea dp[i] la máxima ganancia robando considerando solo las casas con índices 0..i
#   (es decir, el óptimo al “cerrar” el prefijo hasta la casa i).

# Relación de recurrencia:
#   dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
#   Interpretación: en la casa i o no la robas. Si no la robas, te quedas con dp[i-1];
#   si la robas, no puedes haber robado la i-1, así que sumas nums[i] al mejor
#   resultado hasta i-2.

# Casos base:
#   dp[0] = nums[0]
#   dp[1] = max(nums[0], nums[1])

# Complejidad:
#   Tiempo: O(n) con n = len(nums), un paso por índice.
#   Espacio: O(1) si solo guardas dos acumulados (prev2, prev1) en lugar del arreglo completo.


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cur = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, cur

        return prev1


if __name__ == "__main__":
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
    assert sol.rob([5]) == 5
    assert sol.rob([1, 2]) == 2
    print("Pruebas locales 198: OK")
