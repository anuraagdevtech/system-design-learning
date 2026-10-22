# System Design Problem Guides

This directory contains one README for each of the 60 core system design interview problems, with a consistent interview framework for clarifying requirements, proposing an architecture, and explaining trade-offs.

## Problem index

- [1. Design Google Search](01-design-google-search/README.md) — crawling, indexing, ranking
- [2. Design YouTube / video streaming platform](02-design-youtube-video-streaming-platform/README.md) — ingestion, transcoding, storage
- [3. Design Google Drive](03-design-google-drive/README.md) — file upload, metadata storage, sync
- [4. Design Google Docs collaborative editing](04-design-google-docs-collaborative-editing/README.md) — operational transforms, OT vs CRDT, real-time sync
- [5. Design Google Maps](05-design-google-maps/README.md) — geospatial indexing, route computation, caching
- [6. Design Gmail](06-design-gmail/README.md) — message ingestion, spam filtering, search
- [7. Design Google Calendar](07-design-google-calendar/README.md) — scheduling, time zone handling, recurring events
- [8. Design Google Photos](08-design-google-photos/README.md) — object storage, metadata indexing, deduplication
- [9. Design Google Meet](09-design-google-meet/README.md) — media signaling, real-time audio/video, WebRTC
- [10. Design a URL shortener](10-design-a-url-shortener/README.md) — hash generation, DB design, analytics
- [11. Design a rate limiter](11-design-a-rate-limiter/README.md) — token bucket, sliding window, distributed enforcement
- [12. Design a notification service](12-design-a-notification-service/README.md) — retries, deduplication, fan-out
- [13. Design a messaging or chat system](13-design-a-messaging-or-chat-system/README.md) — durable queues, presence, message ordering
- [14. Design a social feed](14-design-a-social-feed/README.md) — feed generation, ranking, caching
- [15. Design Instagram](15-design-instagram/README.md) — media storage, timeline generation, engagement ranking
- [16. Design Twitter/X feed](16-design-twitter-x-feed/README.md) — write-heavy traffic, follower graph, timeline assembly
- [17. Design Spotify](17-design-spotify/README.md) — music streaming, playback metadata, recommendations
- [18. Design Dropbox](18-design-dropbox/README.md) — sync engine, delta updates, conflict management
- [19. Design a content moderation system](19-design-a-content-moderation-system/README.md) — classification pipeline, human review, abuse detection
- [20. Design an autocomplete service](20-design-an-autocomplete-service/README.md) — indexing, prefix search, popularity weighting
- [21. Design a distributed cache](21-design-a-distributed-cache/README.md) — eviction policies, consistency, replication
- [22. Design a CDN](22-design-a-cdn/README.md) — edge caching, origin fetch, invalidation
- [23. Design a key-value store](23-design-a-key-value-store/README.md) — partitioning, replication, consensus
- [24. Design a distributed logging system](24-design-a-distributed-logging-system/README.md) — ingestion, retention, partitioning
- [25. Design a metrics and monitoring platform](25-design-a-metrics-and-monitoring-platform/README.md) — time-series ingestion, aggregation, alerts
- [26. Design an event-driven architecture](26-design-an-event-driven-architecture/README.md) — message brokers, at-least-once semantics, exactly-once challenges
- [27. Design a job scheduler](27-design-a-job-scheduler/README.md) — retries, backoff, fairness
- [28. Design a distributed task queue](28-design-a-distributed-task-queue/README.md) — worker scaling, queue partitioning, dead-letter handling
- [29. Design a leader election system](29-design-a-leader-election-system/README.md) — consensus, failover, split-brain prevention
- [30. Design a rate-limited API gateway](30-design-a-rate-limited-api-gateway/README.md) — auth, quotas, layered throttling
- [31. Design a distributed counter](31-design-a-distributed-counter/README.md) — sharding, eventual consistency, deduplication
- [32. Design a data warehouse for analytics](32-design-a-data-warehouse-for-analytics/README.md) — ETL, partitioning, columnar storage
- [33. Design a search indexing engine](33-design-a-search-indexing-engine/README.md) — indexing pipelines, document updates, relevance ranking
- [34. Design a web crawler](34-design-a-web-crawler/README.md) — discovery, politeness policies, deduplication
- [35. Design a recommendation engine](35-design-a-recommendation-engine/README.md) — ranking models, feature storage, offline and online scoring
- [36. Design a leaderboards system](36-design-a-leaderboards-system/README.md) — rank updates, snapshotting, real-time aggregation
- [37. Design a file storage system](37-design-a-file-storage-system/README.md) — block storage, metadata services, replication
- [38. Design a blob storage system](38-design-a-blob-storage-system/README.md) — object lifecycle, checksum validation, versioning
- [39. Design a payment processing system](39-design-a-payment-processing-system/README.md) — idempotency, reconciliation, audit trails
- [40. Design an e-commerce checkout system](40-design-an-e-commerce-checkout-system/README.md) — cart, order state machine, inventory reservation
- [41. Design inventory management](41-design-inventory-management/README.md) — stock tracking, locking, warehouse consistency
- [42. Design an order management system](42-design-an-order-management-system/README.md) — lifecycle transitions, synchronous vs asynchronous steps, observability.
- [43. Design a ticket booking platform](43-design-a-ticket-booking-platform/README.md) — concurrency control, seat reservation, cancellations
- [44. Design an analytics dashboard](44-design-an-analytics-dashboard/README.md) — event pipelines, aggregation layers, query latency
- [45. Design a real-time bidding system](45-design-a-real-time-bidding-system/README.md) — auction logic, low-latency routing, fairness
- [46. Design a transaction ledger](46-design-a-transaction-ledger/README.md) — immutability, auditability, consistency
- [47. Design a database sharding strategy](47-design-a-database-sharding-strategy/README.md) — key selection, hotspot mitigation, resharding
- [48. Design a replication system](48-design-a-replication-system/README.md) — read replicas, write quorum, failover
- [49. Design Google Cloud Storage or object storage at scale](49-design-google-cloud-storage-or-object-storage-at-scale/README.md) — durability, data placement, erasure coding
- [50. Design Google Ads click system](50-design-google-ads-click-system/README.md) — event collection, fraud detection, attribution
- [51. Design Google Kubernetes-style orchestration](51-design-google-kubernetes-style-orchestration/README.md) — scheduling, health checks, node failures
- [52. Design a CI/CD platform](52-design-a-ci-cd-platform/README.md) — build pipelines, caching, artifact storage
- [53. Design a code review or source control system](53-design-a-code-review-or-source-control-system/README.md) — branching, merge conflicts, commit history
- [54. Design an online code editor](54-design-an-online-code-editor/README.md) — collaborative editing, session state, file persistence
- [55. Design a digital wallet](55-design-a-digital-wallet/README.md) — ledger, balances, fraud checks
- [56. Design a ridesharing service](56-design-a-ridesharing-service/README.md) — location tracking, ETA estimation, matching algorithms
- [57. Design a hotel booking service](57-design-a-hotel-booking-service/README.md) — inventory, reservation TTL, cancellations
- [58. Design a subscription billing platform](58-design-a-subscription-billing-platform/README.md) — recurring invoices, renewals, retries
- [59. Design a fraud detection system](59-design-a-fraud-detection-system/README.md) — streaming features, rules engine, model scoring
- [60. Design a recommendation feed for commerce](60-design-a-recommendation-feed-for-commerce/README.md) — ranking, cold start, user embeddings

