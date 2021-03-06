"""
Edges in MST
You are given a connected weighted undirected graph without any loops and multiple edges.

Let us remind you that a graph's spanning tree is defined as an acyclic connected subgraph of the given graph that includes all of the graph's vertexes. The weight of a tree is defined as the sum of weights of the edges that the given tree contains. The minimum spanning tree (MST) of a graph is defined as the graph's spanning tree having the minimum possible weight. For any connected graph obviously exists the minimum spanning tree, but in the general case, a graph's minimum spanning tree is not unique.

Your task is to determine the following for each edge of the given graph: whether it is either included in any MST, or included at least in one MST, or not included in any MST.
"""

#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int, int> pii;
const int N = 1e6 + 100;
 
int n, m, U[N], V[N], W[N], h[N], up[N], par[N], ans[N];
bool mark[N];
vector<int> vec[N], nei[N];
map<pii, int> edge_dex;
 
int g_par(int v) {
	return (par[v] == v? v: par[v] = g_par(par[v]));
}
 
int dfs(int v, int par = -1) {
	mark[v] = true;
	up[v] = h[v];
	bool see = false;
	for (int u: nei[v])
		if(u == par && see == false)
			see = true;
		else if(mark[u])
			up[v] = min(up[v], h[u]);
		else {
			h[u] = h[v] + 1;
			int x = dfs(u, v);
			if(x > h[v])
				ans[edge_dex[pii(u, v)]]++;
			up[v] = min(up[v], x);
		}
	return up[v];
}
 
int main() {
	ios::sync_with_stdio(false), cin.tie(0);
	cin >> n >> m;
	iota(par, par + n, 0);
	for (int i = 0; i < m; i++) {
		cin >> U[i] >> V[i] >> W[i];
		U[i]--;
		V[i]--;
		vec[W[i]].push_back(i);
	}
	for (int w = 0; w < N; w++) {
		edge_dex.clear();
		vector<int> help;
		for (int dex: vec[w]) {
			int u = g_par(U[dex]), v = g_par(V[dex]);
			if(u != v) {
				ans[dex] = 1;
				edge_dex[pii(u, v)] = edge_dex[pii(v, u)] = dex;
				nei[u].push_back(v);
				nei[v].push_back(u);
				help.push_back(u);
				help.push_back(v);
			}
		}
		for (int u: help)
			if(mark[u] == false)
				dfs(u);
		for (int dex: help)
			nei[dex].clear(), mark[dex] = false;
		
		for (int dex: vec[w])
			par[g_par(U[dex])] = g_par(V[dex]);
	}
	for (int i = 0; i < m; i++)
		cout << (ans[i] == 2? "any": ans[i] == 1? "at least one": "none") << '\n';
	return 0;
}
