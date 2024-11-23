n = int(input())
arr = dict()
for i in range(n):
    root, left, right = map(str, input().split())
    arr[root]  = [left, right]

def preorder(root):
    if root != '.':
        print(root, end = '')
        left, right = arr[root]
        preorder(left)
        preorder(right)
def inorder(root):
    if root != '.':
        left, right = arr[root]
        inorder(left)
        print(root, end='')
        inorder(right)
def postorder(root):
    if root != '.':
        left, right = arr[root]
        postorder(left)
        postorder(right)
        print(root, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')
