import uuid
from datetime import datetime
from sqlalchemy import String,DateTime,Integer,Float,Text,Boolean,UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID,JSONB
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.sql import func
from app.db import Base
def uid():return uuid.uuid4()
class ResearchRun(Base):
 __tablename__="research_runs";id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid)
 tenant_id:Mapped[str]=mapped_column(String(128),index=True);principal_id:Mapped[str]=mapped_column(String(256))
 goal:Mapped[str]=mapped_column(Text);mode:Mapped[str]=mapped_column(String(32));status:Mapped[str]=mapped_column(String(32),index=True,default="CREATED")
 plan:Mapped[dict|None]=mapped_column(JSONB,nullable=True);budget:Mapped[dict]=mapped_column(JSONB,default=dict);created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now())
class Task(Base):
 __tablename__="research_tasks";__table_args__=(UniqueConstraint("run_id","task_key"),)
 id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);run_id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),index=True)
 task_key:Mapped[str]=mapped_column(String(128));question:Mapped[str]=mapped_column(Text);status:Mapped[str]=mapped_column(String(32),index=True,default="PENDING")
 request:Mapped[dict]=mapped_column(JSONB,default=dict);result:Mapped[dict|None]=mapped_column(JSONB,nullable=True);attempt:Mapped[int]=mapped_column(Integer,default=0)
class EvidenceRecord(Base):
 __tablename__="evidence";id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);run_id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),index=True)
 evidence_key:Mapped[str]=mapped_column(String(128),index=True);source_type:Mapped[str]=mapped_column(String(64));uri:Mapped[str]=mapped_column(Text)
 title:Mapped[str]=mapped_column(Text);snippet:Mapped[str]=mapped_column(Text);scores:Mapped[dict]=mapped_column(JSONB,default=dict);meta:Mapped[dict]=mapped_column(JSONB,default=dict)
class ClaimRecord(Base):
 __tablename__="claims";id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);run_id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),index=True)
 claim_key:Mapped[str]=mapped_column(String(128));text:Mapped[str]=mapped_column(Text);evidence_ids:Mapped[list]=mapped_column(JSONB,default=list);confidence:Mapped[float]=mapped_column(Float,default=0)
class Outbox(Base):
 __tablename__="outbox";id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);event_type:Mapped[str]=mapped_column(String(128),index=True)
 aggregate_id:Mapped[str]=mapped_column(String(128),index=True);payload:Mapped[dict]=mapped_column(JSONB);published:Mapped[bool]=mapped_column(Boolean,default=False,index=True)
class Audit(Base):
 __tablename__="audit";id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);run_id:Mapped[uuid.UUID|None]=mapped_column(UUID(as_uuid=True),nullable=True,index=True)
 actor:Mapped[str]=mapped_column(String(256));event_type:Mapped[str]=mapped_column(String(128));data:Mapped[dict]=mapped_column(JSONB,default=dict)
