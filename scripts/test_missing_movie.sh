#!/bin/bash

# Teste faltando filme
echo "Teste faltando filme:"
curl -X POST http://localhost:5000/movies -H "Content-Type: application/json" -d '{"user": "test_user"}'

