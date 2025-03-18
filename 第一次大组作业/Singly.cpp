#include<stdio.h>
#include<stdlib.h>
#define ElementType int  //自定义数据类型
typedef struct singly *Singly;
struct singly {
    ElementType Data;
    struct singly *Next;  //定义一个单向链表(这里用栈结构举例)
};

Singly CreateSinglyList() //创建链表
{
    Singly S = (Singly)malloc(sizeof(struct singly));
    S->Next = NULL;
    return S; //此处S为头节点，不包含数据
}

void AddSinglyList(Singly S,ElementType item)  //填入数据
{
    Singly Temp = (Singly)malloc(sizeof(struct singly));
    Temp->Data = item;
    Temp->Next = NULL;
    if(S->Next == NULL)
        S->Next = Temp;
    else{
        Temp->Next = S->Next;
        S->Next = Temp;  //加到头节点处（栈）
    }
}

void DelSinglyList(Singly S,ElementType item) //删除数据
{
    Singly Temp;
    Singly BfTemp;
    Temp = S->Next;
    BfTemp = S;
    for( ; Temp!=NULL ; Temp = Temp->Next , BfTemp = BfTemp->Next){
        if(Temp->Data = item){ //寻找数据对应链
            BfTemp->Next = Temp->Next; //前链接后链实现删除
            free(Temp);  //释放内存
            return;   //直接退出
        }
    }
}

void PrintSinglyList(Singly S) //打印链表
{
    Singly Temp;
    Temp = S->Next;
    for( ; Temp!=NULL ; Temp = Temp->Next){
        printf("%d\n",Temp->Data);
    }
}

int main()  //主函数
{
    Singly S = CreateSinglyList(); //创建链表
    int i = 3;
    int item;
    while(i--){  //输入三个数据
        printf("请输入第%d个数据：",3-i);
        scanf("%d",&item);
        AddSinglyList(S,item);  //加入链表
    }
    PrintSinglyList(S);  //打印初始链表状态
    printf("请输入要删除的数据：");
    scanf("%d",&item);  
    DelSinglyList(S,item);  //删除数据
    PrintSinglyList(S);  //打印改变后链表状态
    return 0; //结束程序
}