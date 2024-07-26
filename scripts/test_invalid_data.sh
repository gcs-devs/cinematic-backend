#!/bin/bash

# Teste com entrada inválida
echo "Teste com entrada inválida:"
curl -X POST http://localhost:5000/movies -H "Content-Type: application/json" -d 'invalid_data'

