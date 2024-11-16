# main.py

import sys

# Token and Tokenizer Classes

class Token:
    def __init__(self, type: str, value):
        self.type = type
        self.value = value

class Tokenizer:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.next = None
        self.select_next()
    
    def select_next(self):
        while self.position < len(self.source):
            char = self.source[self.position]
            if char in ' \t\n':
                self.position += 1
            elif char == '/':
                # Check for comments
                if self.position + 1 < len(self.source) and self.source[self.position + 1] == '/':
                    # Single-line comment, skip until end of line
                    self.position += 2
                    while self.position < len(self.source) and self.source[self.position] != '\n':
                        self.position += 1
                else:
                    # Division operator
                    self.next = Token('OP', '/')
                    self.position += 1
                    return
            else:
                break
        
        if self.position >= len(self.source):
            self.next = Token('EOF', None)
            return
        
        char = self.source[self.position]

        if char.isdigit():
            num = ''
            while self.position < len(self.source) and self.source[self.position].isdigit():
                num += self.source[self.position]
                self.position +=1
            self.next = Token('INT', int(num))
        
        elif char.isalpha() or char == '_':
            id_str = ''
            while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
                id_str += self.source[self.position]
                self.position +=1
            if id_str == 'account':
                self.next = Token('ACCOUNT', id_str)
            elif id_str == 'if':
                self.next = Token('IF', id_str)
            elif id_str == 'else':
                self.next = Token('ELSE', id_str)
            elif id_str == 'while':
                self.next = Token('WHILE', id_str)
            elif id_str == 'transfer':
                self.next = Token('TRANSFER', id_str)
            elif id_str == 'cashout':
                self.next = Token('CASHOUT', id_str)
            else:
                self.next = Token('IDENTIFIER', id_str)
        elif char == '=':
            self.position +=1
            if self.position < len(self.source) and self.source[self.position] == '=':
                self.next = Token('RELOP', '==')
                self.position +=1
            else:
                self.next = Token('ASSIGN', '=')
        elif char in '+-*/':
            self.next = Token('OP', char)
            self.position +=1
        elif char in '<>!':
            self.position +=1
            if self.position < len(self.source) and self.source[self.position] == '=':
                if char == '<':
                    self.next = Token('RELOP', '<=')
                elif char == '>':
                    self.next = Token('RELOP', '>=')
                elif char == '!':
                    self.next = Token('RELOP', '!=')
                self.position +=1
            else:
                self.next = Token('RELOP', char)
        elif char == ';':
            self.next = Token('SEMI', char)
            self.position +=1
        elif char == '(':
            self.next = Token('LPAREN', char)
            self.position +=1
        elif char == ')':
            self.next = Token('RPAREN', char)
            self.position +=1
        elif char == '{':
            self.next = Token('LBRACE', char)
            self.position +=1
        elif char == '}':
            self.next = Token('RBRACE', char)
            self.position +=1
        else:
            raise ValueError(f"Invalid character: {char}")

# AST Node Classes

class Node:
    def evaluate(self, symbol_table):
        pass

class NumberNode(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, symbol_table):
        return self.value

class VariableNode(Node):
    def __init__(self, name):
        self.name = name

    def evaluate(self, symbol_table):
        return symbol_table.get(self.name)

class BinOpNode(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self, symbol_table):
        left_val = self.left.evaluate(symbol_table)
        right_val = self.right.evaluate(symbol_table)
        if self.op == '+':
            return left_val + right_val
        elif self.op == '-':
            return left_val - right_val
        elif self.op == '*':
            return left_val * right_val
        elif self.op == '/':
            if right_val == 0:
                raise ValueError("Division by zero")
            return left_val // right_val
        elif self.op == '<':
            return 1 if left_val < right_val else 0
        elif self.op == '>':
            return 1 if left_val > right_val else 0
        elif self.op == '==':
            return 1 if left_val == right_val else 0
        elif self.op == '<=':
            return 1 if left_val <= right_val else 0
        elif self.op == '>=':
            return 1 if left_val >= right_val else 0
        elif self.op == '!=':
            return 1 if left_val != right_val else 0
        else:
            raise ValueError(f"Unknown operator: {self.op}")

class AssignmentNode(Node):
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def evaluate(self, symbol_table):
        value = self.expression.evaluate(symbol_table)
        symbol_table.set(self.name, value)
        return value

