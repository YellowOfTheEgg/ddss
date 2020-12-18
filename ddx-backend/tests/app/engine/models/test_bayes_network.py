from app.engine.models.bayes_network import BayesNetwork


def test_naive_bayes():
    bn = BayesNetwork()
    engine_result_headache = bn.ddx(["headache"])
    should_be_result = {
        "abscess": 0.75,
        "acid reflux": 0.9230769230769231,
        "acute renal failure": 0.5,
        "alcohol intoxication": 0.25,
        "alcoholism": 0.5384615384615384,
    }
    engine_result_missing = bn.ddx(["XXX"])
    assert engine_result_headache == should_be_result
    assert engine_result_missing == {}
