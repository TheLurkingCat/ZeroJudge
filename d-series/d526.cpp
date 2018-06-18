#include <iostream>
using namespace std;

struct node {
    int value;
    node *parent, *leftChild, *rightChild;
};

void preoder(node *t) {
    cout << t->value << ' ';
    if (t->leftChild != NULL)
        preoder(t->leftChild);

    if (t->rightChild != NULL)
        preoder(t->rightChild);

    return;
}

void freeAll(node *t) {
    if (t->leftChild != NULL)
        freeAll(t->leftChild);
    if (t->rightChild != NULL)
        freeAll(t->rightChild);

    delete t;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int n, num;
    node *head, *ptr;
    while (cin >> n) {
        head = new node;
        head->parent = NULL;
        head->leftChild = NULL;
        head->rightChild = NULL;

        cin >> num;
        head->value = num;

        for (int i = 1; i < n; i++) {
            cin >> num;

            node *new_node = new node;
            new_node->value = num;
            new_node->leftChild = NULL;
            new_node->rightChild = NULL;

            ptr = head;

            while (1) {
                if (new_node->value < ptr->value) {
                    if (ptr->leftChild != NULL)
                        ptr = ptr->leftChild;
                    else {
                        new_node->parent = ptr;
                        ptr->leftChild = new_node;
                        break;
                    }
                } else {
                    if (ptr->rightChild != NULL)
                        ptr = ptr->rightChild;
                    else {
                        new_node->parent = ptr;
                        ptr->rightChild = new_node;
                        break;
                    }
                }
            }
        }

        preoder(head);
        cout << '\n';
        freeAll(head);
    }
}