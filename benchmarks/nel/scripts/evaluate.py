""" Evaluation on test data. """

from datasets.dataset import Dataset
import typer
from custom_functions import create_candidates_via_embeddings


def main(dataset_name: str):
    """Evaluate the trained EL component by applying it to unseen text."""

    Dataset.generate_dataset_from_id(dataset_name).evaluate(
        candidate_generation=True, baseline=True, context=True
    )


if __name__ == "__main__":
    typer.run(main)
