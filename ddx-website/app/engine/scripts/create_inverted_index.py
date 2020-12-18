import csv
import json
import logging

import click

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# this script creates from the csv file with format (disease, [symptoms]) a file with the format (symptom: [(disease,probability)])
@click.command()
@click.option(
    "--input_file",
    default="../resources/DerivedKnowledgeGraph_final.csv",
    help="Path to an input .csv file",
)
@click.option("--output_file", help="Path to where the inverted index should be saved")
def create_inverted_index(input_file, output_file):
    """Simple script that takes a comma-delimited file with the knowledge
    graph that was inferred using the noisy-or Bayesian network. The input
    file can be found under resources and is taken from:
    https://github.com/clinicalml/HealthKnowledgeGraph
    """
    inverted_index = {}
    with open(input_file, "r") as csv_file:
        logger.info("reading source .csv file: {}".format(input_file))
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for line in csv_reader:
            disease = line[0]
            symptoms = line[1]
            for symptom in symptoms.split(","):
                symptom_str, probability = symptom.strip().rsplit(" ", 1)
                probability = float(probability.replace("(", "").replace(")", ""))
                if symptom_str not in inverted_index:
                    inverted_index[symptom_str] = {}
                inverted_index[symptom_str][disease] = probability

        with open(output_file, "w") as fp:
            json.dump(inverted_index, fp, indent=2)
        logger.info("created inverted index: {}".format(output_file))


if __name__ == "__main__":
    create_inverted_index()