class DeclarationNode(Node):
    def __init__(self, name, expression=None):
        self.name = name
        self.expression = expression

    def evaluate(self, symbol_table):
        if symbol_table.exists_in_current_scope(self.name):
            raise ValueError(f"Variable '{self.name}' already declared in this scope")
        if self.expression:
            value = self.expression.evaluate(symbol_table)
        else:
            value = 0
        symbol_table.declare(self.name, value)
        return value

class IfNode(Node):
    def __init__(self, condition, true_block, false_block=None):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

    def evaluate(self, symbol_table):
        condition_value = self.condition.evaluate(symbol_table)
        if condition_value:
            new_scope = SymbolTable(symbol_table)
            self.true_block.evaluate(new_scope)
        elif self.false_block:
            new_scope = SymbolTable(symbol_table)
            self.false_block.evaluate(new_scope)

class WhileNode(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def evaluate(self, symbol_table):
        while self.condition.evaluate(symbol_table):
            new_scope = SymbolTable(symbol_table)
            self.body.evaluate(new_scope)

class StatementsNode(Node):
    def __init__(self):
        self.statements = []

    def add(self, statement):
        self.statements.append(statement)

    def evaluate(self, symbol_table):
        for stmt in self.statements:
            stmt.evaluate(symbol_table)

class CashoutNode(Node):
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, symbol_table):
        value = self.expression.evaluate(symbol_table)
        print(value)

class UnOpNode(Node):
    def __init__(self, op, child):
        self.op = op
        self.child = child

    def evaluate(self, symbol_table):
        value = self.child.evaluate(symbol_table)
        if self.op == '+':
            return +value
        elif self.op == '-':
            return -value
        else:
            raise ValueError(f"Unknown unary operator: {self.op}")

# Symbol Table with Scoping

