from app.engine.models.wmc_noisy_or.ddx import ddx


def test_existent_inference():
    assert ddx(["low oxygen in the body", "chest discomfort"]) == {'bronchitis': 0.00011519888246510253,
     'congestive heart failure': 5.7599441232551264e-05, 
     'pulmonary embolism': 0.029490481580047516, 
     'pulmonary hypertension': 0.007372722359874787}


def test_nonexistent_inference():
    assert ddx(["XXX"]) == {}
