#!/bin/bash

# Apply database components
kubectl apply -f 1-database/postgres-deployment.yaml
kubectl apply -f 1-database/postgres-service.yaml
kubectl apply -f 1-database/postgres-pvc.yaml

# Wait for database to be ready
echo "Waiting for database to become ready..."
kubectl wait --for=condition=ready pod -l app=postgres --timeout=120s

# Apply application components
kubectl apply -f 2-application/django-configmap.yaml
kubectl apply -f 2-application/django-deployment.yaml

# Apply networking components
kubectl apply -f 3-networking/django-service.yaml
kubectl apply -f 3-networking/django-ingress.yaml

echo "Deployment complete!"
