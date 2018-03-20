echo "Testing floyd-warshall application"


# Testing with path argument
python3 api/tools.py data/input.txt
# Without
python3 api/tools.py

# 200: Hello world
curl -X GET http://localhost:5000/

# 405: GET is not allowed on this route
curl -X GET http://localhost:5000/floyd-warshall

# 401: Forbidden, we need Basic Auth Credentials
curl -X POST http://localhost:5000/floyd-warshall

# 200: Authenticated but we need body
curl -X POST http://admin:toupie@localhost:5000/floyd-warshall

# 200: It's all good
curl -X POST http://localhost:5000/floyd-warshall -H 'Authorization: Basic YWRtaW46dG91cGll' -F 'data=4ta=4
5
1,3,-2
2,1,4
4,2,-1
3,4,2
2,3,3
'
