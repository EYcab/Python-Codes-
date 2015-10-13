/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

// A utility function to get height of the tree
int ht(struct node *N)
{
    if (N == NULL)
        return 0;
    return N->ht;
}
int max(int a, int b);
// A utility function to get maximum of two integers
int max(int a, int b)
{
    return (a > b)? a : b;
}
 
/* Helper function that allocates a new node with the given key and
    NULL left and right pointers. */
struct node* newNode(int val)
{
    struct node* node = (struct node*)
                        malloc(sizeof(struct node));
    node->val  = val;
    node->left   = NULL;
    node->right  = NULL;
    node->ht = 0;  // new node is initially added at leaf
    return(node);
}
 
// A utility function to right rotate subtree rooted with y
// See the diagram given above.
struct node *rightRotate(struct node *y)
{
    struct node *x = y->left;
    struct node *T2 = x->right;
 
    // Perform rotation
    x->right = y;
    y->left = T2;
 
    // Update heights
    y->ht = max(ht(y->left), ht(y->right));
    x->ht = max(ht(x->left), ht(x->right))-1;
 
    // Return new root
    return x;
}
 
// A utility function to left rotate subtree rooted with x
// See the diagram given above.
struct node *leftRotate(struct node *x)
{
    struct node *y = x->right;
    struct node *T2 = y->left;
 
    // Perform rotation
    y->left = x;
    x->right = T2;
 
    //  Update heights
    x->ht = max(ht(x->left), ht(x->right));
    y->ht = max(ht(y->left), ht(y->right))+1;
 
    // Return new root
    return y;
}
 
// Get Balance factor of node N
int getBalance(struct node *N)
{
    if (N == NULL)
        return 0;
    return ht(N->left) - ht(N->right);
}




node * insert(node * node,int val)
{
   /* 1.  Perform the normal BST rotation */
    if (node == NULL)
        return(newNode(val));
 
    if (val < node->val)
        node->left  = insert(node->left, val);
    else
        node->right = insert(node->right, val);
 
    /* 2. Update height of this ancestor node */
    node->ht = max(ht(node->left), ht(node->right)) + 1;
 
    /* 3. Get the balance factor of this ancestor node to check whether
       this node became unbalanced */
    int balance = getBalance(node);
 
    // If this node becomes unbalanced, then there are 4 cases
 
    // Left Left Case
    if (balance > 1 && val < node->left->val)
        return rightRotate(node);
 
    // Right Right Case
    if (balance < -1 && val > node->right->val)
        return leftRotate(node);
 
    // Left Right Case: left ---right
    if (balance > 1 && val > node->left->val)
    {
        node->left =  leftRotate(node->left);
        return rightRotate(node);
    }
 
    // Right Left Case
    if (balance < -1 && val < node->right->val)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }
 
    /* return the (unchanged) node pointer */
    return node;
  
}
// A utility function to print preorder traversal of the tree.
// The function also prints height of every node
void preOrder(struct node *root)
{
    if(root != NULL)
    {
        printf("%d ", root->val);
        preOrder(root->left);
        preOrder(root->right);
    }
}
 /* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

// A utility function to get height of the tree
int ht(struct node *N)
{
    if (N == NULL)
        return 0;
    return N->ht;
}
int max(int a, int b);
// A utility function to get maximum of two integers
int max(int a, int b)
{
    return (a > b)? a : b;
}
 
/* Helper function that allocates a new node with the given key and
    NULL left and right pointers. */
struct node* newNode(int val)
{
    struct node* node = (struct node*)
                        malloc(sizeof(struct node));
    node->val  = val;
    node->left   = NULL;
    node->right  = NULL;
    node->ht = 0;  // new node is initially added at leaf
    return(node);
}
 
// A utility function to right rotate subtree rooted with y
// See the diagram given above.
struct node *rightRotate(struct node *y)
{
    struct node *x = y->left;
    struct node *T2 = x->right;
 
    // Perform rotation
    x->right = y;
    y->left = T2;
 
    // Update heights
    y->ht = max(ht(y->left), ht(y->right));
    x->ht = max(ht(x->left), ht(x->right))-1;
 
    // Return new root
    return x;
}
 
// A utility function to left rotate subtree rooted with x
// See the diagram given above.
struct node *leftRotate(struct node *x)
{
    struct node *y = x->right;
    struct node *T2 = y->left;
 
    // Perform rotation
    y->left = x;
    x->right = T2;
 
    //  Update heights
    x->ht = max(ht(x->left), ht(x->right));
    y->ht = max(ht(y->left), ht(y->right))+1;
 
    // Return new root
    return y;
}
 
// Get Balance factor of node N
int getBalance(struct node *N)
{
    if (N == NULL)
        return 0;
    return ht(N->left) - ht(N->right);
}




node * insert(node * node,int val)
{
   /* 1.  Perform the normal BST rotation */
    if (node == NULL)
        return(newNode(val));
 
    if (val < node->val)
        node->left  = insert(node->left, val);
    else
        node->right = insert(node->right, val);
 
    /* 2. Update height of this ancestor node */
    node->ht = max(ht(node->left), ht(node->right)) + 1;
 
    /* 3. Get the balance factor of this ancestor node to check whether
       this node became unbalanced */
    int balance = getBalance(node);
 
    // If this node becomes unbalanced, then there are 4 cases
 
    // Left Left Case
    if (balance > 1 && val < node->left->val)
        return rightRotate(node);
 
    // Right Right Case
    if (balance < -1 && val > node->right->val)
        return leftRotate(node);
 
    // Left Right Case: left ---right
    if (balance > 1 && val > node->left->val)
    {
        node->left =  leftRotate(node->left);
        return rightRotate(node);
    }
 
    // Right Left Case
    if (balance < -1 && val < node->right->val)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }
 
    /* return the (unchanged) node pointer */
    return node;
  
}
// A utility function to print preorder traversal of the tree.
// The function also prints height of every node
void preOrder(struct node *root)
{
    if(root != NULL)
    {
        printf("%d ", root->val);
        preOrder(root->left);
        preOrder(root->right);
    }
}
 