from app.engine.models.noisyOr import NoisyOr
from pgmpy.factors.discrete import TabularCPD

test_weights = {
    "parents": [
        {"name": "abscess", "weight": 0.8},
        {"name": "acid reflux", "weight": 0.2},
    ],
    "children": [
        {
            "name": "pain",
            "weights": {"abscess": 0.6153846153846154, "acid reflux": 0.0},
        },
        {
            "name": "fever",
            "weights": {"abscess": 0.46153846153846156, "acid reflux": 1.0},
        },
        {
            "name": "swelling",
            "weights": {"abscess": 0.15384615384615385, "acid reflux": 1.0},
        },
        {"name": "redness", "weights": {"acid reflux": 1.0}},
    ],
}

test_cptss = {
    "pain": {
        "names": ["abscess", "acid reflux"],
        "values": [[1, 0, 0.6153846153846154, 0], [0, 1, 1 - 0.6153846153846154, 1]],
    },
    "fever": {
        "names": ["abscess", "acid reflux"],
        "values": [
            [1, 1, 0.46153846153846156, 0.46153846153846156],
            [0, 0, 1 - 0.46153846153846156, 1 - 0.46153846153846156],
        ],
    },
    "swelling": {
        "names": ["abscess", "acid reflux"],
        "values": [
            [1, 1, 0.15384615384615385, 0.15384615384615385],
            [0, 0, 1 - 0.15384615384615385, 1 - 0.15384615384615385],
        ],
    },
    "redness": {"names": ["abscess", "acid reflux"], "values": [[1, 1], [0, 0]]},
}
test_cpts = {
    "pain": TabularCPD(
        variable="pain",
        variable_card=2,
        evidence=["abscess", "acid reflux"],
        evidence_card=[2, 2],
        values=[[1, 0, 0.6153846153846154, 0], [0, 1, 1 - 0.6153846153846154, 1]],
    ),
    "fever": TabularCPD(
        variable="fever",
        variable_card=2,
        evidence=["abscess", "acid reflux"],
        evidence_card=[2, 2],
        values=[
            [1, 1, 0.46153846153846156, 0.46153846153846156],
            [0, 0, 1 - 0.46153846153846156, 1 - 0.46153846153846156],
        ],
    ),
    "swelling": TabularCPD(
        variable="swelling",
        variable_card=2,
        evidence=["abscess", "acid reflux"],
        evidence_card=[2, 2],
        values=[
            [1, 1, 0.15384615384615385, 0.15384615384615385],
            [0, 0, 1 - 0.15384615384615385, 1 - 0.15384615384615385],
        ],
    ),
    "redness": TabularCPD(
        variable="redness",
        variable_card=2,
        evidence=["acid reflux"],
        evidence_card=[2],
        values=[[1, 1], [0, 0]],
    ),
    "abscess": TabularCPD(variable="abscess", variable_card=2, values=[[0.8, 0.2]]),
    "acid reflux": TabularCPD(
        variable="acid reflux", variable_card=2, values=[[0.2, 0.8]]
    ),
}

noisyOr = NoisyOr(
    knowledge_graph_path="tests/app/engine/resources/DerivedKnowledgeNoisyOrTest.csv",
    trainingsdata_path="tests/app/engine/resources/noisy_or_test_trainingsdata.csv",
)


def test_noisy_or_weights():
    assert noisyOr.weights == test_weights


def test_noisy_or_cpts_values():
    for cpd in noisyOr.cpds:
        node = cpd.variables[0]
        assert cpd.__str__() == test_cpts.get(node, "").__str__()


def test_noisy_or_model():
    assert noisyOr.model.check_model() == True


def test_noisy_or_inference():
    assert noisyOr.ddx(["pain"]) == {
        "abscess": 0.2150943396226414,
        "acid reflux": 0.9811320754716982,
    }
