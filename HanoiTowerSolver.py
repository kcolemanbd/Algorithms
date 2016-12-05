# HanoiTowerSolver-in-Python
# Artificial intelligence Solver for Hanoi Towers


from System import *

class HanoiSolver(object):
	def computedTowers(count, source, dest, spare):
		if count == 1:
			Console.WriteLine("Move disk from pole {0} to pole {1}", source, dest)
		else:
			HanoiSolver.computedTowers(count - 1, source, spare, dest)
			HanoiSolver.computedTowers(1, source, dest, spare)
			HanoiSolver.computedTowers(count - 1, spare, dest, source)

	computedTowers = staticmethod(computedTowers)
#Main Class for HanoiSolver
	def Main(args):
		Console.Write("Enter number of Rings: ")
		myCount = Convert.ToInt16(Console.ReadLine())
		Console.Write("Enter letter of peg to put rings on: ")
		mySource = Convert.ToChar(Console.ReadLine())
		Console.Write("Enter letter of peg to move rings: ")
		myDest = Convert.ToChar(Console.ReadLine())
		Console.Write("Enter letter of spare peg: ")
		mySpare = Convert.ToChar(Console.ReadLine())
		HanoiSolver.computedTowers(myCount, mySource, myDest, mySpare)
		Console.ReadLine()

	Main = staticmethod(Main)
