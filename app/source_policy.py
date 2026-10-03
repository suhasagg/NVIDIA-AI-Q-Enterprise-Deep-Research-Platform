def authorize(source_type:str,allowed:list[str],tenant_id:str):
 if source_type not in allowed:return False
 return source_type in {"enterprise","web","sql","vector","graph","search"}
