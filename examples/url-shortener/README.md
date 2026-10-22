# Example: URL shortener design

This example shows how a system-design answer becomes a working prototype.

## 1. Clarify the problem

We want a service that accepts a long URL and returns a short URL, and then redirects the short URL to the original target.

Requirements:
- Accept a long URL and create a short code.
- Redirect a short code to the original URL.
- Handle high read traffic and low write traffic.
- Keep the system simple and reliable.

## 2. Choose the core design

A practical design usually includes:
- API layer that receives create/lookup requests
- Hashing or ID-generation logic
- A database to store mapping: short_code -> long_url
- A cache for hot URLs to reduce latency
- A redirect endpoint for browser clients

## 3. Data model

A simple storage record looks like this:

- short_code: unique identifier
- long_url: original destination
- created_at: timestamp
- expires_at: optional, if TTL is needed

## 4. Why this works

The main bottleneck is usually the redirect flow: read-heavy, latency-sensitive, and easy to cache. The write path is smaller and simpler, so the design optimizes for fast lookups and compact storage.

## 5. Simplified code sample

See `main.py` for a compact Python prototype.

It demonstrates:
- generating a short code from a numeric ID
- storing mappings in memory
- resolving short codes back to original URLs
- keeping the design close to what you would say in an interview
