#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    for _ in range(1, n):
        tria = triangles[-1]
        holder = [1]

        for i in range(len(tria) - 1):
            holder.append(tria[i] + tria[i + 1])

        holder.append(1)
        triangles.append(holder)

    return triangles