class SymbolTable:
    def __init__(self, parent=None):
        self.table = {}
        self.parent = parent  # Reference to the parent scope

    def declare(self, name, value=0):
        if name in self.table:
            raise ValueError(f"Variable '{name}' already declared in this scope")
        self.table[name] = value

    def set(self, name, value):
        if name in self.table:
            self.table[name] = value
        elif self.parent:
            self.parent.set(name, value)
        else:
            raise ValueError(f"Variable '{name}' not declared")
    
    def get(self, name):
        if name in self.table:
            return self.table[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise ValueError(f"Variable '{name}' not declared")
    
    def exists(self, name):
        if name in self.table:
            return True
        elif self.parent:
            return self.parent.exists(name)
        else:
            return False

    def exists_in_current_scope(self, name):
        return name in self.table

# Parser

class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def parse(self):
        node = self.parseStatements()
        if self.tokenizer.next.type != 'EOF':
            raise ValueError("Unexpected token after program end")
        return node

    def parseStatements(self):
        statements = StatementsNode()
        while self.tokenizer.next.type != 'EOF' and self.tokenizer.next.type != 'RBRACE':
            stmt = self.parseStatement()
            statements.add(stmt)
        return statements

    def parseStatement(self):
        if self.tokenizer.next.type == 'ACCOUNT':
            self.tokenizer.select_next()
            if self.tokenizer.next.type != 'IDENTIFIER':
                raise ValueError("Expected identifier after 'account'")
            name = self.tokenizer.next.value
            self.tokenizer.select_next()
            if self.tokenizer.next.type == 'ASSIGN':
                self.tokenizer.select_next()
                expression = self.parseRelExpression()
                if self.tokenizer.next.type != 'SEMI':
                    raise ValueError("Expected ';' after declaration")
                self.tokenizer.select_next()
                return DeclarationNode(name, expression)
            elif self.tokenizer.next.type == 'SEMI':
                self.tokenizer.select_next()
                return DeclarationNode(name)
            else:
                raise ValueError("Expected '=' or ';' after variable name")
        elif self.tokenizer.next.type == 'IDENTIFIER':
            name = self.tokenizer.next.value
            self.tokenizer.select_next()
            if self.tokenizer.next.type == 'ASSIGN':
                self.tokenizer.select_next()
                expression = self.parseRelExpression()
                if self.tokenizer.next.type != 'SEMI':
                    raise ValueError("Expected ';' after assignment")
                self.tokenizer.select_next()
                return AssignmentNode(name, expression)
            else:
                raise ValueError("Expected '=' after identifier")
        elif self.tokenizer.next.type == 'CASHOUT':
            self.tokenizer.select_next()
            if self.tokenizer.next.type != 'LPAREN':
                raise ValueError("Expected '(' after 'cashout'")
            self.tokenizer.select_next()
            expression = self.parseRelExpression()
            if self.tokenizer.next.type != 'RPAREN':
                raise ValueError("Expected ')' after 'cashout' expression")
            self.tokenizer.select_next()
            if self.tokenizer.next.type != 'SEMI':
                raise ValueError("Expected ';' after 'cashout' statement")
            self.tokenizer.select_next()
            return CashoutNode(expression)
        elif self.tokenizer.next.type == 'IF':
            self.tokenizer.select_next()
            if self.tokenizer.next.type != 'LPAREN':
                raise ValueError("Expected '(' after 'if'")
            self.tokenizer.select_next()
            condition = self.parseRelExpression()
            if self.tokenizer.next.type != 'RPAREN':
                raise ValueError("Expected ')' after condition")
            self.tokenizer.select_next()
            if self.tokenizer.next.type != 'LBRACE':
                raise ValueError("Expected '{' after 'if' condition")
            self.tokenizer.select_next()
            true_block = self.parseStatements()
            if self.tokenizer.next.type != 'RBRACE':
                raise ValueError("Expected '}' after 'if' block")
            self.tokenizer.select_next()
            false_block = None
            if self.tokenizer.next.type == 'ELSE':
                self.tokenizer.select_next()
                if self.tokenizer.next.type != 'LBRACE':
                    raise ValueError("Expected '{' after 'else'")
                self.tokenizer.select_next()
                false_block = self.parseStatements()
                if self.tokenizer.next.type != 'RBRACE':
                    raise ValueError("Expected '}' after 'else' block")
                self.tokenizer.select_next()
            return IfNode(condition, true_block, false_block)
        elif self.tokenizer.next.type == 'WHILE':
            self.tokenizer.select_next()
            if self.tokenizer.next.type != 'LPAREN':
                raise ValueError("Expected '(' after 'while'")
            self.tokenizer.select_next()
            condition = self.parseRelExpression()
            if self.tokenizer.next.type != 'RPAREN':
                raise ValueError("Expected ')' after condition")
            self.tokenizer.select_next()
            if self.tokenizer.next.type != 'LBRACE':
                raise ValueError("Expected '{' after 'while' condition")
            self.tokenizer.select_next()
            body = self.parseStatements()
            if self.tokenizer.next.type != 'RBRACE':
                raise ValueError("Expected '}' after 'while' block")
            self.tokenizer.select_next()
            return WhileNode(condition, body)
        else:
            raise ValueError(f"Unknown statement: {self.tokenizer.next.type}")

    def parseRelExpression(self):
        left = self.parseExpression()
        while self.tokenizer.next.type == 'RELOP':
            op = self.tokenizer.next.value
            self.tokenizer.select_next()
            right = self.parseExpression()
            left = BinOpNode(left, op, right)
        return left

    def parseExpression(self):
        left = self.parseTerm()
        while self.tokenizer.next.type == 'OP' and self.tokenizer.next.value in '+-':
            op = self.tokenizer.next.value
            self.tokenizer.select_next()
            right = self.parseTerm()
            left = BinOpNode(left, op, right)
        return left

    def parseTerm(self):
        left = self.parseFactor()
        while self.tokenizer.next.type == 'OP' and self.tokenizer.next.value in '*/':
            op = self.tokenizer.next.value
            self.tokenizer.select_next()
            right = self.parseFactor()
            left = BinOpNode(left, op, right)
        return left

    def parseFactor(self):
        if self.tokenizer.next.type == 'INT':
            node = NumberNode(self.tokenizer.next.value)
            self.tokenizer.select_next()
            return node
        elif self.tokenizer.next.type == 'IDENTIFIER':
            node = VariableNode(self.tokenizer.next.value)
            self.tokenizer.select_next()
            return node
        elif self.tokenizer.next.type == 'LPAREN':
            self.tokenizer.select_next()
            node = self.parseRelExpression()
            if self.tokenizer.next.type != 'RPAREN':
                raise ValueError("Expected ')'")
            self.tokenizer.select_next()
            return node
        elif self.tokenizer.next.type == 'OP' and self.tokenizer.next.value in '+-':
            op = self.tokenizer.next.value
            self.tokenizer.select_next()
            node = self.parseFactor()
            return UnOpNode(op, node)
        else:
            raise ValueError("Unexpected token in factor")

# Main Program

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <source_file>")
        return
    with open(sys.argv[1], 'r') as f:
        source_code = f.read()
    tokenizer = Tokenizer(source_code)
    parser = Parser(tokenizer)
    try:
        ast = parser.parse()
        symbol_table = SymbolTable()
        ast.evaluate(symbol_table)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()