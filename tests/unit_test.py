import unittest
import lrparse

class TestLRParse(unittest.TestCase):

    # ---------- lr (first match) ----------
    def test_lr_basic(self):
        self.assertEqual(lrparse.lr("pre[mid]post", "[", "]"), ["mid"])

    def test_lr_no_match(self):
        self.assertEqual(lrparse.lr("hello world", "{", "}"), [])

    def test_lr_empty_delimiters(self):
        self.assertEqual(lrparse.lr("abc", "", ""), ["abc"])

    def test_lr_nested_first(self):
        self.assertEqual(lrparse.lr("<a><a>x</a></a>", "<a>", "</a>"), ["<a>x</a>"])

    def test_lr_unbalanced(self):
        self.assertEqual(lrparse.lr("<a>Oops", "<a>", "</a>"), [])

    def test_lr_unicode(self):
        self.assertEqual(lrparse.lr("pre😀mid😀post", "😀", "😀"), ["mid"])

    def test_lr_null_byte(self):
        self.assertEqual(lrparse.lr("ab\0cd<xy>ef", "<", ">"), ["xy"])

    # ---------- lrr (all matches) ----------
    def test_lrr_basic_multiple(self):
        self.assertEqual(lrparse.lrr("<a><b>c", "<", ">"), ["a", "b"])

    def test_lrr_multiple_blocks(self):
        self.assertEqual(lrparse.lrr("<x>1</x><x>2</x>", "<x>", "</x>"), ["1", "2"])

    def test_lrr_nested(self):
        self.assertEqual(
            lrparse.lrr("<a><a>x</a></a><a>y</a>", "<a>", "</a>"),
            ["<a>x</a>", "y"]
        )

    def test_lrr_empty_block(self):
        self.assertEqual(lrparse.lrr("<a></a>", "<a>", "</a>"), [""])

    def test_lrr_unbalanced(self):
        self.assertEqual(lrparse.lrr("<a>x", "<a>", "</a>"), [])

    def test_lrr_same_delimiter_toggle(self):
        self.assertEqual(lrparse.lrr('He said: "Hello" "World"', '"', '"'), ["Hello", "World"])

    def test_lrr_deep_nested(self):
        self.assertEqual(
            lrparse.lrr("<a><a><a>Deep</a></a></a>", "<a>", "</a>"),
            ["<a><a>Deep</a></a>"]
        )


    def test_lrr_null_byte(self):
        self.assertEqual(lrparse.lrr("<a>Te\0st</a>", "<a>", "</a>"), ["Te\0st"])


if __name__ == "__main__":
    unittest.main()
