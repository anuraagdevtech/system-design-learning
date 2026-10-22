# system-design-learning
A comprehensive repository for learning system design with topics, concepts, and code samples.

## Study guides

- [Google system design interview questions](./google-system-design-interview-questions.md) — 60 Google-style interview questions and design themes for preparation.

## Problem guides

- [System design problem guides](./problems/README.md) — one README per problem with interview approach and solution framing.

## Repository focus

This repository is intended to collect study material for system design interviews, including architecture patterns, interview questions, and practical design scenarios.

## How to design each problem

For every system design question, the expected answer is not just a list of buzzwords. A strong design answer should follow this shape:

- Clarify the functional and non-functional requirements.
- Estimate the traffic shape, data size, and bottlenecks.
- Choose the core architecture: clients, services, storage, caches, queues, and background workers.
- Walk through the main request path and explain the bottleneck at scale.
- Discuss trade-offs: consistency, durability, latency, cost, and operational complexity.
- End with explicit failure modes and how the design degrades gracefully.

This repository keeps the interview framing and adds the design structure so you can move from "approach" to "actual solution design".

## Design walkthroughs and code examples

- [URL shortener example](./examples/url-shortener/README.md) — a practical design walkthrough with a small Python prototype.
- [Examples index](./examples/README.md) — add more worked examples as the repo grows.
