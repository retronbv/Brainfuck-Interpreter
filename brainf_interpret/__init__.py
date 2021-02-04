import sys

__version__ = '1.1.0'

def run(prg, showMem=False):
  PrgPos = 0
  mem = [0]
  memPos = 0
  while PrgPos < len(prg):
      if prg[PrgPos] == ">":
          memPos += 1
          if len(mem) <= memPos:
              mem.append(0)
      elif prg[PrgPos] == "<":
          memPos -= 1
          if memPos < 0:
              print("Error: Moved off memory!")
              sys.exit(0)
      elif prg[PrgPos] == "+":
          mem[memPos] += 1
          if mem[memPos] >= 255:
              mem[memPos] = 0
      elif prg[PrgPos] == "-":
          mem[memPos] -= 1
          if mem[memPos] <= -1:
              mem[memPos] = 255
      elif prg[PrgPos] == ".":
          print(chr(mem[memPos]), end="")
      elif prg[PrgPos] == ",":
          inp = input("input requested: ")
          mem[memPos] = ord( inp[0] )
      elif prg[PrgPos] == "[":
          if mem[memPos] == 0:
              countOpened = 0
              PrgPos += 1
              while PrgPos < len(prg):
                  if prg[PrgPos] == "]" and countOpened == 0:
                      break
                  elif prg[PrgPos] == "[":
                      countOpened += 1
                  elif prg[PrgPos] == "]":
                      countOpened -= 1
                  PrgPos += 1
      elif prg[PrgPos] == "]":
          if mem[memPos] != 0:
              countClosed = 0
              PrgPos -= 1
              while PrgPos >= 0:
                  if prg[PrgPos] == "[" and countClosed == 0:
                      break
                  elif prg[PrgPos] == "]":
                      countClosed += 1
                  elif prg[PrgPos] == "[":
                      countClosed -= 1
                  PrgPos -= 1
      PrgPos += 1
  if (showMem):
    print(mem)
