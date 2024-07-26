#!/bin/bash

# Teste de sucesso
echo "Teste de sucesso:"
curl -X POST http://localhost:5000/movies -H "Content-Type: application/json" -d '{"user": "test_user", "movie": "The Two Towers"}'

