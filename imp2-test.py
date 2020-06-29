import unittest
import tatsu                            # Tatsu is the parser generator.

class TestImpGrammar(unittest.TestCase):

    def __test_parse(self, parser, file_name, ast):
        source_h = open(file_name)
        source = source_h.read()
        source_h.close()
        self.assertEqual(str(parser.parse(source)), ast)

    def test_parse(self):
        imp_grammar_h = open('imp2.ebnf')
        imp_grammar = imp_grammar_h.read()
        imp_grammar_h.close()
        parser = tatsu.compile(imp_grammar)
        test_pairs = \
            [('examples/exp-test0.imp2', "AST({'ds': AST({'d': AST({'op': 'var', 'idn': 'x', 'e': 'False'})}), 'cs': AST({'ac': AST({'idn': 'x', 'op': ':=', 'e': AST({'e1': AST({'e': AST({'e1': '1', 'op': '<', 'e2': AST({'e': AST({'e': AST({'e1': '4', 'op': '*', 'e2': AST({'e': AST({'e1': '3', 'op': '/', 'e2': '3'})})})})})})}), 'op': '==', 'e2': 'True'})})})})"), ('examples/exp-test1.imp2',"AST({'ds': AST({'d': AST({'op': 'var', 'idn': 'y', 'e': AST({'e1': 'True', 'op': 'and', 'e2': AST({'e': AST({'e1': 'z', 'op': 'and', 'e2': AST({'e': AST({'op': 'not', 'e': 'True'})})})})})})}), 'cs': None})"), ('examples/exp-test2.imp2', "AST({'ds': [], 'cs': AST({'ac': AST({'idn': 'x', 'op': ':=', 'e': AST({'e1': AST({'e': AST({'e1': '2', 'op': '+', 'e2': '2'})}), 'op': '-', 'e2': '4'})})})})"), ('examples/exp-test3.imp2', "AST({'ds': [], 'cs': AST({'ac': AST({'idn': 'x', 'op': ':=', 'e': AST({'e1': AST({'e': AST({'e1': 'x', 'op': '+', 'e2': '1'})}), 'op': '<', 'e2': '2'})})})})"), ('examples/exp-test4.imp2',"AST({'ds': [], 'cs': AST({'ac': AST({'idn': 'x', 'op': ':=', 'e': AST({'e1': '4', 'op': '+', 'e2': AST({'e1': '3', 'op': '-', 'e2': '5'})})})})})"), ('examples/cmd-test0.imp2', "AST({'ds': AST({'d': AST({'op': 'var', 'idn': ['x', 'y'], 'e': ['10', '1']})}), 'cs': AST({'ac': AST({'op': 'while', 't': AST({'e': AST({'e1': 'x', 'op': '>', 'e2': '0'})}), 'b': AST({'ds': [], 'cs': AST({'ac': [AST({'idn': 'y', 'op': ':=', 'e': AST({'e1': 'y', 'op': '*', 'e2': 'x'})}), AST({'idn': 'x', 'op': ':=', 'e': AST({'e1': 'x', 'op': '-', 'e2': '1'})})]})})})})})"),('examples/cmd-test1.imp2',"AST({'ds': AST({'d': AST({'op': 'var', 'idn': ['x', 'y', 'z'], 'e': ['1', '0', '0']})}), 'cs': AST({'ac': [AST({'idn': 'x', 'op': ':=', 'e': '0'}), AST({'idn': 'y', 'op': ':=', 'e': '1'}), AST({'idn': 'z', 'op': ':=', 'e': '3'}), AST({'op': 'if', 't': AST({'e': AST({'e1': 'x', 'op': '<', 'e2': '2'})}), 'b1': AST({'ds': [], 'cs': AST({'ac': AST({'idn': 'z', 'op': ':=', 'e': '3'})})}), 'b2': None})]})})"), ('examples/def-test0.imp2', "AST({'ds': AST({'d': AST({'op': 'def', 'idn': 'fat', 'f': ['x'], 'b': AST({'ds': AST({'d': [AST({'op': 'var', 'idn': 'z', 'e': 'x'}), AST({'op': 'var', 'idn': 'y', 'e': '1'})]}), 'cs': AST({'ac': AST({'op': 'while', 't': AST({'e': AST({'e1': 'z', 'op': '>', 'e2': '0'})}), 'b': AST({'ds': [], 'cs': AST({'ac': [AST({'idn': 'y', 'op': ':=', 'e': AST({'e1': 'y', 'op': '*', 'e2': 'z'})}), AST({'idn': 'z', 'op': ':=', 'e': AST({'e1': 'z', 'op': '-', 'e2': '1'})})]})})})})})})}), 'cs': AST({'ac': AST({'idn': 'fat', 'a': ['10']})})})"), ('examples/def-test1.imp2',"AST({'ds': AST({'d': AST({'op': 'def', 'idn': 'fat', 'f': ['x', ',', 'y'], 'b': AST({'ds': [], 'cs': AST({'ac': AST({'op': 'if', 't': AST({'e': AST({'e1': 'x', 'op': '>', 'e2': '0'})}), 'b1': AST({'ds': [], 'cs': AST({'ac': AST({'idn': 'fat', 'a': [AST({'e1': 'x', 'op': '-', 'e2': '1'}), ',', AST({'e1': 'y', 'op': '*', 'e2': 'x'})]})})}), 'b2': None})})})})}), 'cs': AST({'ac': AST({'idn': 'fat', 'a': ['10', ',', '1']})})})")]
        for (file_name, ast) in test_pairs:
            self.__test_parse(parser, file_name, ast)
           
if __name__ == '__main__':
    unittest.main()
