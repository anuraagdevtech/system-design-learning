# Google System Design Interview Questions

This document is a practical study guide for system design interviews, especially Google-style interviews. It is organized as a course companion and includes 40+ commonly asked questions with concise design themes, trade-offs, and technical focus areas.

## How to study this list

When preparing for a Google-style system design interview, focus on three things:

1. Clarify requirements and constraints.
2. Identify bottlenecks and scale trade-offs.
3. Explain concrete architecture choices with reasoning.

A strong answer is not just a diagram; it is a clear narrative that covers data flow, consistency, availability, latency, cost, and operational complexity.

---

## 1) Core system design questions

1. Design Google Search
   - Focus: crawling, indexing, ranking, query latency, sharding.

2. Design YouTube / video streaming platform
   - Focus: ingestion, transcoding, storage, CDN, adaptive bitrate streaming.

3. Design Google Drive
   - Focus: file upload, metadata storage, sync, conflict resolution.

4. Design Google Docs collaborative editing
   - Focus: operational transforms, OT vs CRDT, real-time sync, conflict handling.

5. Design Google Maps
   - Focus: geospatial indexing, route computation, caching, real-time traffic data.

6. Design Gmail
   - Focus: message ingestion, spam filtering, search, delivery guarantees.

7. Design Google Calendar
   - Focus: scheduling, time zone handling, recurring events, notification pipeline.

8. Design Google Photos
   - Focus: object storage, metadata indexing, deduplication, face recognition.

9. Design Google Meet
   - Focus: media signaling, real-time audio/video, WebRTC, scaling of conferencing sessions.

10. Design a URL shortener
   - Focus: hash generation, DB design, analytics, rate limiting.

11. Design a rate limiter
   - Focus: token bucket, sliding window, distributed enforcement, fail-open/fail-closed.

12. Design a notification service
   - Focus: retries, deduplication, fan-out, delivery guarantees.

13. Design a messaging or chat system
   - Focus: durable queues, presence, message ordering, offline delivery.

14. Design a social feed
   - Focus: feed generation, ranking, caching, fan-out on write vs read.

15. Design Instagram
   - Focus: media storage, timeline generation, engagement ranking, cache invalidation.

16. Design Twitter/X feed
   - Focus: write-heavy traffic, follower graph, timeline assembly, hot user handling.

17. Design Spotify
   - Focus: music streaming, playback metadata, recommendations, user personalization.

18. Design Dropbox
   - Focus: sync engine, delta updates, conflict management, file versioning.

19. Design a content moderation system
   - Focus: classification pipeline, human review, abuse detection, audit.

20. Design an autocomplete service
   - Focus: indexing, prefix search, popularity weighting, low-latency serving.

---

## 2) Distributed systems and scalability questions

21. Design a distributed cache
   - Focus: eviction policies, consistency, replication, hot keys, invalidation.

22. Design a CDN
   - Focus: edge caching, origin fetch, invalidation, request routing, cache miss handling.

23. Design a key-value store
   - Focus: partitioning, replication, consensus, reads/writes, CAP trade-offs.

24. Design a distributed logging system
   - Focus: ingestion, retention, partitioning, search, backpressure handling.

25. Design a metrics and monitoring platform
   - Focus: time-series ingestion, aggregation, alerts, dashboards, retention policies.

26. Design an event-driven architecture
   - Focus: message brokers, at-least-once semantics, exactly-once challenges, consumers.

27. Design a job scheduler
   - Focus: retries, backoff, fairness, concurrency control, worker orchestration.

28. Design a distributed task queue
   - Focus: worker scaling, queue partitioning, dead-letter handling, priorities.

29. Design a leader election system
   - Focus: consensus, failover, split-brain prevention, quorum.

30. Design a rate-limited API gateway
   - Focus: auth, quotas, layered throttling, per-tenant isolation.

31. Design a distributed counter
   - Focus: sharding, eventual consistency, deduplication, ordering semantics.

32. Design a data warehouse for analytics
   - Focus: ETL, partitioning, columnar storage, query optimization, clustering.

33. Design a search indexing engine
   - Focus: indexing pipelines, document updates, relevance ranking, storage layout.

34. Design a web crawler
   - Focus: discovery, politeness policies, deduplication, anti-bot handling, content freshness.

35. Design a recommendation engine
   - Focus: ranking models, feature storage, offline and online scoring, cold starts.

36. Design a leaderboards system
   - Focus: rank updates, snapshotting, real-time aggregation, heavy read patterns.

---

## 3) Data systems and storage questions

37. Design a file storage system
   - Focus: block storage, metadata services, replication, snapshotting, integrity checks.

38. Design a blob storage system
   - Focus: object lifecycle, checksum validation, versioning, lifecycle policies.

