docker login


oc apply -f secret-mongodb.yaml
oc apply -f pvc-mongodb.yaml
oc apply -f deploy-mongodb.yaml
oc apply -f service-mongodb.yaml

oc apply -f deploy-dal-server.yaml

oc apply -f service-dal-server.yaml
oc apply -f route-dal-server.yaml



