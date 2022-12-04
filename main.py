import os
import sys
import regex as re


def remove_comments(string):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):
        # if the 2nd group (capturing comments) is not None,
        # it means we have captured a non-quoted (real) comment string.
        if match.group(2) is not None:
            return "" # so we will return empty to remove the comment
        else: # otherwise, we will return the 1st group
            return match.group(1) # captured quoted-string
    return regex.sub(_replacer, string)

def ast_parse(java_code):
    try:
        tree = javalang.parse.parse(java_code)
        return tree
    except:
        return None
    
def graph_parse(tree, vector):
    if len(tree.children) > 0:
        for child in tree.children:
            if child:
                for li in child:
                    if li.__class__.__name__ == 'MethodDeclaration':
                        vector["MethodDeclaration"] = vector["MethodDeclaration"] + 1
                    if li.__class__.__name__ == 'IfStatement':
                        vector["IfStatement"] = vector["IfStatement"] + 1
                    if li.__class__.__name__ == 'ForStatement':
                        vector["ForStatement"] = vector["ForStatement"] + 1
                    if li.__class__.__name__ == 'ClassDeclaration':
                        vector["ClassDeclaration"] = vector["ClassDeclaration"] + 1
                    if li.__class__.__name__ == 'WhileStatement':
                        vector["WhileStatement"] = vector["WhileStatement"] + 1
                    if li.__class__.__name__ == 'StatementExpression':
                        vector["StatementExpression"] = vector["StatementExpression"] + 1
                    if li.__class__.__name__ == 'LocalVariableDeclaration':
                        vector["LocalVariableDeclaration"] = vector["LocalVariableDeclaration"] + 1
                    if hasattr(li, 'body'):
                        for node in li.body: 
                            if (not node is None) and (issubclass(type(node), javalang.tree.Statement) or issubclass(type(node), javalang.tree.Expression) or issubclass(type(node), javalang.tree.Declaration)):    
                                left_loop = False
                                if node.__class__.__name__ == 'MethodDeclaration':
                                    vector["MethodDeclaration"] = vector["MethodDeclaration"] + 1
                                if node.__class__.__name__ == 'IfStatement':
                                    vector["IfStatement"] = vector["IfStatement"] + 1
                                if node.__class__.__name__ == 'ForStatement':
                                    vector["ForStatement"] = vector["ForStatement"] + 1
                                    vector["CurrentNestingLevel"] = vector["CurrentNestingLevel"] + 1
                                    if vector["CurrentNestingLevel"] > vector["MaxNestingLevel"]:
                                        vector["MaxNestingLevel"] = vector["CurrentNestingLevel"]
                                    left_loop = True
                                if node.__class__.__name__ == 'ClassDeclaration':
                                    vector["ClassDeclaration"] = vector["ClassDeclaration"] + 1
                                if node.__class__.__name__ == 'WhileStatement':
                                    vector["WhileStatement"] = vector["WhileStatement"] + 1
                                    vector["CurrentNestingLevel"] = vector["CurrentNestingLevel"] + 1
                                    if vector["CurrentNestingLevel"] > vector["MaxNestingLevel"]:
                                        vector["MaxNestingLevel"] = vector["CurrentNestingLevel"]
                                    left_loop = True
                                if node.__class__.__name__ == 'StatementExpression':
                                    vector["StatementExpression"] = vector["StatementExpression"] + 1
                                
                                graph_parse(node, vector)
                                if left_loop: 
                                    vector["CurrentNestingLevel"] = vector["CurrentNestingLevel"] - 1 


def main():
    
   
    java_code = open('./App.java').read()
    nw_code = remove_comments(java_code)

    ast_code = ast_parse(nw_code)
    vect = {"MethodDeclaration": 0, "IfStatement": 0, "ForStatement": 0, 
    "ClassDeclaration": 0, "WhileStatement": 0, "StatementExpression": 0, 
    "LocalVariableDeclaration": 0, "MaxNestingLevel": 0, "CurrentNestingLevel": 0}
    if ast_code is not None:
        graph_code = graph_parse(ast_code, vect)
    print(vect)
    
    
    sys.exit(0)


if __name__ == "__main__":
    main()
