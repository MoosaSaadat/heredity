import unittest
import heredity as hrd


class TestHeredity(unittest.TestCase):
    def test_joint_probability(self):

        # One gene
        people = hrd.load_data("data/family0.csv")
        one_gene = {"Harry"}
        two_gene = {"James"}
        have_trait = {"James"}
        self.assertAlmostEqual(
            hrd.joint_probability(people, one_gene, two_gene, have_trait), 0.00266, 5,
        )

        # No genes
        one_gene = {}
        two_gene = {"James"}
        have_trait = {"James"}
        self.assertAlmostEqual(
            hrd.joint_probability(people, one_gene, two_gene, have_trait),
            0.000060546,
            5,
        )

        # Two genes
        one_gene = {}
        two_gene = {"James", "Harry"}
        have_trait = {"James"}
        self.assertAlmostEqual(
            hrd.joint_probability(people, one_gene, two_gene, have_trait),
            0.000021405,
            5,
        )


if __name__ == "__main__":
    unittest.main()
