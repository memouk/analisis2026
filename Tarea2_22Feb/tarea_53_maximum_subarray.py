"""
Ejercicio de la semana — Maximum Subarray (LeetCode 53)
https://leetcode.com/problems/maximum-subarray/

Subarreglo contiguo con suma máxima.
"""

from typing import List


# --- Fuerza bruta (todos los subarreglos) ---
#
# Idea: probar cada par (inicio, fin) con i <= j y sumar nums[i..j].
# Complejidad tiempo: O(n^2) con n = len(nums) (dos bucles anidados).
# Complejidad espacio: O(1) adicional si acumulas la suma en una variable.
#
# Variante O(n^3): para cada (i, j) recalcular la suma con un tercer bucle;
# es más lenta y no aporta claridad extra si ya tienes la versión O(n^2).


def max_subarray_bruteforce(nums: List[int]) -> int:
    if not nums:
        raise ValueError("nums no puede estar vacío según el enunciado de LeetCode")

    best = nums[0]
    for i in range(len(nums)):
        run = 0
        for j in range(i, len(nums)):
            run += nums[j]
            best = max(best, run)
    return best


# --- Kadane (una pasada) ---
#
# Idea: en cada posición, el mejor subarreglo que termina aquí o bien empieza
# de nuevo en nums[i], o bien extiende el mejor que terminaba en i-1.
# Relación: ending = max(nums[i], ending + nums[i]); global_max = max(global_max, ending)
#
# Complejidad tiempo: O(n)
# Complejidad espacio: O(1)


def max_subarray_kadane(nums: List[int]) -> int:
    if not nums:
        raise ValueError("nums no puede estar vacío según el enunciado de LeetCode")

    best = nums[0]
    ending = nums[0]
    for i in range(1, len(nums)):
        ending = max(nums[i], ending + nums[i])
        best = max(best, ending)
    return best


class Solution:
    """Misma lógica que Kadane; coincide con lo que conviene enviar a LeetCode."""

    def maxSubArray(self, nums: List[int]) -> int:
        return max_subarray_kadane(nums)


if __name__ == "__main__":
    ejemplo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    esperado = 6

    assert max_subarray_bruteforce(ejemplo) == esperado
    assert max_subarray_kadane(ejemplo) == esperado
    assert Solution().maxSubArray(ejemplo) == esperado

    assert Solution().maxSubArray([1]) == 1
    assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23

    print("Pruebas locales 53: OK (bruteforce y Kadane coinciden)")
