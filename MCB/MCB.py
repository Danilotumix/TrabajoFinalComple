#!/usr/bin/env python
# coding: utf-8

from math import sqrt, inf
from heapq import heappop, heappush

import sys

def find(s,a):
  if s[a] < 0:
    return a
  grandpa = find(s, s[a])
  return grandpa

def union(s,a,b):
  pa = find(s,a)
  pb = find(s,b)
  if pa == pb:
    return
  if s[pa] >= s[pb]:
    s[pa] += s[pb]
    s[pb] = pa
  elif s[pb] > s[pa]:
    s[pb] += s[pa]
    s[pa] = pb

def kruskal(q, n):
  root = [-1]*n
  T = []
  while len(q):
    ww, ii, ff = heappop(q)
    if find(root, ii) != find(root, ff):
      union(root, ii, ff)
      T.append((ii, ff, ww))
  return T
#hi
def distance(a, b):
  return sqrt(a**2 + b**2)

def MCB(ady, n):
  
  dist = [[inf]*n for i in range(n)]
  q = []
  for u in range(n):
    for l in range(len(ady[u])):
      v, w = ady[u][l]
      dist[u][v] = w
      dist[v][u] = w
      heappush(q, (w,u,v))
  
  mst = kruskal(q[:], n)
  freq = [0]*n

  for e in mst:
    freq[e[0]] += 1
    freq[e[1]] += 1
  
  cycle = []
  outPoints = []

  for p in range(n):
    if freq[p] == 1:
      cycle.append(p)
    else:
      outPoints.append(p)

  while len(outPoints):
    m = len(cycle)
    e = outPoints.pop()
    idx = 0
    
    for i in range(1, len(cycle)):
      if dist[e][cycle[idx]] > dist[e][cycle[i]]:
        idx = i
    
    if dist[cycle[idx-1]][e] > dist[cycle[(idx+1)%m]][e]:
      cycle.insert(idx, e)
    else:
      cycle.insert(idx+1, e)
  
  adyc = [[] for i in range(n)]

  for i in range(len(cycle)-1):
    
    u = cycle[i]
    v = cycle[i+1]
    adyc[u].append((v, dist[u][v]))
  u = cycle[0]
  v = cycle[-1]
  adyc[u].append((v, dist[u][v]))

  return adyc, cycle

if len(sys.argv) == 1:
    adyLstFN = "adylst.al"
else:
    adyLstFN = sys.argv[1]

with open(adyLstFN) as al:
  line=al.readline().strip()
  pre = []
  for ss in al:
    ss = ss.replace("\r", "").replace("\n", "")
    a = ss.split(";")
    b = [x.split(",") for x in a]
    pre.append(b)
  
  proc = []
  ns = []
  for a in pre:
    temp1 = []
    for b in a:
      i = 0
      temp2 = []
      for c in b:
        if i == 0:
          ns.append(int(c))
          temp2.append(int(c))
        else:
          temp2.append(float(c))
        i += 1
        temp1.append(temp2)
    proc.append(temp1)
  
  adyc,cycle = MCB(proc, max(ns)+1)
  print("La ruta de Minimun Cycle Bifurcation es: ")
  print(cycle)
  print("")
  
  uwu=len(adyc)

  total = 0

  for inn in range(uwu):
    for _, v in adyc[inn]:
      total += v
  
  print("El recorrido total es: " + str(round(total, 5)) + " km")