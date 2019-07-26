class g:
	edge = []
	temp = []
	vertices = set()
	ad_list = {}
	def insert_edge(self,u,v,w=None):
		self.temp.append([u,v])
		self.edge.append([u,v,w if directed else 1])
		if not directed:
			self.edge.append([v,u,w if directed else 1])
	def adj_list(self):
		self.ad_list = {key : [] for key in set(self.temp)}
		for ed in self.edge:
			self.ad_list[ed[0]].append({ed[1],ed[2]})
	def vertices_number(self):
		return len(set(self.temp))


