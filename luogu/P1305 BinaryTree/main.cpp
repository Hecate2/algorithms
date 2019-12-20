#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
using namespace std;

struct node
{
    char data;
    node* lchild;
    node* rchild;
    node* parent;
};

struct node tree[26];//整棵树

void printTree(struct node* root)
{
    if(root)
    {
        printf("%c",root->data);
        printTree(root->lchild);
        printTree(root->rchild);
    }
}

struct node* findRoot(struct node* currentNode)	//找树根
{
    if(currentNode->parent!=NULL)
    {
        return findRoot(currentNode->parent);
    }
    else
    {
        return currentNode;
    }
}

int main()
{
    char currentName='a';
    for(int i=0;i<26;++i)
    {
        tree[i].data=currentName;
        ++currentName;
        tree[i].lchild=NULL;
        tree[i].rchild=NULL;
        tree[i].parent=NULL;
    }
    int n;//节点数
    scanf("%d",&n);
    char s[4];//输入字符串
    int position;//指示输入的节点在tree中的位置
    int nextPosition;//指示输入的节点的儿子在tree中的位置
    for(int i=0;i<n;++i)
    {
        cin>>s;
        position=s[0]-'a';
        if(s[1]!='*')
        {
            nextPosition=s[1]-'a';
            tree[position].lchild=&(tree[nextPosition]);
            tree[nextPosition].parent=&(tree[position]);
        }
//		else
//		{
//			tree[i].lchild=NULL;
//		}

        if(s[2]!='*')
        {
            nextPosition=s[2]-'a';
            tree[position].rchild=&(tree[nextPosition]);
            tree[nextPosition].parent=&(tree[position]);
        }
//		else
//		{
//			tree[i].lchild=NULL;
//		}
    }
    struct node* root=findRoot(&(tree[position]));
    printTree(root);
//    printf("\n");
//    for(int i=0;i<n;++i)
//    {
//        printf("%c %d %d\n",tree[i].data,tree[i].lchild-tree+'a',tree[i].rchild-tree+'a');
//    }
}
