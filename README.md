## Minimal Flask api exposing FloydWarshall algorithm.

@TODO:

* Comments
* Authenticate route/form
* Docker's integration
* Path helper function giving shortest path between 2 nodes ? (path(u,v):return list[u,...,v])
* Test using --> [FloydWarshall Scipy impementation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.floyd_warshall.html#scipy.sparse.csgraph.floyd_warshall)

## How to start

* `pipenv shell or create virtualenv with pip install -r requirement.txt`
* `python api/tools.py or python api/tools.py /path/to/my/file.txt` 
_(../data/input.txt used if args aren't provided)_
