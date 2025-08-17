oc apply -f secret-mongodb.yaml
oc apply -f pvc-mongodb.yaml
oc apply -f deploy-mongodb.yaml
oc apply -f service-mongodb.yaml