#!/bin/bash

# Teste faltando usuário
echo "Teste faltando usuário:"
curl -X POST http://localhost:5000/movies -H "Content-Type: application/json" -d '{"movie": "The Two Towers"}'

