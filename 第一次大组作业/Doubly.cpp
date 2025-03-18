#include<stdio.h>
#include<stdlib.h>
#define ElementType int  //自定义数据类型
typedef struct doubly *Doubly;
struct doubly {
    ElementType Data;
    struct doubly *Next;  
    struct doubly *Prev;  //定义一个单向链表(这里用栈结构举例)
};

Doubly CreateDoublyList() //创建链表
{
    Doubly D = (Doubly)malloc(sizeof(struct doubly));
    D->Next = D->Prev = NULL;
    return D; //此处D为头节点，不包含数据
}

void AddDoublyList(Doubly D, ElementType item)  //填入数据
{
    Doubly Temp = (Doubly)malloc(sizeof(struct doubly));
    Temp->Data = item;
    Temp->Next = NULL;
    if (D->Next == NULL)
        D->Next = Temp;
    else {
        D->Next->Prev = Temp;
        Temp->Next = D->Next;
        D->Next = Temp;  //加到头节点处（栈）
    }
    Temp->Prev = D;
}

void DelDoublyList(Doubly D, ElementType item) //删除数据
{
    Doubly Temp; //此处不需要BfTemp了
    Temp = D->Next;
    for (; Temp != NULL; Temp = Temp->Next) {
        if (Temp->Data == item) { //寻找数据对应链
            Temp->Prev->Next = Temp->Next; //前链接后链实现删除(直接用前的后接上后即可)
            free(Temp);  //释放内存
            return;   //直接退出
        }
    }
}

void PrintDoublyList(Doubly D) //打印链表
{
    Doubly Temp;
    Temp = D->Next;
    for (; Temp != NULL; Temp = Temp->Next) {
        printf("%d\n", Temp->Data);
    }
}

int main()  //主函数
{
    Doubly D = CreateDoublyList(); //创建链表
    int i = 3;
    int item;
    while (i--) {  //输入三个数据
        printf("请输入第%d个数据：", 3 - i);
        scanf("%d", &item);
        AddDoublyList(D, item);  //加入链表
    }
    PrintDoublyList(D);  //打印初始链表状态
    printf("请输入要删除的数据：");
    scanf("%d", &item);  
    DelDoublyList(D, item);  //删除数据
    PrintDoublyList(D);  //打印改变后链表状态
    return 0; //结束程序
}