39. Design a payment processing system
   - Focus: idempotency, reconciliation, audit trails, ledger consistency.

40. Design an e-commerce checkout system
   - Focus: cart, order state machine, inventory reservation, payment orchestration.

41. Design inventory management
   - Focus: stock tracking, locking, warehouse consistency, eventual reconciliation.

42. Design an order management system
   - Focus: lifecycle transitions, synchronous vs asynchronous steps, observability.

43. Design a ticket booking platform
   - Focus: concurrency control, seat reservation, cancellations, fairness.

44. Design an analytics dashboard
   - Focus: event pipelines, aggregation layers, query latency, user-level security.

45. Design a real-time bidding system
   - Focus: auction logic, low-latency routing, fairness, bid validation.

46. Design a transaction ledger
   - Focus: immutability, auditability, consistency, append-only model.

47. Design a database sharding strategy
   - Focus: key selection, hotspot mitigation, resharding, cross-shard joins.

48. Design a replication system
   - Focus: read replicas, write quorum, failover, lag handling, correctness.

---

## 4) Application-specific Google-like product questions

49. Design Google Cloud Storage or object storage at scale
   - Focus: durability, data placement, erasure coding, data lifecycle policies.

50. Design Google Ads click system
   - Focus: event collection, fraud detection, attribution, billing correctness.

51. Design Google Kubernetes-style orchestration
   - Focus: scheduling, health checks, node failures, autoscaling, resource isolation.

52. Design a CI/CD platform
   - Focus: build pipelines, caching, artifact storage, deployment strategies.

53. Design a code review or source control system
   - Focus: branching, merge conflicts, commit history, permissioning.

54. Design an online code editor
   - Focus: collaborative editing, session state, file persistence, autosave.

55. Design a digital wallet
   - Focus: ledger, balances, fraud checks, retries, transactional consistency.

56. Design a ridesharing service
   - Focus: location tracking, ETA estimation, matching algorithms, hot-spots.

57. Design a hotel booking service
   - Focus: inventory, reservation TTL, cancellations, rate limits.

58. Design a subscription billing platform
   - Focus: recurring invoices, renewals, retries, proration rules.

59. Design a fraud detection system
   - Focus: streaming features, rules engine, model scoring, alerting pipelines.

60. Design a recommendation feed for commerce
   - Focus: ranking, cold start, user embeddings, real-time personalization.

---

## 5) Common design themes Google interviewers evaluate

When answering any system design question, be ready to discuss:

- Functional requirements: what the system must do.
- Non-functional requirements: latency, reliability, scale, costs.
- Data model: schema, storage engine, indexing choices.
- API design: request/response patterns, versioning, idempotency.
- Storage strategy: SQL vs NoSQL, caching at layers, hot spots.
- Consistency model: strong consistency vs eventual consistency.
- Reliability: retries, timeouts, circuit breakers, deduplication.
- Scalability: sharding, partitioning, replication, queueing.
- Trade-offs: CAP, cost vs performance, complexity vs reliability.

---

## 6) Suggested interview response framework

Use this template during interviews:

1. Clarify assumptions and scope.
2. State functional and non-functional requirements.
3. Propose a high-level architecture.
4. Break down core components: clients, APIs, services, storage, cache, queue, workers.
5. Discuss data flow and bottlenecks.
6. Explain consistency, reliability, and scaling strategies.
7. Identify trade-offs and alternative designs.
8. Mention observability, metrics, and failure handling.

This structured approach is often more important than memorizing a single "perfect" design.

---

## 7) Practical study roadmap

A good 2- to 4-week preparation plan is:

- Week 1: Learn core patterns such as load balancers, caching, sharding, replication, queueing, and CAP.
- Week 2: Practice 10-15 of the above questions, focusing on detailed trade-offs.
- Week 3: Simulate interviews with a timer and talk through design decisions.
- Week 4: Review metrics, failure modes, and how to explain architecture clearly.

A strong candidate does not just name technologies; they explain why the chosen architecture fits the problem.

---

## 8) Quick reference for high-frequency patterns

- Use caching for read-heavy hot paths.
- Use queues for decoupling and burst absorption.
- Use sharding when a single database becomes a bottleneck.
- Use replication for scalability and failover.
- Use CDN for static and near-static content delivery.
- Use event streams for analytics and downstream processing.
- Use immutable logs for auditability and replay.
- Use idempotency keys for safe retries in payment and order systems.

---

## 9) Final note

The goal of a Google system design interview is not to memorize a single standard answer. It is to show structured thinking, technical depth, and the ability to make sound design decisions under constraints. Use the questions in this list as a study set and practice explaining your architecture in clear steps.
