#include<stdio.h>
#include<stdlib.h>
#define ElementType int  //�Զ�����������

typedef struct singly *Singly;
struct singly {
    ElementType Data;
    struct singly *Next;  //����һ����������
};

Singly Rear;

int IsEmpty(Singly S) {
    return S->Next == NULL;
}

Singly CreateSinglyList() { //��������
    Singly S = (Singly)malloc(sizeof(struct singly));
    S->Next = NULL;
    Rear = S;
    return S; //�˴�SΪͷ�ڵ㣬����������
}

void AddSinglyList(Singly S, ElementType item) { //��������
    Singly Temp = (Singly)malloc(sizeof(struct singly));
    Temp->Data = item;
    Temp->Next = NULL;
    Rear->Next = Temp;
    Rear = Temp; 
}

void DelSinglyList(Singly S) { //ɾ������(���׳���)
    if(IsEmpty(S)) {
        printf("���пգ�\n");
        return;
    }
    Singly Temp = S->Next;
    S->Next = Temp->Next;
    if(S->Next == NULL) Rear = S;
    free(Temp);
}

ElementType GetFront(Singly S) { //��ȡ����Ԫ��
    if(IsEmpty(S)) {
        printf("���пգ�\n");
        return -1;
    }
    return S->Next->Data;
}

void ClearList(Singly S) { //��ն���
    while(!IsEmpty(S)) {
        DelSinglyList(S);
    }
}

int Length(Singly S) { //���г���
    int count = 0;
    Singly Temp = S->Next;
    while(Temp != NULL) {
        count++;
        Temp = Temp->Next;
    }
    return count;
}

void PrintSinglyList(Singly S) { //��ӡ����
    if(IsEmpty(S)) {
        printf("����Ϊ��\n");
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
            printf("����Ԫ�أ���֧�����֣�:");
            while(scanf("%d", &item) != 1) {
                printf("���鲢��������:");
                while(getchar() != '\n'); // ������뻺����
            }
            AddSinglyList(S, item);
            break;
        case 2:
            DelSinglyList(S);
            break;
        case 3:
            printf("����%s\n", IsEmpty(S) ? "��" : "�ǿ�");
            break;
        case 4:
            item = GetFront(S);
            if(item != -1) printf("����Ԫ��: %d\n", item);
            break;
        case 5:
            ClearList(S);
            printf("���������\n");
            break;
        case 6:
            printf("���г���: %d\n", Length(S));
            break;
        case 7:
            ClearList(S);
            printf("���������³�ʼ��\n");
            break;
        case 8:
            PrintSinglyList(S);
            break;
    }
}

int main() { //������
    Singly S = CreateSinglyList(); //��������
    int opt;
    while(1) {
        printf("\n1.Ԫ�����\n2.Ԫ�س���\n3.�ж϶��Ƿ�Ϊ��\n4.ȡ����Ԫ��\n5.��ն�\n6.���ӵĳ���\n7.���³�ʼ����\n8.��ӡ��\n9.�˳�����\n");
        printf("��ѡ�����:");
        while(scanf("%d", &opt) != 1 || opt < 1 || opt > 9) {
            printf("����ȷ����(1-9):");
            while(getchar() != '\n'); // ������뻺����
        }
        if(opt == 9) {
            printf("��лʹ��\n");
            ClearList(S);
            free(S);
            return 0;
        }
        Option(S, opt);
        // ����ָ�Windows��system("cls")��Linux/Mac��system("clear")
        system("cls"); // �� system("clear");
    }
}
