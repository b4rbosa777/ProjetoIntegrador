# Projeto Integrador SENAI: Estufa Inteligente com Controle Automatizado

## Introdução
Este é um projeto integrador para o curso do SENAI que une conhecimentos das áreas de Tecnologia da Informação (TI) e Tecnologia da Automação (TA). O objetivo do projeto é desenvolver uma **estufa de plantação automatizada** com **irrigação por gotejamento**, capaz de monitorar automaticamente os níveis de temperatura e umidade.

## Tecnologias Utilizadas

### Backend
O backend do sistema está sendo desenvolvido em **ASP.NET**, oferecendo uma estrutura robusta e escalável para o gerenciamento de dados dos sensores de monitoramento e controle.

### Frontend
A interface do usuário é construída em **React**, proporcionando uma experiência dinâmica para o acompanhamento dos dados em tempo real e controle dos parâmetros da estufa.

## Funcionalidades
- **Monitoramento em tempo real** de temperatura e umidade da estufa.
- **Interface de usuário** para visualização e configuração dos dados monitorados.

## Conclusão
Este projeto integrador representa uma aplicação prática dos conhecimentos adquiridos, aplicando TI e TA no desenvolvimento de uma solução para monitoramento e controle de condições agrícolas.


## Diagrama de Sequência

```mermaid
sequenceDiagram
    participant ESP32
    participant Backend
    participant Frontend

    ESP32->>Backend: Envia dados de temperatura e umidade em formato JSON
    Backend->>ESP32: Confirma recebimento dos dados
    Frontend->>Backend: Faz requisições HTTP para obter dados em tempo real
    Backend->>Frontend: Retorna dados processados para exibição
    Frontend->>Backend: Envia comandos de controle (ex.: ajustar temperatura ou ativar irrigação)
    Backend->>ESP32: Envia comandos para os atuadores (lâmpada, bomba)
    ESP32->>Backend: Confirma execução dos comandos
    Backend->>Frontend: Atualiza status do sistema

    
