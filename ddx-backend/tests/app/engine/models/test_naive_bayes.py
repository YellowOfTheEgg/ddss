from app.engine.models.naive_bayes import ddx as naive_ddx


def test_naive_bayes(knowledge_base):
    engine_result_fever = naive_ddx(["heartburn"], knowledge_base)
    engine_result_headache = naive_ddx(["XXX"], knowledge_base)
    assert engine_result_fever == {"acid reflux": 0.02, "burn": 0.023}
    assert engine_result_headache == {}
