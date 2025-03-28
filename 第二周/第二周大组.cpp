#include<stdio.h>
#include<stdlib.h>
#define ElementType int  //自定义数据类型

typedef struct singly *Singly;
struct singly {
    ElementType Data;
    struct singly *Next;  //定义一个单向链表
};

Singly Rear;

int IsEmpty(Singly S) {
    return S->Next == NULL;
}

Singly CreateSinglyList() { //创建链表
    Singly S = (Singly)malloc(sizeof(struct singly));
    S->Next = NULL;
    Rear = S;
    return S; //此处S为头节点，不包含数据
}

void AddSinglyList(Singly S, ElementType item) { //填入数据
    Singly Temp = (Singly)malloc(sizeof(struct singly));
    Temp->Data = item;
    Temp->Next = NULL;
    Rear->Next = Temp;
    Rear = Temp; 
}

void DelSinglyList(Singly S) { //删除数据(队首出队)
    if(IsEmpty(S)) {
        printf("队列空！\n");
        return;
    }
    Singly Temp = S->Next;
    S->Next = Temp->Next;
    if(S->Next == NULL) Rear = S;
    free(Temp);
}

ElementType GetFront(Singly S) { //获取队首元素
    if(IsEmpty(S)) {
        printf("队列空！\n");
        return -1;
    }
    return S->Next->Data;
}

void ClearList(Singly S) { //清空队列
    while(!IsEmpty(S)) {
        DelSinglyList(S);
    }
}

int Length(Singly S) { //队列长度
    int count = 0;
    Singly Temp = S->Next;
    while(Temp != NULL) {
        count++;
        Temp = Temp->Next;
    }
    return count;
}

void PrintSinglyList(Singly S) { //打印链表
    if(IsEmpty(S)) {
        printf("队列为空\n");
        return;
    }
    Singly Temp = S->Next;
    while(Temp != NULL) {
        printf("%d ", Temp->Data);
        Temp = Temp->Next;
    }
    printf("\n");
}

void Option(Singly S, int opt) {
    ElementType item;
    switch(opt) {
        case 1:
            printf("输入元素（仅支持数字）:");
            while(scanf("%d", &item) != 1) {
                printf("请检查并重新输入:");
                while(getchar() != '\n'); // 清除输入缓冲区
            }
            AddSinglyList(S, item);
            break;
        case 2:
            DelSinglyList(S);
            break;
        case 3:
            printf("队列%s\n", IsEmpty(S) ? "空" : "非空");
            break;
        case 4:
            item = GetFront(S);
            if(item != -1) printf("队首元素: %d\n", item);
            break;
        case 5:
            ClearList(S);
            printf("队列已清空\n");
            break;
        case 6:
            printf("队列长度: %d\n", Length(S));
            break;
        case 7:
            ClearList(S);
            printf("队列已重新初始化\n");
            break;
        case 8:
            PrintSinglyList(S);
            break;
    }
}

int main() { //主函数
    Singly S = CreateSinglyList(); //创建链表
    int opt;
    while(1) {
        printf("\n1.元素入队\n2.元素出队\n3.判断队是否为空\n4.取队首元素\n5.清空队\n6.检测队的长度\n7.重新初始化队\n8.打印队\n9.退出程序\n");
        printf("请选择操作:");
        while(scanf("%d", &opt) != 1 || opt < 1 || opt > 9) {
            printf("请正确输入(1-9):");
            while(getchar() != '\n'); // 清除输入缓冲区
        }
        if(opt == 9) {
            printf("感谢使用\n");
            ClearList(S);
            free(S);
            return 0;
        }
        Option(S, opt);
        // 清屏指令，Windows用system("cls")，Linux/Mac用system("clear")
        system("cls"); // 或 system("clear");
    }
}
