from app import crud
from app.engine.ddx import naive_bayes_ddx


def test_ddx(knowledge_base):
    engine_result_fever = naive_bayes_ddx(["heartburn"], knowledge_base)
    engine_result_headache = naive_bayes_ddx(["XXX"], knowledge_base)
    assert engine_result_fever == {"acid reflux": 0.02, "burn": 0.023}
    assert engine_result_headache == {}
