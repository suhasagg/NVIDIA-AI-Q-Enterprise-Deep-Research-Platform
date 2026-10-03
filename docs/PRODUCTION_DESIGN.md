# Production Design

SQL is authoritative. Persist task/evidence/report transitions and an outbox event atomically. Kafka/Pulsar distributes work. Research workers use leases/fencing/idempotency. Artifacts live in object storage. Retrieval systems enforce tenant ACLs. OpenTelemetry traces the complete research graph.
