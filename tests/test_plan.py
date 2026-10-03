from app.planner import Planner
from app.compiler import compile_plan
def test_deep_plan():assert len(compile_plan(Planner().plan("x","deep")).nodes)>=4
