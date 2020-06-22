import unittest
import heredity as hrd


class TestHeredity(unittest.TestCase):
    def test_joint_probability(self):

        # One gene
        people = hrd.load_data("data/family0.csv")
        one_gene = {"Harry"}
        two_genes = {"James"}
        have_trait = {"James"}
        self.assertAlmostEqual(
            hrd.joint_probability(people, one_gene, two_genes, have_trait), 0.00266, 5,
        )

        # No genes
        one_gene = {}
        two_genes = {"James"}
        have_trait = {"James"}
        self.assertAlmostEqual(
            hrd.joint_probability(people, one_gene, two_genes, have_trait),
            0.000060546,
            5,
        )

        # Two genes
        one_gene = {}
        two_genes = {"James", "Harry"}
        have_trait = {"James"}
        self.assertAlmostEqual(
            hrd.joint_probability(people, one_gene, two_genes, have_trait),
            0.000021405,
            5,
        )

    def test_update(self):

        probabilities = {
            "Harry": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}},
            "James": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}},
            "Lilly": {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}},
        }
        one_gene = {"Harry"}
        two_genes = {"James"}
        have_trait = {"James"}
        p = 0.00266
        hrd.update(probabilities, one_gene, two_genes, have_trait, p)
        self.assertEqual(
            probabilities,
            {
                "Harry": {"gene": {2: 0, 1: p, 0: 0}, "trait": {True: 0, False: p}},
                "James": {"gene": {2: p, 1: 0, 0: 0}, "trait": {True: p, False: 0}},
                "Lilly": {"gene": {2: 0, 1: 0, 0: p}, "trait": {True: 0, False: p}},
            },
        )


if __name__ == "__main__":
    unittest.main()
