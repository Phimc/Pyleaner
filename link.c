#include<stdio.h>
typedef struct Link{
	int data;
	struct Link *next;
}link,*list;
link LA = NULL;
link LB = NULL;
link LC = NULL;
void sumlist(list &LA,list &LB, list &LC){
    pa = LA->next;
    pb = LB->next;
    LC = pc = LA;
    while(pa&&pb){
        if(pa->data <= pb->data){
            pc->next = pa;pc = pa;pa = pa->next;
        }
        else{
            pc->next = pb;pc = pb;pb = pb->next;
        }
    }
}