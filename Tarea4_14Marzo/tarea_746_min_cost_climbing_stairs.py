"""
Tarea – Programación dinámica
Ejercicio 2: Min Cost Climbing Stairs (LeetCode 746)
https://leetcode.com/problems/min-cost-climbing-stairs/

Puedes empezar en el escalón 0 o 1. Desde el escalón i pagas cost[i] y subes 1 o 2 escalones.
El objetivo es llegar “arriba” (más allá del último índice) con costo mínimo.
"""

from typing import List


# Subproblema:
#   Sea dp[i] el costo mínimo total para estar de pie en el escalón i
#   (habiendo pagado cost[i] al llegar a ese escalón; el enunciado de LeetCode
#   equivale a: pagas al salir de i; la misma recurrencia clásica se escribe así).

# Relación de recurrencia:
#   dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])   para i >= 2
#   Llegas a i desde i-1 o i-2 y pagas el costo del escalón en el que quedas.

# Casos base:
#   dp[0] = cost[0]
#   dp[1] = cost[1]
#   (Puedes empezar en 0 o 1 sin costo previo.)

# Respuesta:
#   min(dp[n - 1], dp[n - 2]) porque desde el penúltimo o el último escalón
#   puedes saltar al “techo” en uno o dos pasos.

# Complejidad:
#   Tiempo: O(n)
#   Espacio: O(1) con dos variables en lugar del vector dp completo.


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, cur

        return min(prev1, prev2)


if __name__ == "__main__":
    sol = Solution()
    assert sol.minCostClimbingStairs([10, 15, 20]) == 15
    assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert sol.minCostClimbingStairs([0, 0]) == 0
    print("Pruebas locales 746: OK")
