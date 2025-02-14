"""

   PROJECT:     Chess
   PROGRAMMER:  Aleksandar Kljaic
   DATE:        Saturday February 29, 2020


"""
class ChessError(Exception): pass
class Check(ChessError): pass
class InvalidMove(ChessError): pass
class CheckMate(ChessError): pass
class Draw(ChessError): pass
class NotYourTurn(ChessError): pass
class InvalidCoord(ChessError): pass