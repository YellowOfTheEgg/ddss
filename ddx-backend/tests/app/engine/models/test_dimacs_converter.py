import app.engine.models.wmc_noisy_or.dimacs_converter as dimacs_converter


dimacs_str = dimacs_converter.run(["fever", "headache"], "abscess", decrease_variable_names=False)


with open("tests/app/engine/resources/dimacs.cnf", "r") as test_data:
    test_str = test_data.read()


def test_dimacs_file():
    assert dimacs_str == test_str
