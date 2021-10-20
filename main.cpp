//O(E LOG V)
//DIJKSTRA USING PRIORITY QUEUE
//V IS THE NUMBER OF VERTICES
//E IS THE NUMBER OF EDGES
vector<int> Dijkstra(vector<vector<int>>& v, int s)
{
	//NODE STRUCT FOR DIJKSTRA
	struct Node
	{
		Node(int weight, int index)
		{
			this->weight = weight;
			this->index = index;
		}
		bool operator < (const Node& other) const
		{
			return this->weight > other.weight;
		}
		int weight;
		int index;
	};
	
	int n = v.size();

	vector<int> distances(n, INT_MAX);
	vector<bool> visited(n, false);
	priority_queue<Node> pq;

	pq.push(Node(0, s));
	distances[s] = 0;

	while (!pq.empty())
	{
		Node node = pq.top();
		pq.pop();
		visited[node.index] = true;

		for (int i = 0; i < n; i++)
		{
			int newCost = node.weight + v[node.index][i];
			if (v[node.index][i] != -1 and visited[i] == false and newCost < distances[i])
			{
				pq.push(Node(newCost, i));
				distances[i] = newCost;
			}
		}
	}

	return distances;
}	
