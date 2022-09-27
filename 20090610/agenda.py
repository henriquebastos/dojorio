class Agenda:
	
	eventos = []
	
	def colide(self, outra_agenda):		
		return len(self.eventos) > 0
			
		
	def adicionar(self, evento):
		self.eventos.append(evento)
		
class Evento:
	def __init__(self, nome, inicio, fim):
		pass