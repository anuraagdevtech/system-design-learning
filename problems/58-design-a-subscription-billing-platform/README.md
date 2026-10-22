# Problem 58: Design a subscription billing platform

## How to approach this problem

Start by clarifying the product goal, user and system constraints, expected read/write patterns, and the biggest bottleneck. In an interview, a strong answer usually moves through: requirements, capacity estimates, core components, data flow, bottlenecks, and trade-offs.

## Key focus areas
- recurring invoices
- renewals
- retries
- proration rules.

## 1. Clarify the requirements

- Define the functional behavior: what the system must do for users and operators.
- Capture the non-functional goals: latency, availability, durability, cost, scale, and operability.
- State assumptions explicitly when the problem is underspecified, such as traffic mix, regional usage, or privacy requirements.

## 2. Define the core constraints

- Estimate traffic shape: peak QPS, read-heavy vs write-heavy access, and data growth over time.
- Identify the most important failure modes: hot keys, uneven traffic, storage limits, network partitions, or thundering herds.
- Separate true requirements from nice-to-have features that can be dropped or deferred.

## 3. High-level architecture

Propose a clean layered design: clients and edge services, application logic, storage and indexing, background workers, and observability. Keep the design explainable and grounded in the real bottlenecks of the problem.

A typical architecture includes:

- API layer or edge services for request handling
- Business logic for validation, fan-out, routing, or scheduling
- Databases or object stores for durable state
- Caches or materialized views for latency-sensitive access
- Queues and workers for asynchronous processing
- Monitoring, tracing, and alerting for reliability

## 4. Deep dive into the main components

Explain each component in terms of purpose and trade-offs:

- Which service owns the write path?
- Where does data get stored and replicated?
- What is the hot path for reads and writes?
- Where do you introduce caching, partitioning, or precomputation?
- How do background jobs and retries affect consistency and cost?

## 5. Data flow and bottlenecks

Walk through the request lifecycle from the user action to storage and back. Highlight where latency is introduced and what becomes the main bottleneck at scale.

Typical questions to answer:

- Where is the system read-heavy or write-heavy?
- What will fail first under load?
- What needs to be sharded, replicated, or cached?
- What is the cost of consistency and durability?

## 6. Trade-offs to discuss

Be ready to explain why the chosen approach is reasonable and what alternatives were rejected.

- SQL vs NoSQL, or object storage vs block storage
- Strong consistency vs eventual consistency
- Read-optimized vs write-optimized storage
- Push-based fan-out vs pull-based aggregation
- Hot key mitigation through sharding, partitioning, or rate limits
- Synchronous vs asynchronous processing paths
- Cache freshness, invalidation, and correctness trade-offs

## 7. Interview-ready summary

A strong final answer should sound like this:

> We would start by clarifying the core user flow and traffic shape. Then we would split the system into edge services, domain logic, durable storage, and asynchronous workers. The primary bottleneck is likely <insert main constraint>, so we would optimize there with sharding, caching, replication, or queue-based processing. We would keep the design modular and explain how it fails gracefully under load and partial outages.

## 8. Suggested solution framing for this specific problem

For design a subscription billing platform, focus on the specific mechanics that determine success:

- Understand the data model and how records are created, updated, and read.
- Identify the expensive or latency-sensitive path and optimize it first.
- Explain how the design helps with scale without over-engineering the system.
- Show awareness of failure handling, observability, and operational complexity.

This problem is best answered by combining a practical architecture with explicit reasoning about bottlenecks, trade-offs, and operational realities.
