from model.model import Model

model=Model()
model.buildGraph(1399)
print(model.getNumNodes())
print(model.getNumEdges())