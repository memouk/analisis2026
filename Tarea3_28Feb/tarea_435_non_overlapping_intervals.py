"""
Tarea 3 — Algoritmos voraces (Greedy)
LeetCode 435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/

Mínimo de intervalos a eliminar para que el resto no se solape.
En LeetCode, [1,2] y [2,3] no se solapan (solo se tocan en un punto).
"""

from typing import List


# --- Justificación de la estrategia voraz ---
#
# 1) Ordenar por tiempo de fin (end) ascendente.
#    Mantener el intervalo que termina antes deja el máximo “espacio” libre a la
#    derecha para poder encajar más intervalos después. Es el mismo criterio que
#    maximizar la cantidad de intervalos compatibles; aquí el complemento es
#    minimizar cuántos hay que quitar.
#
# 2) Recorrido en una pasada: guardamos `end` = fin del último intervalo que
#    conservamos en la cadena compatible. Para cada siguiente [s, e]:
#    - Si s >= end, no hay solape con el último conservado: lo aceptamos y
#      actualizamos end = e.
#    - Si s < end, choca con el último conservado: hay que descartar uno.
#      Como los intervalos están ordenados por e creciente, el actual termina
#      al menos tan tarde como el que ya teníamos en la cadena en el conflicto;
#      descartar el actual (contar +1 en eliminaciones y no cambiar end) es
#      seguro y óptimo: conservar el que termina antes nunca empeora la
#      posibilidad futura de encajar más intervalos.
#
# Complejidad:
#   Tiempo: O(n log n) por el ordenamiento (n = len(intervals)); el recorrido es O(n).
#   Espacio: O(1) extra además del arreglo ordenado in-place (el ordenamiento en
#   Python puede usar espacio auxiliar O(n) en el peor caso internamente).


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x: x[1])
        removals = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            if s < end:
                removals += 1
            else:
                end = e

        return removals


if __name__ == "__main__":
    sol = Solution()
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    assert sol.eraseOverlapIntervals([[1, 100], [1, 2], [2, 3]]) == 1
    print("Pruebas locales 435: OK")
